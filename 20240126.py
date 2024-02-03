import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime

def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0
    
def check_acc_nmb(num):
    try:
        fpin = open(num+".txt", "r")
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invaild Number\nTry Again")
        return 0
    fpin.close()
    return

def home_return(master):
    master.destroy()
    Main_Menu()

def write(master,name,oc,pin):
    if((is_number(name)) or (is_number(pin) == 0) or name==""):
        messagebox.showinfo("Error", "Invaild Number\nTry Again")
        master.destroy()
        return

    f1 = open("Accnt_Record.txt", "r")
    accnt_no = int(f1.readline())
    accnt_no += 1
    f1.close

    f1 = open("Accnt_Record.txt", "w")
    f1.write(str(accnt_no))
    f1.close

    fdet = open(str(accnt_no)+".txt", "w")
    fdet.write(pin+"\n")
    fdet.write(oc+"\n")
    fdet.write(str(accnt_no)+"\n")
    fdet.write(name+"\n")
    fdet.close()

    frec = open(str(accnt_no) + "-rec.txt", "w")
    frec.write("Date                            Credit      Debit       Balance\n")
    frec.write(str(strftime("[%Y - %m - %d] [%H:%M:%S]",gmtime()))+"     "+oc+"                     "+oc+"\n")
    frec.close()

    messagebox.showinfo("Details", "Your Account number is:"+str(accnt_no))
    master.destroy()
    return

def Create():
    crwn = tk.Tk()
    crwn.geometry("600x300")
    crwn.title("Create Account")
    crwn.config(background='LightBlue')
    frl = tk.Frame(crwn,bg="LightBlue")
    l_title=tk.Message(crwn,text="Bank Management System", relief="raised", width=2000, padx=600, pady=0, fg="white", bg="blue", justify="center", anchor="center")
    l_title.config(font=("Comic Sans MS", 40, "bold"))
    l_title.pack(side="top")
    l1=tk.Label(crwn,text="Enter Name:", font=("Times",16), relief="raised")
    l1.pack(side="top")
    el=tk.Entry(crwn)
    el.pack(side="top")
    l2=tk.Label(crwn,text="Enter Opening Credit:", font=("Times",16), relief="raised")
    l2.pack(side="top")
    e2=tk.Entry(crwn)
    e2.pack(side="top")
    l3=tk.Label(crwn,text="Enter Your Pin:", font=("Times",16), relief="raised")
    l3.pack(side="top")
    e3=tk.Entry(crwn)
    e3.pack(side="top")
    b = tk.Button(crwn,text="Submit",font=("Times",16), command=lambda: write(crwn, el.get().strip(), e2.get().strip(),e3.get().strip()))
    b.pack(side="top")
    return

def login(master):
    master.destroy()
    loginwn = tk.Tk()
    loginwn.geometry("600x300")
    loginwn.title("Log in")
    loginwn.config(bg="LightBlue")
    frl = tk.Frame(loginwn, bg="blue")
    l_title=tk.Message(loginwn,text="Bank Management System", relief="raised", width=2000, padx=600, pady=0, fg="white", bg="blue", justify="center", anchor="center")
    l_title.config(font=("Comic Sans MS", 40, "bold"))
    l_title.pack(side="top")
    l1=tk.Label(loginwn,text="Enter Name:", font=("Times",16), relief="raised")
    l1.pack(side="top")
    el=tk.Entry(loginwn)
    el.pack(side="top")
    l2=tk.Label(loginwn,text="Enter account number:", font=("Times",16), relief="raised")
    l2.pack(side="top")
    e2=tk.Entry(loginwn)
    e2.pack(side="top")
    l3=tk.Label(loginwn,text="Enter Your Pin:", font=("Times",16), relief="raised")
    l3.pack(side="top")
    e3=tk.Entry(loginwn)
    e3.pack(side="top")
    b = tk.Button(loginwn,text="Submit",font=("Times",16), command=lambda: check_login(loginwn, el.get().strip(), e2.get().strip(),e3.get().strip()))
    b.pack(side="top")
    b1=tk.Button(text="HOME", font=("Times",16),bg="blue",fg="white",
                 command = lambda: home_return(loginwn))
    b1.pack(side="top")

