import clingo

from query import num_col_data


def print_answer_sets(program):
    control = clingo.Control()
    control.add("base", [], program)
    control.ground([("base", [])])
    control.configuration.solve.models = 0
    for model in control.solve(yield_=True):
        sorted_model = [str(atom) for atom in model.symbols(shown=True)]
        sorted_model.sort()
        print("Answer set: {{{}}}".format(", ".join(sorted_model)))


def print_answer_sets1():
    control = clingo.Control()
    control.add("base", ["-c", "k=3"], "")
    control.load("lp-files/generated/data/data.lp")
    #control.load("data/enc1.lp")
    control.ground([("base", [])])
    control.configuration.solve.models = 0
    for model in control.solve(yield_=True):
        sorted_model = [str(atom) for atom in model.symbols(shown=True)]
        sorted_model.sort()
        print("Answer set: {{{}}}".format(", ".join(sorted_model)))


def generate_priority_counts():
    count = 0
    control = clingo.Control()
    control.add("base", [], "")
    control.load("lp-files/fixed-solution/gen-priority-counts.lp")
    control.load("lp-files/priorities/col-priorities.lp")
    control.load("lp-files/generated/solution/columns.lp")
    control.add('#show priority_count/2.#show priority_number/2.')
    control.ground([("base", [])])
    control.configuration.solve.models = 0

    f = open("lp-files/priorities/generated/priority-counts.lp", "w")
    priority_counts = set()
    for model in control.solve(yield_=True):
        for atom in model.symbols(shown=True):
            priority_counts.add(atom)
            #f.write(str(atom) + ".\n")

    for pc in priority_counts:
        f.write(str(str(pc)) + ".\n")
    f.close()


def generate_column_combinations():
    control = clingo.Control()
    control.add("base", [], "")
    control.load("lp-files/fixed-solution/gen-priority-counts.lp")
    control.load("lp-files/fixed-solution/gen-column-combinations.lp")
    control.load("lp-files/priorities/col-priorities.lp")
    control.load("lp-files/generated/solution/columns.lp")
    control.ground([("base", [])])
    control.configuration.solve.models = 0
    count = 1

    f = open("lp-files/generated/solution/col-combs.lp", "w")
    comb_str = ""

    for model in control.solve(yield_=True):
        for atom in model.symbols(shown=True):
            f.write("comb(" + str(atom) + "," + str(count) + ").\n")
        count = count + 1
    print(count)
    for y in range(1, count):
        comb_str += "comb(" + str(y) + ")"
        if y +1== count:
            comb_str += "."
        else:
            comb_str += "|"
    f.write(comb_str)
    f.close()

    """for model in control.solve(yield_=True):
        sorted_model = [str(atom) for atom in model.symbols(shown=True)]
        sorted_model.sort()
        print("Answer set: {{{}}}".format(", ".join(sorted_model)))"""
    return count


def generate_k_anonym_data():
    control = clingo.Control(["--opt-mode=optN", "-c", "k=7"])
    control.add("base", [], "")
    control.load("lp-files/generated/data/data.lp")
    control.load("lp-files/generated/solution/col-combs.lp")
    del_c_str = ""
    for h in range(1, num_col_data() - 2):
        if h != num_col_data():
            del_c_str += "del_c(" + str(h) + ")"
            del_c_str += "|"
    del_c_str=del_c_str[:-1]
    del_c_str+="."
    print(del_c_str)
    control.add(del_c_str)

    control.load("lp-files/generated/solution/columns.lp")
    control.load("lp-files/generated/solution/priority-distr.lp")
    control.load("lp-files/generated/solution/enc.lp")
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
    ids=[]
    #control = clingo.Control(["-c", "id=7"])
    control = clingo.Control()
    control.add("base", [], "")
    control.load("lp-files/generated/data/data.lp")
    control.add("#show person/1.")
    control.ground([("base", [])])
    control.configuration.solve.models = 0
    for model in control.solve(yield_=True):
        for atom in model.symbols(shown=True):
            ids.append(atom.arguments[0])


    print(atom.arguments[0])
    for i in ids:
        arg = "id=" + str(i)
        #print(arg)
        control1 = clingo.Control(["-c", arg])
        control1.load("lp-files/generated/data-to-be-exported/data-3.lp")
        control1.load("lp-files/generated/solution/get-item.lp")
        control1.ground([("base", [])])
        control1.configuration.solve.models = 0
        for model in control1.solve(yield_=True):
            for atom in model.symbols(shown=True):
                print(str(atom))
                #print(str(atom) + ".\n")


def generate_priority_distribution():
    control = clingo.Control()
    control.add("base", [], "")
    control.load("lp-files/fixed-solution/cnt.lp")
    control.load("lp-files/priorities/generated/priority-counts.lp")
    control.ground([("base", [])])
    control.configuration.solve.models = 0

    f = open("lp-files/generated/solution/priority-distr.lp", "w")
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
