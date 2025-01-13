import pandas as pd


def quasi_identifiers():
    return ["age","sex", "married_status", "job","religion","city"]

def quasi_identifiers1():
    return ["sex", "married_status", "job","religion"]

def num_col_data():
    return len(quasi_identifiers())

def check(df, columns):
    df = df[columns]

    print("length:", len(df))
    print(df.head())
    aggreg_query = df.groupby(columns).size().reset_index().rename(columns={0: 'count'})
    print(aggreg_query)
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
    f.close()
    print("data.lp generated")

    f = open("lp-files/generated/solution/values.lp", "w")
    for col in df.columns:
        for val in d[col]:
            f.write(col+"("+val + ").")
            f.write("\n")
        f.write(col+"(na).")
        f.write("\n")
    f.write("val(na).\n")
    f.close()
    print("values.lp generated")

    f = open("lp-files/generated/solution/get-item.lp", "w")
    f.write("person_(X) :- person(X), X=id.\n")
    f.write("p_sex__(X, Y) :- p_sex_(X, Y), X=id.\n")
    f.write("p_married_status__(X, Y) :- p_married_status_(X, Y), X=id.\n")
    f.write("p_religion__(X, Y) :- p_religion_(X, Y), X=id.\n")
    f.write("p_job__(X, Y) :- p_job_(X, Y), X=id.\n")
    f.write("#show p_sex__/2.\n")
    f.write("#show p_job__/2.\n")
    f.write("#show p_religion__/2.\n")
    f.write("#show p_married_status__/2.\n")
    f.close()
    print("get-item.lp generated.")

    f = open("lp-files/generated/solution/col-specific-hide.lp", "w")
    tmp=""
    tmp1=""
    tmp2=""
    count =0
    for col in df.columns:
        f.write("p_"+ col + "_(X,na) :- p_"+ col + "(X,_), hide_column("+col+",_).")
        f.write("\n")
        f.write("p_" + col + "_(X,Y) :- p_" + col + "(X,Y), not hide_column(" + col + ",_).")
        f.write("\n")
        tmp+= col + "(X"+ str(count) +"),"
        tmp1+="X"+str(count)+","
        tmp2+= "p_"+ col + "_(X,X" +str(count)+"),"
        count=count+1
    tmp1=tmp1[:-1]
    tmp= tmp[:-1]
    tmp2 = tmp2[:-1]
    f.write("count_ext("+tmp1+",N) :-" + tmp +",N=#count{X: "+tmp2+"}.\n")
    f.write("count_ext_(" + tmp1 + ",N) :- " + "count_ext("+tmp1+",N), N!=0.\n")
    f.write("sum_test(N1) :- N1=#sum{N," + tmp1+" : count_ext("+tmp1+",N)}.\n")
    f.write("min(N1) :- N1=#min{N:count_ext_("+tmp1+",N)}.\n")
    f.close()
    print("col-specific-hide.lp generated.")


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

