from tkinter import *
import sqlite3
from tkinter import ttk
import tkinter.messagebox
from datetime import *
import datetime
from tkinter.ttk import Combobox
##from tkinter import filedialog
from tkinter import Canvas, Frame, BOTH

##from tkcalendar import Calendar, DateEntry
##from PIL import ImageTk, Image
##import os

root = Tk()
root.title("LogIn")
root.geometry("400x250+600+350")
##img = ImageTk.PhotoImage(Image.open("logo1.png"))
##width=400
##height=220
##screen_width=root.winfo_screenwidth()
##screen_height=root.winfo_screenheight()
##x=(screen_width/2)-(width/2)
##y=(screen_width/2)-(height/2)
##root.geometry("%dx%d+%d+%d"%(width,height,x,y))
root.resizable(0, 0)
root.configure(background="whitesmoke")


def fillnot():
    tkinter.messagebox.showerror("LogIn Invalid", "Please Fill The Require Fields...!!!")


def exits():
    tkinter.messagebox.showerror("LogIn Invalid", "Your ID And Password Does Not Exist")


def logmsg():
    if tkinter.messagebox.askyesno("LogOut", "Are You Sure You Want to LogOut"):
        Design.destroy()
        root.deiconify()


def time():
    datetime.datetime.now()


def DataBase():
    global conn, cursor
    conn = sqlite3.connect("Libdata.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `Administrator` WHERE Username='ADMIN' AND Password='ADMIN'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `Administrator`('Username','Password')VALUES('ADMIN','ADMIN')")
        conn.commit()


# ---login variables----------
USERNAME = StringVar()
PASSWORD = StringVar()
# -----SEARCH VERIABLE-----
searchbox = StringVar()
combosearch = StringVar()
# ---------------LogIn Function---------------------
dlist = StringVar()


def login(event=None):
    global USERNAME
    DataBase()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        tkinter.messagebox.showerror("LogIn", "Please Enter The Require Fields")
    else:
        cursor.execute("SELECT * FROM `Administrator` WHERE Username=? AND Password=?",
                       (USERNAME.get(), PASSWORD.get()))
        result = cursor.fetchone()
        if result is not None:
            print("Sucessfully LogIn")
            Searchdesign()
            USERNAME.set("")
            PASSWORD.set("")
        else:
            tkinter.messagebox.showerror("LogIn", "Your ID & Passowrd Does Not Exists...")
            USERNAME.set("")
            PASSWORD.set("")

        cursor.close()
        conn.close()


# -----------------Login Form-------------------
# CREATE FRAME------
topframe = Frame(root, background="#000080", height=30)
topframe.pack(side=TOP, fill=X)
form = Frame(root, background="whitesmoke")
form.pack(pady=30)
# LABELs---TextBox---Button----
heading = Label(topframe, text="Entrance", font=('Times 32', 15, "bold"), fg="white", bg="#000080")
heading.pack(fill=X)
l1 = Label(form, text="Username", font=('Times 32', 10), fg="black", bg="whitesmoke", anchor="e")
l1.grid(column=0, row=0, pady=5)
l2 = Label(form, text="Password", font=('Times 32', 10), fg="black", bg="whitesmoke", anchor="e")
l2.grid(column=0, row=1, pady=5)
username = Entry(form, width=30, textvariable=USERNAME).grid(row=0, column=1, pady=5)
passowrd = Entry(form, width=30, textvariable=PASSWORD, show="*").grid(column=1, row=1, pady=5)

btn1 = Button(form, text="LogIn", width=12, command=login)
btn1.grid(pady=10, row=3, columnspan=3, sticky="n")
btn1.bind('<Return>', login)
l3 = Label(root, background="#000080").pack(side=BOTTOM, fill=X)
# -----------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
from matplotlib import pyplot as plt
##from matplotlib.backends
import numpy as np

excel_file = 'college.xlsx'
data = pd.read_excel(excel_file, index_col=0)


def Jobers():
    len_placement = len(data['Placed By:'])
    AUR_Count = 0;
    self_Count = 0;
    for i in range(len_placement):
        if (data['Placed By:'][i] == 'AUR'):
            AUR_Count += 1
        else:
            self_Count += 1
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    langs = ['AUR', 'Self']
    students = [AUR_Count, self_Count]
    ax.pie(students, labels=langs, autopct='%1.2f%%')
    plt.show()


def LOCATION():
    len_ADDRESS = len(data['Permanent Address'])
    Inside_Count = 0;
    Outside_Count = 0;
    for i in range(len_ADDRESS):
        if (data['Permanent Address'][i] == 'Rajasthan'):
            Inside_Count += 1
        else:
            Outside_Count += 1
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    langs = ['Belong to Rajasthan', 'Belongs to Other City']
    students = [Inside_Count, Outside_Count]
    ax.pie(students, labels=langs, autopct='%1.2f%%')
    plt.show()


