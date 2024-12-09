import clingo

from asp import generate_column_combinations, \
    generate_priority_counts, add_deletion_rank, generate_k_anonym_data, generate_csv_from_asp
from query import read_data, check, quasi_identifiers, create_initial_lp_data, quasi_identifiers1, create_string_data

do = 4
random_state = 10


if do == 2:
    print("creating initial lp files")
    data = read_data("datainfo.csv", random_state, 100)
    check(data, quasi_identifiers1())
    create_initial_lp_data(data, quasi_identifiers1())

if do == 3:
    generate_priority_counts()

if do == 4:
    generate_column_combinations()

if do == 5:
    add_deletion_rank()

if do == 6:
    generate_k_anonym_data()
if do == 7:
    generate_csv_from_asp()