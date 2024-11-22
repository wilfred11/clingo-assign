import clingo

from asp import print_answer_sets, print_answer_sets1, generate_column_combinations, check_k_anon_comb, generate_priority_counts
from query import read_data, check, quasi_identifiers, create_initial_lp_data, quasi_identifiers1, create_string_data

do = 4
random_state = 10

if do==1:
    program = '''    
        {a}.
        b:- a.
        :- not b.
    '''

    with open('program.lp', mode='w') as file:
        file.write(program)
    print_answer_sets(program)

if do==11:
    _file = "data/data.lp"

    with open(_file, 'r') as file:
        instance = file.read().replace("\n"," ")
    print(instance)

    print_answer_sets(instance)

if do == 2:
    print("creating initial lp files")
    data = read_data("datainfo.csv", random_state, 2000)
    check(data, quasi_identifiers1())
    create_initial_lp_data(data, quasi_identifiers1())
    #instance = create_string_data(data, quasi_identifiers1())
    #print(instance)
    #print_answer_sets1()
if do == 3:
    generate_priority_counts()

if do == 4:
    generate_column_combinations()

if do == 5:
    check_k_anon_comb()