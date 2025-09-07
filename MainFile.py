import os.path
import tkinter as tk
from logging import exception

from tkinter import PhotoImage, Entry, Frame, Label, Canvas, Button,Toplevel
from tkinter import ttk
from tkinter import END                                #Importing requirements
from PIL import Image,ImageTk
import csv

global month,week,amount,remain

def adddata():
    global m_en,w_en,a_en
    global window1
    window1 = Toplevel(home)
    window1.title("CashEase - Easy and Efficient")
    window1.geometry("800x400")                                        #Add data window
    window1.config(background="Black")
    window1.resizable(height=False, width=False)

    canvas2 = Canvas(window1, width=800, height=400)
    canvas2.pack(fill="both", expand=True)
    bg_img = Image.open("add_data.png")
    bg3 = ImageTk.PhotoImage(bg_img)
    canvas2.bg = bg3
    canvas2.create_image(0,0,image=bg3,anchor="nw")

    canvas2.create_text(400,50,text="PLEASE FILL OUT THE FOLLOWING",font=("Arial",14))
    m_en = Entry(window1,width=35,borderwidth=2)
    m_en.insert(0,"ENTER MONTH") #change to MONTH (Ex:August, May)
    w_en = Entry(window1,width=35,borderwidth=2)
    w_en.insert(0, "CHOOSE WEEK THROUGH 1-4") #change to WEEK (Ex:1,2,3,4)
    a_en = Entry(window1,width=35,borderwidth=2)
    a_en.insert(0, "ENTER BUDGET") #change to AMOUNT (Ex:1000,2500)

    m_en.place(x=300,y=80)
    w_en.place(x=300,y=130)
    a_en.place(x=300,y=180)

    Clear = Button(window1,text="CLEAR",command=clear,bg="#8dabba")
    Clear.config(width=10)
    Clear.place(x=370, y=230)
    submit = Button(window1,text="SUBMIT",command=data,bg="#8dabba")
    submit.config(width=10)
    submit.place(x=370,y=260)


def error(text,size):
    warning = Toplevel(home)
    warning.title("Ooops")
    warning.geometry("600x100")
    warning.config(background="white")
    warning.resizable(height=False, width=False)
    label = Label(warning, text=text, font=("Arial", size), bg="white",fg="black")                 #Error Screen
    label.place(x=120, y=20)

    ok = Button(warning, text="GOT IT", command=warning.destroy, bg="#8dabba")
    ok.config(width=10)
    ok.place(x=250, y=60)
    
def clear():
    global m_en, w_en, a_en
    m_en.delete(0,END)
    w_en.delete(0, END)         #Clearing entries
    a_en.delete(0, END)

def data():
    global data_dic
    from functions import save_data as SD
    from functions import clarification as CF

    try:
       week_check=int(w_en.get())
       month = m_en.get()
       try:
           if 1 <= week_check <= 4:
               week = week_check
               try:
                   amount = int(a_en.get())
                   window1.destroy()
                   v_code = f"{month}{week}"
                   check = CF(v_code)
                   if check == False:
                       data_dic = {
                               "month_d": f"{month}",
                               "week_d": f"{week}",                  #Retrieving data
                               "amount_d": f"{amount}"
                           }
                       SD(month, week, amount,v_code)
                       new_tab(month, week, amount)
                   else:
                       error("OOPS, THIS DATA ALREADY EXISTS",14)

               except ValueError:
                   error("OOPS, YOU MUST ENTER AN INTEGER!", 14)
           else:
               error("OOPS, PLEASE CHOOSE A WEEK THROUGH 1-4", 12)     #Error handling when retrieving data
       except ValueError:
           error("OOOPS, PLEASE FOLLOW THE GIVEN EXAMPLES!", 12)
    except ValueError:
       error("OOPS, PLEASE CHOOSE A WEEK THROUGH 1-4",12)


