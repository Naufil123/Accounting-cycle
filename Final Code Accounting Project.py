import sys
from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter.simpledialog import askstring, askinteger
import sqlite3
con=sqlite3.connect('Journal Entries.db')
c=con.cursor()

class Accounting:
    pass
    #def __init__(self):
        
class JournalEntry:
    def __init__(self):
        self.con=sqlite3.connect('Journal Entries.db')
        self.c=self.con.cursor()
        self.Date = None
        self.AccountsCode = None
        self.AccountsExplanation = None
        self.Debit = None
        self.Credit = None
        self.Type = None
        self.a = 0
        self.b =0
        self.AC = {"Assets": {"Cash": "A01", "Equipment": "A02", "Accounts Reciveable": "A03","Prepaid Insurance":"A04","Prepaid Rent":"A05"},
                   "Laibilities" :{"Accounts payable": "L01","Salaries Payable":"L02","Rent Payable":"L03","Unearned Revenue":"L04"},
                   "Revenue":{"sales Revenue":"R01","Rent Revenue": "R02","Interest Revenue ": "R03"},
                   "Expense":{"Salaries Expense":"E01","Rent Expense":"E02","Utility Expense":"E03"},
                   "Owners Equity" :{"Owners capital": "O01", "Owners Drawing":"O02"}}
    def Account_Chart(self):
        print("\t\t\t *****ACCOUNT TITLES*****")
        for k1, v1 in self.AC.items():
            print(k1)
            if type(v1)==dict:
                for k2,v2 in v1.items():
                    print("{0},{1}".format(k2,v2))
                print('\n')            
    def Account_Title(self, code):
        for k1, v1 in self.AC.items():
            if type(v1) == dict:
                for k2, v2 in v1.items():
                    if code == v2:
                        return("{0}".format(k2))
        
    def MainScreen(self):
        screen= Tk()
        #canvas=Canvas(width=400,height=250,bg='blue')
        #canvas.pack()
        #photo=PhotoImage(file='
        screen.geometry("500x500")
        screen.title("Main Menu",)
        
        heading= Label(screen,text="MAIN MENU",bg="black",fg="white",width="300",height="3",font=("Lucida Console",12,'bold'))
        heading.pack()
        heading1= Label(screen,text="Accounting Cycle",bg="black",fg="white",width="300",height="3",font=("Lucida Console",12,'bold'))
        heading1.pack()
        def leftClick(event):
            screen.destroy()
            self.Insert_data()
        #heading= Label(screen,text="Enter Entry",bg="black",fg="white",width="300",height="3",font=("Lucida Console",12))
        #heading.pack()
        Entry_button=Button(screen,text="Enter Entry", width="100", height="3",font=("Lucida Console",12))
        Entry_button.pack()
        Entry_button.bind('<Button-1>',leftClick)
        def RighClick(event):
            screen.destroy()
        quit_button= Button(screen,font=('arial',8,'bold'),text="QUIT",bg="black",fg="white", width="20", height="3")
        quit_button.place(x=330,y=400)
        quit_button.bind('<Button-1>', RighClick)
        
        

        
    def create_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS journal_entries(DATE integer, AccountsExplanationDebit Text,AccountsExplanationCredit Text, Debit integer,Credit integer)')
        #c.execute('CREATE TABLE Trial_Balance(AccountsExplanation Text, Debit integer,Credit integer)')
        #c.execute('CREATE TABLE Cash(DATE integer, AccountsExplanation Text, Debit integer,Credit integer)')
        #self.comp_name =input("Enter the Company name: ")
        self.c.close()
        self.con.close()

    def InsertJ(self):
        
        a = input("want to enter a entry: ")
        if a == "yes":
            self.Insert_data()
        else:
            print("Thank you")
    def Insert_data(self):
        def save(Date,AccountsExplanation,Type,Debit,Credit):
            self.Date_info=self.DATE.get()
            self.AccountsDebit_info=self.AccountsExplanationDebit.get()
            self.AccountsExplanationDebit = self.Account_Title(self.AC)
            self.AccountsCredit_info=self.AccountsExplanationCredit.get()
            self.AccountsExplanationCredit = self.Account_Title(self.AC)
            self.Type_info=self.Type.get()
            self.Debit_info=self.Debit.get()
            #d=int(Debit_info)
            self.Credit_info=self.Credit.get()
            #k=int(Credit_info)
        screen2 = Tk()
        screen2.geometry("500x500")
        screen2.title("Journal Entries")
        heading= Label(screen2,text="Enter Entries",bg="black",fg="white",width="500",height="3",font=("Lucida Console",12))
        heading.pack()
        Date = Label(screen2,text="Enter Date")
        AccountsExplanationDebit = Label(screen2,text="Enter Debit Account")
        AccountsExplanationCredit = Label(screen2,text="Enter Credit Account")
        #Type = Label(screen2,text="Enter Account Type")
        Date.place(x=100, y=70)
        AccountsExplanationDebit.place(x=100, y=150)
        AccountsExplanationCredit.place(x=100, y=280)
        #Type.place(x=100, y=220)
        self.Type= StringVar()
        self.AccointsExplanationDebit = StringVar()
        self.AccointsExplanationCredit = StringVar()
        self.DATE =  StringVar()
        self.DATE = Entry(screen2,textvariable =Date, width="30")
        #self.Date=Entry(screen2)
        self.AccountsExplanationDebit = Entry(screen2,textvariable =AccountsExplanationDebit, width="30")
        Debit=Label(screen2,text="Enter Debit Amount")
        Debit.place(x=100, y=220)
        self.Debit= Entry(screen2,textvariable =Debit, width="30")
        self.Debit.place(x=100, y=240)
        #self.Type= Entry(screen2,textvariable =Type, width="30")
        self.DATE.place(x=100, y=100)
        self.AccountsExplanationDebit.place(x=100, y=180)
       
        self.AccountsExplanationCredit = Entry(screen2,textvariable =AccountsExplanationCredit, width="30")
        self.AccountsExplanationCredit.place(x=100, y=300)
        Credit=Label(screen2,text="Enter Credit Amount")
        Credit.place(x=100, y=340)
        self.Credit= Entry(screen2,textvariable =Credit, width="30")
        self.Credit.place(x=100, y=360)
        #self.Debit=0
        #c.execute("INSERT INTO journal_entries(DATE ,AccountsExplanation,Debit,Credit)VALUES(?,?,?,?)",(self.DATE,self.AccountsExplanation,self.Debit,self.Credit))
        #con.commit()
        def Click(event):
            save(Date,AccountsExplanationDebit,AccountsExplanationCredit,Debit,Credit)
            con=sqlite3.connect('Journal Entries.db')
            c=con.cursor()
            cur = con.cursor()
            ###################################3
            c.execute("INSERT INTO journal_entries(DATE ,AccountsExplanationDebit,AccountsExplanationCredit,Debit,Credit)VALUES(?,?,?,?,?)",(self.Date_info,self.AccountsDebit_info,self.AccountsCredit_info,int(self.Debit_info),int(self.Credit_info)))
