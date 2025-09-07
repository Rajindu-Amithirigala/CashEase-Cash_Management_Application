import pandas as pd
import csv
import os                #Importing requirements

def save_expense(ex_dic,tb_name):
        ex_file = f"{tb_name}.csv"

        if os.path.exists(ex_file):
            df = pd.read_csv(ex_file)
            df = pd.concat([df, pd.DataFrame([ex_dic])], ignore_index=True)  #Saving expenses to pandas dataframe function
        else:
            df = pd.DataFrame([ex_dic])

        df.to_csv(ex_file, index=False)

def DF_records(v_code):
    DF = pd.read_csv(f"{v_code}.csv")         #Returnig a specific dataframe
    return DF

def del_expense(file_n):
    file = f"{file_n}.csv"
    if os.path.exists(file):         #Deleting csv data function
        os.remove(file)
    else:
        pass

def remain(name,total,ex_am):
    ex_file = f"{name}.csv"

    if os.path.exists(ex_file):
        df = pd.read_csv(ex_file)

        if not df.empty and "Remain" in df.columns:
            last_remain = int(df.iloc[-1]["Remain"])
        else:                                                       #Counting remain value function
            last_remain = int(total)
    else:
        last_remain = int(total)
    remain = last_remain - ex_am
    return remain

def remain_check(vc,amnt):
    expense_file = f"{vc}.csv"
    if os.path.exists(expense_file):
        df = pd.read_csv(expense_file)
        if not df.empty and "Remain" in df.columns:
            remain = int(df.iloc[-1]["Remain"])              #Counting display remain value function
            return remain
        else:
            remain = int(amnt)
            return remain
    else:
        remain = int(amnt)
        return remain

def save_data(s_month,s_week,s_amount,s_v):
    with open("user_data.csv", "a",newline="") as data_file:
       writer =  csv.writer(data_file)                                 #Saving user data to CSV function
       writer.writerow([s_month,s_week,s_amount,s_v],)

def clarification(vc):
    exist = False
    with open("user_data.csv", "r", newline="") as data_file:
        reader = csv.reader(data_file)                                             #CSV existence clarification function
        data = list(reader)

        if len(data) == 0:
            return exist

        for i in data:
            if len(i) < 4:
                continue

            if i[3].strip() == vc:
                exist = True
                return exist
        return exist



