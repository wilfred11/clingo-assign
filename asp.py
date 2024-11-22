import clingo


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
    count=0
    control = clingo.Control()
    control.add("base", [], "")
    control.load("lp-files/fixed-solution/gen-priority-counts.lp")
    control.load("lp-files/priorities/col-priorities.lp")
    control.load("lp-files/generated/solution/columns.lp")
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

    for model in control.solve(yield_=True):
        f = open("lp-files/generated/solution/col-comb-"+str(count)+".lp", "w")
        #facts = set()
        for atom in model.symbols(shown=True):
            #print(str(atom))
            #facts.add(atom)
            f.write(str(atom) + ".\n")
        f.close()
        count= count+1

    """for atom in facts:
        f.write(str(atom)+".\n")"""
    f.close()

    #control1 = clingo.Control()
    #control1.add(m)
    #print(control.solve(on_model=print))

    for model in control.solve(yield_=True):
        sorted_model = [str(atom) for atom in model.symbols(shown=True)]
        sorted_model.sort()
        print("Answer set: {{{}}}".format(", ".join(sorted_model)))

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