#############################################################
            con.commit()
            
            #c.close()
            #con.close()
            screen2.destroy()
            self.Screen3()
            
            
            
            
        Okay = Button(screen2, text="Okay", width="18", height="4",fg='black',font=("Lucida Console",8,'bold'))
        Okay.bind('<Button-1>', Click)
        Okay.place(x=335, y=430)
        
    def Screen3(self):
        screen3= Tk()
        screen3.geometry("300x200")
        screen3.title("Enter More Entries")
        heading= Label(screen3,text="Enter More Entries",bg="black",fg="white",width="300",height="3",font=("Lucida Console",12,'bold'))
        heading.pack()
        def S3Click(event):
            screen3.destroy()
            self.Insert_data()
        Yes_button=Button(screen3, text="Yes", width="100", height="3",fg='black',font=("Lucida Console",12,'bold'))
        Yes_button.pack()
        Yes_button.bind('<Button-1>',S3Click)
        def S4Click(event):
            screen3.destroy()
            con=sqlite3.connect('Journal Entries.db')
            c=con.cursor()
            cur = con.cursor()
            cur.execute("SELECT * FROM journal_entries")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            self.Taccounts()
            self.Print_Trial_Balance(con)
            self.Screen4()
        No_button=Button(screen3, text="No", width="100", height="3",fg='black',font=("Lucida Console",12,'bold'))
        No_button.pack()
        No_button.bind('<Button-1>',S4Click)
       #No_button=Button(screen3, text="No", width="100", height="3",font=("Lucida Console",12))
        #No_button.pack()
        #No_button.bind('<Button-1>',S4Code)
    def Screen4(self):
        screen4= Tk()
        screen4.geometry("350x250")
        screen4.title("Enter Adjusted Entries")
        heading= Label(screen4,text="Want To Enter Adjusted Entries",bg="black",fg="white",width="300",height="3",font=("Lucida Console",12,'bold'))
        heading.pack()
        def YS4Click(event):
            screen4.destroy()
            self.Insert_Adjusted_Data()
        Yes_button=Button(screen4, text="Yes", width="100", height="3",fg='black',font=("Lucida Console",12,'bold'))
        Yes_button.pack()
        Yes_button.bind('<Button-1>',YS4Click)
        def NS4Click(event):
            screen4.destroy()
        No_button=Button(screen4, text="No", width="100", height="3",fg='black',font=("Lucida Console",12,'bold'))
        No_button.pack()
        No_button.bind('<Button-1>',NS4Click)
        def BackScreen3(event):
            self.Insert_data()
            screen4.destroy()
        Back_button=Button(screen4, text="Back",fg='black')
        Back_button.pack()
        Back_button.bind('<Button-1>',BackScreen3)
        Back_button.place(x=10,y=180)
        #screen4.mainloop()
    def Insert_Adjusted_Data(self):
        screen5 = Tk()
        screen5.geometry("500x500")
        screen5.title("Journal Entries")
        heading= Label(screen5,text="Enter Adjusted Entries",bg="black",fg="white",width="500",height="3",font=("Lucida Console",12,'bold'))
        heading.pack()
        Date = Label(screen5,text="Enter Date")
        AccountsExplanationDebit = Label(screen5,text="Enter Debit Account")
        AccountsExplanationCredit = Label(screen5,text="Enter Credit Account")
        #Type = Label(screen2,text="Enter Account Type")
        Date.place(x=100, y=70)
        AccountsExplanationDebit.place(x=100, y=150)
        AccountsExplanationCredit.place(x=100, y=280)
        #Type.place(x=100, y=220)
        self.Type= StringVar()
        self.AccointsExplanationDebit = StringVar()
        self.AccointsExplanationCredit = StringVar()
        self.DATE =  StringVar()
        self.DATE = Entry(screen5,textvariable =Date, width="30")
        #self.Date=Entry(screen2)
        self.AccountsExplanationDebit = Entry(screen5,textvariable =AccountsExplanationDebit, width="30")
        Debit=Label(screen5,text="Enter Debit Amount")
        Debit.place(x=100, y=220)
        self.Debit= Entry(screen5,textvariable =Debit, width="30")
        self.Debit.place(x=100, y=240)
        #self.Type= Entry(screen2,textvariable =Type, width="30")
        self.DATE.place(x=100, y=100)
        self.AccountsExplanationDebit.place(x=100, y=180)
       
        self.AccountsExplanationCredit = Entry(screen5,textvariable =AccountsExplanationCredit, width="30")
        self.AccountsExplanationCredit.place(x=100, y=300)
        Credit=Label(screen5,text="Enter Credit Amount")
        Credit.place(x=100, y=340)
        self.Credit= Entry(screen5,textvariable =Credit, width="30")
        self.Credit.place(x=100, y=360)
        def S5Click(event):
            #save(Date,AccountsExplanationDebit,AccountsExplanationCredit,Debit,Credit)
            con=sqlite3.connect('Journal Entries.db')
            c=con.cursor()
