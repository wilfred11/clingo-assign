import clingo
from query import num_col_data


def generate_priority_counts():
    count = 0
    control = clingo.Control()
    control.add("base", [], "")
    control.load("lp-files/fixed-solution/gen-priority-counts-numbers.lp")
    control.load("lp-files/priorities/col-priorities.lp")
    control.load("lp-files/fixed-solution/count-cols-priorities.lp")
    control.load("lp-files/generated/solution/columns.lp")
    control.add('#show priority_count/2.#show priority_number/2.')
    control.ground([("base", [])])
    control.configuration.solve.models = 0

    f = open("lp-files/priorities/generated/priority-counts.lp", "w")
    for model in control.solve(yield_=True):
        for atom in model.symbols(shown=True):
            f.write(str(atom) + ".\n")
    f.close()


def generate_column_combinations():
    control = clingo.Control()

    control.add("base", [], "")
    control.load("lp-files/priorities/generated/priority-counts.lp")
    control.load("lp-files/fixed-solution/gen-column-combinations.lp")
    control.load("lp-files/fixed-solution/count-cols-priorities.lp")
    control.load("lp-files/priorities/col-priorities.lp")
    control.load("lp-files/generated/solution/columns.lp")
    control.ground([("base", [])])
    control.configuration.solve.models = 0
    count = 1

    f = open("lp-files/generated/solution/col-combs.lp", "w")
    comb_str = ""

    with (control.solve(yield_=True) as handle):
        for model in handle:
            model_control = clingo.Control(["-c", "comb_n=" + str(model.number)])
            model_control.add("base", [], "")
            model_control.add("comb(col_priority(X1,S,T),comb_n) :- col_priority(X1,S,T).")
            model_control.add("#show comb/2.")
            for atom in model.symbols(shown=True):
                model_control.add(str(atom) + ".")

            model_control.ground([("base", [])])
            model_control.configuration.solve.models = 0
            with model_control.solve(yield_=True) as modelhandle:
                for model_ in modelhandle:
                    for atom in model_.symbols(shown=True):
                        f.write(str(atom) + ".\n")
            count = count + 1

    for y in range(1, count):
        comb_str += "comb(" + str(y) + ")"
        if y + 1 == count:
            comb_str += "."
        else:
            comb_str += "|"
    f.write(comb_str)
    f.close()


def generate_k_anonym_data():
    control = clingo.Control(["--opt-mode=optN", "-c", "k=4"])
    control.add("base", [], "")
    control.load("lp-files/generated/data/data.lp")
    control.load("lp-files/generated/solution/col-combs.lp")

    del_c_str = "del_c(0)|"
    for h in range(1, num_col_data() - 2):
        if h != num_col_data():
            del_c_str += "del_c(" + str(h) + ")"
            del_c_str += "|"
    del_c_str = del_c_str[:-1]
    del_c_str += "."
    print(del_c_str)
    control.add(del_c_str)

    control.load("lp-files/generated/solution/columns.lp")
    control.load("lp-files/generated/solution/priority-deletion-rank.lp")
    control.load("lp-files/fixed-solution/search-constraints.lp")
    control.load("lp-files/generated/solution/col-specific-hide.lp")
    control.load("lp-files/generated/solution/values.lp")
    control.ground([("base", [])])
    control.configuration.solve.models = 0
    count = 1

    for model in control.solve(yield_=True):
        if model.optimality_proven:
            f = open("lp-files/generated/data-to-be-exported/data-" + str(count) + ".lp", "w")
            for atom in model.symbols(shown=True):
                f.write(str(atom) + ".\n")
            f.close()
        count = count + 1


def generate_csv_from_asp():
    ids = []
    control = clingo.Control()
    control.add("base", [], "")
    control.load("lp-files/generated/data-to-be-exported/data-3.lp")
    control.add("#show person/1.")
    control.ground([("base", [])])
    control.configuration.solve.models = 0
    for model in control.solve(yield_=True):
        for atom in model.symbols(shown=True):
            ids.append(atom.arguments[0])

    f = open("lp-files/generated/data-to-be-exported/data-3.csv", "w")
    for i in ids:
        arg = "id=" + str(i)
        control1 = clingo.Control(["-c", arg])
        control1.load("lp-files/generated/data-to-be-exported/data-3.lp")
        control1.load("lp-files/generated/solution/get-item.lp")
        control1.load("lp-files/generated/solution/values.lp")
        control1.ground([("base", [])])
        control1.configuration.solve.models = 0
        f.write(str(i))
        f.write(";")
        for model in control1.solve(yield_=True):
            for atom in model.symbols(shown=True):
                f.write(str(atom.arguments[1]))
                f.write(";")
            f.write("\n")
    f.close()


def add_deletion_rank():
    control = clingo.Control()
    control.add("base", [], "")
    control.load("lp-files/fixed-solution/add-deletion-rank-priority-numbers.lp")
    control.load("lp-files/priorities/col-priorities.lp")
    control.load("lp-files/fixed-solution/count-cols-priorities.lp")
    control.load("lp-files/priorities/generated/priority-counts.lp")
    control.ground([("base", [])])
    control.configuration.solve.models = 0

    f = open("lp-files/generated/solution/priority-deletion-rank.lp", "w")
    for model in control.solve(yield_=True):
        for atom in model.symbols(shown=True):
            f.write(str(atom) + ".\n")
    f.close()


def check_k_anon_comb():
    control = clingo.Control()
    control.add("base", [], "")
    control.load("data/columns.lp")
    control.load("data/col-comb-1.lp")
    control.load("data/col-select.lp")
    control.ground([("base", [])])
    control.configuration.solve.models = 0
    for model in control.solve(yield_=True):
        sorted_model = [str(atom) for atom in model.symbols(shown=True)]
        sorted_model.sort()
        print("Answer set: {{{}}}".format(", ".join(sorted_model)))