def new_tab(month,week,t_amount):
    from functions import remain_check as RC
    global new
    v_code = f"{month}{week}"
    name = f"{month}{week}".lower()
    month.upper()
    tab_name = f"{month} - {week}"
    new = Frame(notebook, width=1000,height=800,name=name)
    new.pack(expand=1)                                                    #Creating tab using retrieved data
    notebook.add(new,text=tab_name)
    canvas = Canvas(new, width=1000,height=800)
    canvas.pack()
    bg_image = Image.open("Tab_BG.png")
    bg_image = bg_image.resize((1000, 800))
    bg = ImageTk.PhotoImage(bg_image)
    canvas.bg = bg
    canvas.create_image(0,0,image=bg,anchor="nw")
    canvas.create_text(460, 80, text=f"CASHEASE - {month} {week}", font=("Bell Gothic Std Black", 38), fill="Black")

    amount = RC(v_code,t_amount)

    remain_txt = f"REMAINING BUDGET THIS WEEK : \t\tLKR.{amount}"
    canvas.create_text(450,220,text=f"TOTAL BUDGET THIS WEEK : \t\tLKR.{t_amount}",font=("Bell Gothic Std Black", 16), fill="Black")      #Displaying data
    remain_id = canvas.create_text(450, 280, text=remain_txt, font=("Bell Gothic Std Black", 16),fill="Black")

    if "remain_ids" not in globals():
        global remain_ids
        remain_ids = {}                                 #Updating remain
    remain_ids[v_code] = (canvas, remain_id)

    button = Button(canvas,text="ADD EXPENSE",font=("Arial",14),fg="white",bg="#688d94",command=lambda:add_expense(v_code,t_amount),height=1,width=14,borderwidth=2)
    button.place(x=400,y=450)

    del_button = Button(canvas,text="DELETE DATA",font=("Arial",14),fg="white",bg="#688d94",command=lambda :warning_s(v_code,name),height=1,width=14,borderwidth=2)
    del_button.place(x=400,y=500)

    report_button = Button(canvas,text="VIEW REPORT",font=("Arial",14),fg="white",bg="#688d94",command=lambda :display_records(v_code),height=1,width=14,borderwidth=2)
    report_button.place(x=400,y=550)

def add_expense(tab_name,total):
    global ex_en,am_en,expense_window
    expense_window = Toplevel(home)
    expense_window.title("CashEase - Easy and Efficient")
    expense_window.geometry("800x400")
    expense_window.config(background="Black")
    expense_window.resizable(height=False, width=False)

    canvas = Canvas(expense_window, width=800, height=400)
    canvas.pack(fill="both", expand=True)                                   #Add expense window
    bg_img = Image.open("add_data.png")
    bg3 = ImageTk.PhotoImage(bg_img)
    canvas.bg = bg3
    canvas.create_image(0,0,image=bg3,anchor="nw")

    canvas.create_text(400,50,text="LET'S ADD YOUR EXPENSE",font=("Arial",15))

    ex_en = Entry(expense_window,width=35,borderwidth=2)
    ex_en.insert(0,"ENTER EXPENSE")
    am_en = Entry(expense_window,width=35,borderwidth=2)
    am_en.insert(0,"ENTER AMOUNT")

    ex_en.place(x=290,y=100)
    am_en.place(x=290,y=150)

    clear = Button(expense_window,text='CLEAR',command=clear_ex,bg="#8dabba",width=10)
    clear.place(x=360,y=250)
    submit = Button(expense_window,text='SUBMIT',command=lambda:expense_save(tab_name,total),bg="#8dabba",width=10)
    submit.place(x=360,y=280)

def clear_ex():
    ex_en.delete(0,END)             #Clearing entries
    am_en.delete(0, END)

