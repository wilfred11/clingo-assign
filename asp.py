import clingo

from query import num_col_data
from clingo.symbol import Function, Number, parse_term



import sys
from clingo.application import Application, clingo_main

class ClingoApp(Application):
    def __init__(self, name):
        self.program_name = name

    def main(self, ctl, files):
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground([("base", [])])
        ctl.solve()


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

def on_model(m):
    m.context.add_clause([(Function("comb_id", [Number(1)]), False)])
def generate_column_combinations():
    control = clingo.Control()


    control.add("base", [], "")
    #control.load("lp-files/fixed-solution/gen-priority-counts-numbers.lp")
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
            control_model = clingo.Control(["-c", "comb_n="+str(model.number)])
            control_model.add("base", [], "")
            #control_model.load("lp-files/generated/solution/columns.lp")
            #control_model.add("comb(col_priority(X1,S,T),comb_n) :- col_priority(X1,S,T), column(X1).")
            control_model.add("comb(col_priority(X1,S,T),comb_n) :- col_priority(X1,S,T).")
            control_model.add("#show comb/2.")
            for atom in model.symbols(shown=True):
                control_model.add(str(atom)+".")

            control_model.ground([("base", [])])
            control_model.configuration.solve.models = 0
            with control_model.solve(yield_=True) as modelhandle:
                for model1 in modelhandle:
                    for atom in model1.symbols(shown=True):
                        f.write(str(atom)+".\n")
            count=count+1

    for y in range(1, count):
        comb_str += "comb(" + str(y) + ")"
        if y +1== count:
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
    control.load("lp-files/fixed-solution/gen-asp-data-files.lp")
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
    ids=[]
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

def add_count_priority():
    control = clingo.Control()
    control.add("base", [], "")
    control.load("lp-files/fixed-solution/add-count-priority-numbers.lp")
    control.load("lp-files/priorities/col-priorities.lp")
    control.load("lp-files/fixed-solution/count-cols-priorities.lp")
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