def SALARY():
    len_SALARY = len(data['Permanent Address'])
    selery_Count1 = 0;
    selery_Count2 = 0;
    selery_Count3 = 0;
    selery_Count4 = 0;
    for i in range(len_SALARY):
        if (data['Salary (per annum)'][i] < 1000000 and data['Salary (per annum)'][i] > 800000):
            selery_Count1 += 1
        elif (data['Salary (per annum)'][i] < 800000 and data['Salary (per annum)'][i] > 600000):
            selery_Count2 += 1
        elif (data['Salary (per annum)'][i] < 600000 and data['Salary (per annum)'][i] > 400000):
            selery_Count3 += 1
        elif (data['Salary (per annum)'][i] < 400000 and data['Salary (per annum)'][i] > 100000):
            selery_Count4 += 1
    print(selery_Count1)
    fig = plt.figure(figsize=(5, 5), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    langs = ['Salary B/W 1 Million and 8 Lacks', 'Salary B/W 8 Lacks and 6 Lacks', 'Salary B/W 6 Lacks and 4 Lacks',
             'Salary B/W 4 Lacks and 4 Lacks']
    students = [selery_Count1, selery_Count2, selery_Count3, selery_Count4]
    ax.pie(students, labels=langs, autopct='%1.2f%%')
    plt.show()


##    print(AUR_Count,self_Count)
# ...........................................All Form Design.................................
# this is design function that calls every window. it is the basic design..that implement on every window
def Designs():
    global Design
    root.withdraw()
    Design = Toplevel()
    Design.geometry(
        "{0}x{0}".format(Design.winfo_screenwidth(), Design.winfo_screenheight()))  # it open the full window

    # -----Frames--
    topframe1 = Frame(Design, background="#003366", height=10, bd=1, relief=GROOVE)
    topframe1.pack(fill=X)

    topframe = Frame(Design, background="#004C99", height=10, bd=1, relief=GROOVE)
    topframe.pack(fill=X, side=TOP)
    form = Frame(Design, background="whitesmoke")
    form.pack(pady=30)
    # LABELs---TextBox---Button----
    h1 = Label(topframe1, text="GOLDSync", font=('Times 10', 15, "bold"), fg="white", bg="#003366")
    h1.grid(row=0, column=1)

    h1 = Label(topframe1, text=datetime.date.today(), font=('Times 10', 10, "bold"), fg="white", bg="#003366", height=3)
    h1.grid(row=0, column=2, padx=1300)

    heading = Label(topframe, text="", font=('Times 32', 15, "bold"), fg="white", bg="#004C99")
    heading.grid(row=0, column=1)
    Button(topframe, text="LogOut", width=220, command=logmsg).grid(row=0, column=9)
    Label(Design, text="Copyright © 2018 by !3Tech", font=('Times 32', 10, "bold"), fg="WHITE", bg="#003CB3").pack(
        fill=X, side=BOTTOM)


# ..............................................Serch Function..................................................
# this is the search button function when you click on this search button then this function runs
def Searchfun():
    DataBase()
    v1 = combosearch.get()
    print(v1)

    if v1 == "":
        tkinter.messagebox.showerror("Search", "Please fill the require feilds")
    elif v1 == "Preferd or Non Prefered Job":
        Jobers()
    elif v1 == "Insider or Outsider":
        LOCATION()
    elif v1 == "Acc to Salary":
        SALARY();
    cursor.close()
    conn.close()


# -----------------------------------------------Celender function--------------------------------

##def calander():
##    cal = DateEntry(top, width=12, background='darkblue',
##                    foreground='white', borderwidth=2, year=2010)
##    cal.pack(padx=10, pady=10)
# ..............................................Search Form design.................................

def Searchdesign():
    Designs()
    Design.title("Search")
    global searchbox
    searchvalues = ["Preferd or Non Prefered Job", "Acc to Salary", "Acc. to Department", "Insider or Outsider"]
    searchframe = Frame(Design, bg="whitesmoke")
    searchframe.pack(pady=10)
    combo1 = Combobox(searchframe, values=searchvalues, width=50, textvariable=combosearch, state='readonly')
    combo1.grid(row=0, column=0, pady=5, padx=5)
    combo1.set("Select")
    ##    SEARCH=Entry(searchframe,width=50,textvariable=searchbox)
    ##    SEARCH.grid(row=0,column=1,pady=5,padx=5)
    Button(searchframe, text="Search", width=20, command=Searchfun).grid(row=0, column=2, padx=5)