def expense_save(tab_name_pull,total_pull):
    def dead_warning(text):
        e_warning = Toplevel(home)
        e_warning.title("Woah!")
        e_warning.geometry("600x100")
        e_warning.config(background="white")
        e_warning.resizable(height=False, width=False)
        label = Label(e_warning, text=text, font=("Arial", 14), bg="white", fg="black")       #Budget low warning
        label.place(x=100, y=20)

        continue_b = Button(e_warning, text="Continue", command=e_warning.destroy, bg="#8dabba")
        continue_b.config(width=10)
        continue_b.place(x=250, y=60)
    try:
        from functions import save_expense as SE
        from functions import remain as RE
        expense = ex_en.get()
        ex_amount = int(am_en.get())

        remain = RE(tab_name_pull,total_pull,ex_amount)

        expense_dic = {
            "expense":f"{expense}",
            "Amount":f"{ex_amount}",
            "Remain":f"{remain}"                    #retrieving expense data
        }
        expense_window.destroy()
        SE(expense_dic, tab_name_pull)
        if tab_name_pull in remain_ids:
            canvas_obj, text_id = remain_ids[tab_name_pull]
            new_text = f"REMAINING BUDGET\t:\t\tLKR.{remain}"            #Updating remain value

            canvas_obj.itemconfig(text_id, text=new_text)
            dead_line = int(total_pull)/4
            if remain < dead_line and remain> 0:
                canvas_obj.itemconfig(text_id, fill="red")
                dead_warning("WE ARE RUNNING OUT OF BUDGET!")
            elif remain ==0:
                canvas_obj.itemconfig(text_id, fill="red")
                dead_warning("WE RAN OUT OF THIS WEEKS BUDGET!")
            elif remain<0:
                canvas_obj.itemconfig(text_id, fill="red")
                dead_warning("WE ARE GOING OVER OUR BUDGET!")
            else:
                canvas_obj.itemconfig(text_id, fill="black")


    except ValueError:
        error("OOPS,PLEASE ENTER AN INTEGER!",14)           #Error handling when retrieving expenses

def warning_s(v_code,name):
    global d_warning
    d_warning = Toplevel(home)
    d_warning.title("Woah!")
    d_warning.geometry("600x100")         #WARNING BEFORE CLEARING DATA RECORDS
    d_warning.config(background="white")
    d_warning.resizable(height=False, width=False)
    label = Label(d_warning, text="DELETING DATA WILL PERMANENTLY ERASE YOUR RECORDS!", font=("Arial", 12), bg="white",fg="black")
    label.place(x=50, y=20)

    continue_b = Button(d_warning, text="Continue", command=lambda:del_record(v_code,name), bg="#8dabba")
    continue_b.config(width=10)
    continue_b.place(x=150, y=60)

    cancel_b = Button(d_warning, text="Cancel", command=d_warning.destroy, bg="#8dabba")
    cancel_b.config(width=10)
    cancel_b.place(x=350, y=60)

def del_record(vc,name_pull):
    from functions import del_expense as DE
    keep_rows=[]
    d_warning.destroy()

    try:
        widget = notebook.nametowidget(name_pull)
        index = notebook.index(widget)
        notebook.forget(index)                                 #Pulling tab name
    except exception:
        pass

    with open("user_data.csv", "r", newline="") as data:
        reader = csv.reader(data)
        for row in reader:
            if row[3] != vc:                        #Deleting the saved data
                keep_rows.append(row)
    with open("user_data.csv", "w", newline="") as data:
        writer = csv.writer(data)
        for data in keep_rows:
            writer.writerow(data)
    DE(vc)

