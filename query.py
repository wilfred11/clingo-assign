import pandas as pd


def quasi_identifiers():
    return ["age","sex", "married_status", "job","religion","city"]

def quasi_identifiers1():
    return ["sex", "married_status", "job","religion"]

def check(df, columns):
    df = df[columns]
    print("length:", len(df))
    print(df.head())
    aggreg_query = df.groupby(columns).size().reset_index().rename(columns={0: 'count'})
    #print(aggreg_query.loc[aggreg_query['count'] > 1])
    print(aggreg_query['count'].value_counts())

def create_initial_lp_data(df, columns):
    df = df[columns]
    d = dict()
    for col in df.columns:
        d[col] = set()

    f = open("lp-files/generated/solution/columns.lp", "w")
    for col in df.columns:
        f.write("column(" + col + ").")
        f.write("\n")
    f.close()
    print("columns.lp generated")
    f = open("lp-files/generated/data/data.lp", "w")
    for ind in df.index:
        f.write("person("+str(ind)+").")
        f.write("\n")
        for col in df.columns:
            col_value = str(df[col][ind]).replace(" ", "_")
            col_value = col_value.lower()
            f.write("p_"+ col+"("+str(ind)+"," + col_value +").")
            f.write("\n")
            d[col].add(col_value)

    for col in df.columns:
        for val in d[col]:
            f.write(col+"("+val + ").")
            f.write("\n")
    f.close()
    print("data.lp generated")


def create_string_data(df, columns):
    df = df[columns]
    s=""
    for ind in df.index:
        s += "person("+str(ind)+"). "
        for col in df.columns:
            s += col+"("+str(ind)+"," + str(df[col][ind])+"). "
    #f.write("Now the file has more content!")
    return s


def read_data(name, random_state, n=0):
    # Read the CSV file
    student_performance_data = pd.read_csv("data/"+name)
    print(student_performance_data.head())
    if n==0:
        return student_performance_data
    else:
        return student_performance_data.sample(n=n,random_state=random_state)

