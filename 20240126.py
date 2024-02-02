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
    frec.write("Date            Credit      Debit       Balance\n")
    frec.write(str(strftime("[%Y - %m - %d] [%H:%M:%S]",gmtime()))+"    "+oc+"      "+oc+"\n")
    frec.close()

    messagebox.showinfo("Details", "Your Account number is:"+str(accnt_no))
    master.destroy()
    return

def crdt_write(master, amt, accnt, name):
    if(is_number(amt) == 0):
        messagebox.showinfo("Error", "Invaild Number\nTry Again")
        master.destroy()
        return
    
    fdet = open(accnt+".txt", "r")
    pin = fdet.readline()
    camt = int(fdet.readline())
    fdet.close()
    amti = int(amt)
    cb = amti + camt
    fdet = open(accnt+".txt","w")
    fdet.write(pin)
    fdet.write(str(cb)+"\n")
    fdet.write(accnt+"\n")
    fdet.write(name+"\n")
    fdet.close()
    frec = open(str(accnt) + "-rec.txt", "w")
    frec.write(str(strftime("[%Y - %m - %d] [%H:%M:%S]",gmtime()))+"    "+str(amti)+"      "+str(cb)+"\n")
    frec.close()
    messagebox.showinfo("Succesful!!", "Amount Credited!")
    master.destroy()
    return

def Create():
    crwn = tk.Tk()
    crwn.geometry("600x300")
    crwn.title("Create Account")
    crwn.config(background='LightBlue')
    frl = tk.Frame(crwn,bg="LightBlue")
    l_title=tk.Message(text="Bank Management System", relief="raised", width=2000, padx=600, pady=0, fg="white", bg="blue", justify="center", anchor="center")
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

def Main_Menu():
    rootwn = tk.Tk()
    rootwn.geometry("1600x500")
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
    b2 = tk.Button(image=imglog)
    b6 = tk.Button(image=imgq, command=rootwn.destroy)

    b1.place(x=800,y=300)
    b2.place(x=800,y=200)
    b6.place(x=800,y=400)

    rootwn.mainloop()

Main_Menu()