###################################################################33
            c.execute("INSERT INTO journal_entries(DATE ,AccountsExplanationDebit,AccountsExplanationCredit,Debit,Credit)VALUES(?,?,?,?,?)",(self.Date_info,self.AccountsDebit_info,self.AccountsCredit_info,int(self.Debit_info),int(self.Credit_info)))
########################################################################
            cur = con.cursor()
            
            
            con.commit()
            #c.close()
            #con.close()
            screen5.destroy()
            self.Print_Adjusted_Trial_Balance(con)
            self.Income_statement()
            self.OwnersEquity_statement()
            self. Balance_Sheet(con)
            self.ClosingEntries(con)
            self.Post_Closing_trial_balance(con)
            #self.Screen5()
        Okay = Button(screen5, text="Okay", width="18", height="3",fg='black',font=("Lucida Console",8,'bold'))
        Okay.bind('<Button-1>', S5Click)
        Okay.place(x=335, y=430)
        def BackScreen4(event):
            self.Screen4()
            screen5.destroy()
        Back_button=Button(screen5, text="Back",fg='black')
        Back_button.pack()
        Back_button.bind('<Button-1>',BackScreen4)
        Back_button.place(x=10,y=440)
      
                    
   
    def CreateTCash(self):
        #c=con.cursor()
        #cur = con.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS Cash(DATE integer, AccountsExplanationDebit Text ,Debit integer,Total integer)')
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
    def CreateTRevenue(self):
        c.execute('CREATE TABLE IF NOT EXISTS Revenue(DATE integer, AccountsExplanationCredit Text ,Credit integer,Total integer)')
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()   
    def CreateTOwnersEquity(self):
        c.execute('CREATE TABLE IF NOT EXISTS OwnersEquity(DATE integer, AccountsExplanationDebit Text ,Debit integer,Total integer)')
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
    def CreateTExpense(self):
        c.execute('CREATE TABLE IF NOT EXISTS Expense(DATE integer, AccountsExplanationDebit Text ,Debit integer,Total integer)')
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
    def CreateTOwnersCapital(self):
        c.execute('CREATE TABLE IF NOT EXISTS OwnersCapital(DATE integer, AccountsExplanationCredit Text ,Credit integer,Total integer)')
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
    def CreateTDrawing(self):
        c.execute('CREATE TABLE IF NOT EXISTS Drawing(DATE integer, AccountsExplanationDebit Text ,Debit integer,Total integer)')
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
    def CreateTPayable(self):
        c.execute('CREATE TABLE IF NOT EXISTS AccountsPayable(DATE integer, AccountsExplanationCredit Text ,Credit integer,Total integer)')
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
    def Create_Ledgers_Table(self):
        self.CreateTCash()
        self.CreateTRevenue()
        self.CreateTOwnersEquity()
        self.CreateTExpense()
        self.CreateTOwnersCapital()
        self.CreateTDrawing()
        self.CreateTPayable()
    def TCash(self):
        j = 0
        l= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit = 'Cash'")
        a=cur.fetchall()
        #print(a)
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit = 'Cash'")
        x=cur.fetchall()
        cur.execute("SELECT * FROM journal_entries WHERE AccountsExplanationDebit = 'Cash'")
        f = cur.fetchall()
        for y in f:
            #print(y[0],y[1],y[2],y[3], end=' \n')
            c=con.cursor()
            c.execute("INSERT INTO Cash(DATE ,AccountsExplanationDebit,Debit)VALUES(?,?,?)",(y[0], y[1], y[3]))
            con.commit()
        for i in x:
            j = i[0]
        for m in a:
            l = m[0]
        
        
        
        #print(x)
        if l >j or l==j or j==0:
            balance = l - j
            c=con.cursor()
            c.execute("INSERT INTO Cash(Total)  VALUES(?)",(balance,))
            con.commit()
            

            

            print('Cash =', balance)
        elif l<j or l==0:  
             balance = j - l
             print('Cash=',balance)
             c=con.cursor()
             c.execute("INSERT INTO Cash(Total)  VALUES(?)",(balance,))
             con.commit()
    def TOwnersEquity(self):
        j = 0
        l= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit = 'OwnersEquity'")
        a=cur.fetchall()
        #print(a)
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit = 'OwnersEquity'")
        x=cur.fetchall()
        cur.execute("SELECT * FROM journal_entries WHERE AccountsExplanationDebit = 'OwnersEquity'")
        f = cur.fetchall()
        for y in f:
            #print(y[0],y[1],y[2],y[3], end=' \n')
            c=con.cursor()
            c.execute("INSERT INTO OwnersEquity(DATE ,AccountsExplanationDebit,Debit)VALUES(?,?,?)",(y[0], y[1], y[3]))
            con.commit()
        for i in x:
            j = i[0]
        for m in a:
            l = m[0]
        #print(x)
        if l >j or l==j or j==0:
            balance = l - j
            print('Owners Equity=', balance)
            c=con.cursor()
            c.execute("INSERT INTO OwnersEquity(Total)  VALUES(?)",(balance,))
            con.commit()

        
        elif l<j or l==0:
            balance = j - l
            print('Owners Equity =',balance)
            c=con.cursor()
            c.execute("INSERT INTO OwnersEquity(Total)  VALUES(?)",(balance,))
            con.commit()

            return 0
    def TExpense(self):
        j = 0
        l= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit = 'Expense'")
        a=cur.fetchall()
        #print(a)
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit = 'Expense'")
        x=cur.fetchall()
        cur.execute("SELECT * FROM journal_entries WHERE AccountsExplanationDebit= 'Expense'")
        f = cur.fetchall()
        for y in f:
            #print(y[0],y[1],y[2],y[3], end=' \n')
            c=con.cursor()
            c.execute("INSERT INTO Expense(DATE ,AccountsExplanationDebit,Debit)VALUES(?,?,?)",(y[0], y[1], y[3]))
            con.commit()
        for i in x:
            j = i[0]
        for m in a:
            l = m[0]
        #print(x)
        if l >j or l==j or j==0:
            balance = l - j
            #return balance
            print('Expense = ',balance)
            c=con.cursor()
            c.execute("INSERT INTO Expense(Total)  VALUES(?)",(balance,))
            con.commit()
        

        
        elif l<j or l==0:
            balance = j - l
           # return balance
            print('Expense =', balance)
            c=con.cursor()
            c.execute("INSERT INTO Expense(Total)  VALUES(?)",(balance,))
            con.commit()
        

            return 0
       
    def TRevenue(self):
        j = 0
        l= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit = 'Revenue'")
        a=cur.fetchall()
        #print(a)
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit = 'Revenue'")
        x=cur.fetchall()
        cur.execute("SELECT * FROM journal_entries WHERE AccountsExplanationCredit = 'Revenue'")
        f = cur.fetchall()
        for y in f:
            #print(y[0],y[1],y[2],y[3], end=' \n')
            c=con.cursor()
            c.execute("INSERT INTO Revenue(DATE ,AccountsExplanationCredit,Credit)VALUES(?,?,?)",(y[0], y[2], y[3]))
            con.commit()
        for i in x:
            j = i[0]
        for m in a:
            l = m[0]
        #print(x)
        if l >j or l==j or j==0:
            balance = l - j
            #return balance
            print('Revenue = ', balance)
            c=con.cursor()
            c.execute("INSERT INTO Revenue(Total)  VALUES(?)",(balance,))
            con.commit()
      

        
        elif l<j or l==0:
            balance = j - l
            #return balance
            print('Revenue =', balance)
            c=con.cursor()
            c.execute("INSERT INTO Revenue(Total)  VALUES(?)",(balance,))
            con.commit()
    def TOwnersCapital(self):
        j = 0
        l= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit = 'OwnersCapital'")
        a=cur.fetchall()
        #print(a)
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit = 'OwnersCapital'")
        x=cur.fetchall()
        cur.execute("SELECT * FROM journal_entries WHERE AccountsExplanationCredit = 'OwnersCapital'")
        f = cur.fetchall()
        for y in f:
             #print(y[0],y[1],y[2],y[3], end=' \n')
            c=con.cursor()
            c.execute("INSERT INTO OwnersCapital(DATE ,AccountsExplanationCredit,Credit)VALUES(?,?,?)",(y[0], y[2], y[3]))
            con.commit()
        for i in x:
            j = i[0]
        for m in a:
            l = m[0]
        #print(x)
        if l>j or l==j or j==0:
            balance =  l - j
            print('Owners Capital=', balance)
            c=con.cursor()
            c.execute("INSERT INTO OwnersCapital(Total)  VALUES(?)",(balance,))
            con.commit()

        
        elif l<j or l==0:
            balance = j - l
            print('Owners Capital =',balance)
            c=con.cursor()
            c.execute("INSERT INTO OwnersCapital(Total)  VALUES(?)",(balance,))
            con.commit()
    def TDrawing(self):
        j = 0
        l= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit = 'Drawing'")
        a=cur.fetchall()
        #print(a)
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit = 'Drawing'")
        x=cur.fetchall()
        cur.execute("SELECT * FROM journal_entries WHERE AccountsExplanationDebit = 'Drawing'")
        f = cur.fetchall()
        for y in f:
            #print(y[0],y[1],y[2],y[3], end=' \n')
            c=con.cursor()
            c.execute("INSERT INTO Drawing(DATE ,AccountsExplanationDebit,Debit)VALUES(?,?,?)",(y[0], y[1], y[3]))
            con.commit()
        for i in x:
            j = i[0]
        for m in a:
            l = m[0]
        #print(x)
        if l >j or l==j or j==0:
            balance = l - j
            print('Drawing =', balance)
            c=con.cursor()
            c.execute("INSERT INTO Drawing(Total)  VALUES(?)",(balance,))
            con.commit()

        
        elif l<j or l==0:
            balance = j - l
            print('Drawing =',balance)
            c=con.cursor()
            c.execute("INSERT INTO Drawing(Total)  VALUES(?)",(balance,))
            con.commit()

            return 0
    def TPayable(self):
        j = 0
        l= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit = ' AccountsPayable'")
        a=cur.fetchall()
        #print(a)
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit = 'AccountsPayable'")
        x=cur.fetchall()
        cur.execute("SELECT * FROM journal_entries WHERE AccountsExplanationCredit = ' AccountsPayable'")
        f = cur.fetchall()
        for y in f:
            #print(y[0],y[1],y[2],y[3], end=' \n')
            c=con.cursor()
            c.execute("INSERT INTO AccountsPayable(DATE ,AccountsExplanationCredit,Credit)VALUES(?,?,?)",(y[0], y[2], y[3]))
            con.commit()
        for i in x:
            j = i[0]
        for m in a:
            l = m[0]
        #print(x)
        if l >j or l==j or j==0:
            balance = l - j
            #return balance
            print('AccountsPayable = ', balance)
            c=con.cursor()
            c.execute("INSERT INTO AccountsPayable(Total)  VALUES(?)",(balance,))
            con.commit()
      

        
        elif l<j or l==0:
            balance = j - l
            #return balance
            print(' AccountsPayable =', balance)
            c=con.cursor()
            c.execute("INSERT INTO AccountsPayable(Total)  VALUES(?)",(balance,))
            con.commit()

            
        
            
        
    
    def Taccounts(self):
        return(self.TCash(),
        self.TOwnersEquity(),
        self.TRevenue(),
        self.TExpense(),
        self.TOwnersCapital(),
        self.TDrawing(),
        self.TPayable)
    def Print_Trial_Balance(self,con):
        print('-'*155)
        print("\t\t\t\t\t Trial Balance Sheet")
        #print("\t\t\t\t\t", self.comp_name)
        print('-'*155)
        cur = con.cursor()
        #cur.execute("SELECT SUM (Debit) FROM journal_entries and AccountsExplanation WHERE AccountsExplanation = 'Cash'or AccountsExplanation FROM journal_entries ")
        Accounts=['Cash','Equipment', 'Accounts Reciveable', 'Accounts Payable', 'OwnersEquity','Revenue','Expense','OwnersCapital','Drawing']
        for i in Accounts:
            cur.execute("SELECT AccountsExplanationDebit,SUM (Debit)FROM journal_entries WHERE AccountsExplanationDebit =?",(i,))
            cur.execute("SELECT AccountsExplanationCredit,SUM(Credit) FROM journal_entries WHERE AccountsExplanationCredit =?",(i,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
    
            
       # cur.execute("SELECT AccountsExplanation,Debit,Credit FROM journal_entries")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.execute("SELECT SUM (Debit) FROM journal_entries")
        x=cur.fetchall()
        #print('Total of Debit',x)
        cur.execute("SELECT SUM (Credit) FROM journal_entries")
        d=cur.fetchall()
        print('-'*155)
        print('Total ',x,d)
        print('-'*155)
    def Print_Adjusted_Trial_Balance(self,con):
        print('-'*155)
        print("\t\t\t\t\t Adjusted Trial Balance Sheet")
        #print("\t\t\t\t\t", self.comp_name)
        print('-'*155)
        a = con.cursor()
        #cur.execute("SELECT SUM (Debit) FROM journal_entries and AccountsExplanation WHERE AccountsExplanation = 'Cash'or AccountsExplanation FROM journal_entries ")
        Accounts=['Cash','Equipment', 'Accounts Reciveable', 'Accounts Payable', 'OwnersEquity','Revenue','Expense','OwnersCapital','Drawing']
        for i in Accounts:
            a.execute("SELECT AccountsExplanationDebit,SUM (Debit)FROM journal_entries WHERE AccountsExplanationDebit =?",(i,))
            a.execute("SELECT AccountsExplanationCredit,SUM(Credit) FROM journal_entries WHERE AccountsExplanationCredit =?",(i,))
            rows = a.fetchall()
            for row in rows:
                print(row)
    
            
       # cur.execute("SELECT AccountsExplanation,Debit,Credit FROM journal_entries")
        rows = a.fetchall()
        for row in rows:
            print(row)
        a.execute("SELECT SUM (Debit) FROM journal_entries")
        x=a.fetchall()
        #print('Total of Debit',x)
        a.execute("SELECT SUM (Credit) FROM journal_entries")
        d=a.fetchall()
        print('-'*155)
        print('Total ',x,d)
        print('-'*155)
    def Income_statement(self):
        j = 0
        l= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        #cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanation = 'Revenue'")
        #a=cur.fetchall()
        #print(a)
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit = 'Revenue'")
        x=cur.fetchall()
        #cur.execute("SELECT * FROM journal_entries WHERE AccountsExplanation = 'Revenue'")
        for i in x:
            j = i[0]
        #for m in a:
         #   l = m[0]
            a=j
            print(a)
        f = 0
        k= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit = 'Expense'")
        y=cur.fetchall()
        #print(a)
        #cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanation = 'Expense'")
        #v=cur.fetchall()
        #for k in v:
         #   k = i[0]
        for f in y:
            q = f[0]
            b=q
            print(b)
        
       
        Net_Income=a-b
        self. Incomestatement= Net_Income
        print('Net Income = ',Net_Income)
    def OwnersEquity_statement(self):
        j = 0
        l= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        #cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanation = 'Revenue'")
        #a=cur.fetchall()
        #print(a)
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit = 'OwnersCapital'")
        x=cur.fetchall()
        #cur.execute("SELECT * FROM journal_entries WHERE AccountsExplanation = 'Revenue'")
        for i in x:
            j = i[0]
        #for m in a:
         #   l = m[0]
            z=j
            print(z)
            y=self. Incomestatement
            print (y)
        New_OwnersCapital= y + z
        print ("Owners capit + net incme",New_OwnersCapital)
        f = 0
        k= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit = 'Drawing'")
        y=cur.fetchall()
        
        for f in y:
            q = f[0]
            n=q
            print(n)
        if n==0 or n< New_OwnersCapital or n > New_OwnersCapital:
            OwnerCapital= New_OwnersCapital-n
            print(' NewOwnersCapital = ',OwnerCapital)
    def Balance_Sheet(self,con):
        cur = con.cursor()
        print('-'*155)
        print("\t\t\t\t\t Balance Sheet")
        print('-'*155)
        print("Assets Accounts")
        Asset_Accounts=['Cash','AccountsRecivable','Equipment']
        for i in  Asset_Accounts:
             cur.execute("SELECT AccountsExplanationDebit,SUM (Debit)FROM journal_entries WHERE AccountsExplanationDebit =?",(i,))
             rows = cur.fetchall()
             for row in rows:
                print(row)
        Asset_Accounts=['Cash','AccountsRecivable','Equipment']
        for q in  Asset_Accounts:
            cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit=?",(q,))
            x=cur.fetchall()
       # print(x)
        print('-'*155)
        print('Total ',x)
        print('-'*155)
        print("Laibitlities Account")
        Liabilities_Accounts=["AccountsPayable","IntrestPayable"]
        for j in Liabilities_Accounts:
             cur.execute("SELECT AccountsExplanationCredit,SUM (Credit)FROM journal_entries WHERE AccountsExplanationCredit =?",(j,))
             rows = cur.fetchall()
             for row in rows:
                print(row)
        Liabilities_Accounts=["AccountsPayable","IntrestPayable"]
        for f in Liabilities_Accounts:
            cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit=?",(f,))
            g=cur.fetchall()
        #print(g)
            
            
     
        #d=cur.fetchall()
        print('-'*155)
        print('Total ',g)
        print('-'*155)
    def ClosingEntries(self,con):
        print('-'*155)
        print('\t\t\t\t\t Closing Entries')
        print('-'*155)
        cur = con.cursor()
        print('Revenue')
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit='Revenue'")
        d=cur.fetchall()
        print(d)
        self.ICS=d
        print(self.ICS)
        print('Expense')
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit='Expense'")
        a=cur.fetchall()
        print(a)
        self.ICS=a
        print(self.ICS)
        print('IncomeSummary')
        z=self. Incomestatement
        print(z)
        self.ICS=z
        print(z)
        print('OwnersCapital')
        j = 0
        l= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        #cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanation = 'Revenue'")
        #a=cur.fetchall()
        #print(a)
        cur.execute("SELECT SUM (Credit) FROM journal_entries WHERE AccountsExplanationCredit = 'OwnersCapital'")
        x=cur.fetchall()
        #cur.execute("SELECT * FROM journal_entries WHERE AccountsExplanation = 'Revenue'")
        for i in x:
            j = i[0]
        #for m in a:
         #   l = m[0]
            z=j
            #print(z)
            y=self. Incomestatement
            print (y)
        New_OwnersCapital= y + z
       # print ("Owners capit + net incme",New_OwnersCapital)
        f = 0
        k= 0
        con= sqlite3.connect('Journal Entries.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Debit) FROM journal_entries WHERE AccountsExplanationDebit = 'Drawing'")
        y=cur.fetchall()
        
        for f in y:
            q = f[0]
            n=q
           # print(n)
        if n==0 or n< New_OwnersCapital or n > New_OwnersCapital:
            OwnerCapital= New_OwnersCapital-n
            print(' NewOwnersCapital = ',OwnerCapital)
    def Post_Closing_trial_balance(self,con):
         print('-'*155)
         print('\t\t\t\tPost Closing Trial Balance')
         print('-'*155)
         cur = con.cursor()
         Debit_Accounts=['Cash','AccountsRecivable','Equipment']
         for i in  Debit_Accounts:
             cur.execute("SELECT AccountsExplanationDebit,SUM (Debit)FROM journal_entries WHERE AccountsExplanationDebit =?",(i,))
             rows = cur.fetchall()
             for row in rows:
                print(row)
         Credit_Accounts=["AccountsPayable","OwnersCapital"]
         for j in Credit_Accounts:
             cur.execute("SELECT AccountsExplanationCredit,SUM (Credit)FROM journal_entries WHERE AccountsExplanationCredit =?",(j,))
             rows = cur.fetchall()
             for row in rows:
                print(row)
         print('-'*155)
         print('Total ')
         print('-'*155)
                         
     
        
        
        
    
    
    
            
            
            
        
        
      
    
        
       
            
a= JournalEntry()
a.create_table()
a. Create_Ledgers_Table()
#a. TCash()
#a.Account_Chart()
a.MainScreen()
#a.Screen3()
con.commit()
c.close()
con.close()