def check_login(master,name,acc_num,pin):
    if(check_acc_nmb(acc_num)==0):
        master.destroy()
        Main_Menu()
        return
    if((is_number(name)) or(is_number(pin)==0)):
        messagebox.showinfo("Error", "Invalid Input")
        master.destroy()
        Main_Menu()
    else:
        master.destroy()
        messagebox.showinfo("Success", "You Have Logged in!")
        logged_in_menu(acc_num,name)

def logged_in_menu(accnt, name):
    rootwn=tk.Tk()
    rootwn.geometry("1200x500")
    rootwn.title("Welcome - " + name)
    rootwn.config(bg="Lightblue")
    frl = tk.Frame(rootwn)
    frl.pack(side="top")
    l_title = tk.Message(rootwn,text="Bank Management System", relief="raised", width=2000, padx=600, pady=0, fg="white", bg="blue", justify="center", anchor="center")
    l_title.config(font=("Comic Sans MS", 40, "bold"))
    l_title.pack(side="top")
    label = tk.Label(text="Logged in as: "+name, bg="blue",fg="white",
                     font=("Times",16),anchor="center",justify="center")
    label.pack(side='top')
    img2 = tk.PhotoImage(file="credit.gif")
    img3 = tk.PhotoImage(file="debit.gif")
    img4 = tk.PhotoImage(file="balance1.gif")
    img5 = tk.PhotoImage(file="transaction.gif")
    img6 = tk.PhotoImage(file="logout.gif")
    myimg2=img2.subsample(2,2)
    myimg3=img3.subsample(2,2)
    myimg4=img4.subsample(2,2)
    myimg5=img5.subsample(2,2)
    myimg6=img6.subsample(2,2)
    b2=tk.Button(image=myimg2)
    b3=tk.Button(image=myimg3)
    b4=tk.Button(image=myimg4, command = lambda: disp_bal(accnt))
    b5=tk.Button(image=myimg5)
    b6=tk.Button(image=myimg6, command= lambda: logout(rootwn))
    b2.image = myimg2
    b3.image = myimg3
    b4.image = myimg4
    b5.image = myimg5
    b6.image = myimg6

    b2.place(x=100,y=150)
    b3.place(x=100,y=220)
    b4.place(x=900,y=150)
    b5.place(x=900,y=220)
    b6.place(x=500,y=400)

def logout(master):
    messagebox.showinfo("Logged Out","You have been successfully Logged out!")
    master.destroy()
    Main_Menu()

def disp_bal(accnt):
    fdet = open(accnt+".txt","r")
    fdet.readline()
    bal = fdet.readline()
    fdet.close()
    messagebox.showinfo("Balance", bal)


def Main_Menu():
    rootwn = tk.Tk()
    rootwn.geometry("1200x500")
    rootwn.title("Bank Management System")
    rootwn.config(background='LightBlue')
    frl = tk.Frame(rootwn)
    frl.pack(side="top")
    l_title = tk.Message(text="Bank Management System", relief="raised", width=2000, padx=600, pady=0, fg="white", bg="blue", justify="center", anchor="center")
    l_title.config(font=("Comic Sans MS", 40, "bold"))
    l_title.pack(side="top")
    imgcl=tk.PhotoImage(file="new.gif")
    imglo=tk.PhotoImage(file="login.gif")
    imgquit = tk.PhotoImage(file="quit.gif")
    imgc = imgcl.subsample(2,2)
    imglog = imglo.subsample(2,2)
    imgq = imgquit.subsample(2,2)
    

    b1 = tk.Button(image=imgc, command=Create)
    b2 = tk.Button(image=imglog, command = lambda: login(rootwn))
    b6 = tk.Button(image=imgq, command=rootwn.destroy)

    b1.place(x=800,y=300)
    b2.place(x=800,y=200)
    b6.place(x=800,y=400)

    rootwn.mainloop()

Main_Menu()