def display_records(vc):
    from functions import DF_records as DR
    r_window = Toplevel(home)
    r_window.title("CashEase - Easy and Efficient")
    r_window.geometry("800x600")
    r_window.config(background="white")
    r_window.resizable(height=False, width=False)
                                                                       #Display records window
    canvas = Canvas(r_window, width=800, height=400)
    canvas.pack(fill="both", expand=True)
    bg_img = Image.open("report_BG.jpg")
    bg_img=bg_img.resize((800,600))
    bg3 = ImageTk.PhotoImage(bg_img)
    canvas.bg = bg3
    canvas.create_image(0,0,image=bg3,anchor="nw")

    if os.path.exists(f"{vc}.csv"):
        report = DR(vc)
        canvas.create_text(380,60, text="THIS WEEKS TRANSACTIONS", font=("Arial", 18))
        tree = ttk.Treeview(canvas)
        tree.place(x=95,y=120)
        tree["columns"] = list(report.columns)
        tree["show"] = "headings"

        for col in report.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")                                        #Creating data tree and displaying
        for _, row in report.iterrows():
            tree.insert("", "end", values=list(row))

        ok_b = Button(canvas,text="CONTINUE",command=r_window.destroy,bg="#688d94",fg="white")
        ok_b.config(width=10,height=2)
        ok_b.place(x=350,y=400)

    else:
        canvas.create_text(395, 230,text=f"YOUR TRANSACTIONS FOR {vc} WILL BE DISPLAYED HERE \n \t         ONCE EXPENSES ARE ADDED...",font=("Arial", 18))
        canvas.create_text(385, 320, text="THANK YOU!", font=("Arial", 18))
        ok_b = Button(canvas,text="CONTINUE",command=r_window.destroy,bg="#688d94",fg="white")          #If expenses does not exist
        ok_b.config(width=10,height=2)
        ok_b.place(x=340,y=400)


def Home():
    global notebook
    global home
    home = tk.Tk()
    logo = PhotoImage(file="logo_pic.png")
    home.iconphoto(True, logo)
    home.title("CashEase - Easy and Efficient")
    home.geometry("1000x800")                               #Main screen/welcome screen
    home.config(background="Black")
    home.resizable(height=False,width=False)
    notebook = ttk.Notebook(home)
    notebook.pack()

    global main_screen
    main_screen = Frame(notebook, width=1000,height=800,bg="white")
    add_new = Frame(notebook, width=1000,height=800,bg="white")
    main_screen.pack(expand=1)
    add_new.pack(expand=1)

    bg1 = PhotoImage(file="bgimage.png")
    canvas = Canvas(main_screen, width=1000,height=800)
    canvas.pack()
    canvas.create_image(0,0,image=bg1,anchor="nw")
    canvas.create_text(490,120,text="WELCOME TO CashEase!",font=("Arial",48),fill="#87edd4")
    canvas.create_text(500,250,text="\t\t\t\tHey there, glad you’re here.\n\t   Cash Ease is built to help you take control of your weekly spending without the hassle. \nSet your budget, track your expenses, and stay one step ahead of your limits.When your budget’s close to running out,\n\t\tI’ll let you know. No stress, no guesswork - just clear, simple money tracking.\n\t\t\tLet’s get started by setting up your weekly budget.\n\n\t\t\t   Use the tabs above to handle with CashEase",font=("Helvetica",13))

    bg2 = PhotoImage(file=r"add_scree.png")
    canvas = Canvas(add_new, width=1000, height=800)
    canvas.pack()
    canvas.create_image(0, 0, image=bg2, anchor="nw")
    canvas.create_text(500,90,text="LET'S START MANAGING!",font=("Arial",48),fill="#7abbd6")
    add_button = Button(add_new, text="ADD-NEW",font=("Arial",12),fg="black",bg="#ade0b2",command=adddata)
    add_button_canvas = canvas.create_window(450,250,anchor="nw",window=add_button,width=100,height=50)

    notebook.add(main_screen,text="WELCOME")
    notebook.add(add_new, text="ADD NEW")
    try:
        with open("user_data.csv","r") as reading_data:
            data_file = csv.reader(reading_data)
            for data in data_file:                          #Creating tabs with saved data
                new_tab(data[0],data[1],data[2])
    except IndexError:
        pass
    tk.mainloop()

Home()



