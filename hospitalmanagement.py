from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import mysql.connector as msql
from tkinter import messagebox
from tkinter import filedialog


class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Manaagement system")
        self.root.geometry("1540x800+0+0")
        lbtitle=Label(self.root,bd=20,relief=RIDGE,text="+ Hospital Management System",bg="white",fg="red",font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP,fill="x")

        self.nameoftablet=StringVar()
        self.refno=StringVar()
        self.dose=StringVar()
        self.notablet=StringVar()
        self.lot=StringVar()
        self.Issuedate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.sideeffect=StringVar()
        self.furtherinfo=StringVar()
        self.bloodpressure=StringVar()
        self.storage=StringVar()
        self.medication=StringVar()
        self.pid=StringVar()
        self.nhs=StringVar()
        self.pname=StringVar()
        self.dob=StringVar()
        self.paddress=StringVar()
        
        #---------------------------DataFrame------------------------------------------------------
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)
        
        DataFrameleft=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,font=("times new roman",15,"bold")
                                ,text="Patient Information")
        DataFrameleft.place(x=8,y=3,width=980,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,padx=10,relief=RIDGE,font=("times new roman",15,"bold")
                                ,text="Prescription")
        DataFrameRight.place(x=998,y=3,width=485,height=350)

        #--------------------------ButtonFrame----------------------------
        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,height=70,width=1530)

        #--------------------------DeatailsFrame------------------------------
        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,height=190,width=1530)

        #--------------------------DataleftFrame------------------------------
        lblName=Label(DataFrameleft,text="Name of the Tablet",font=("arial",12,"bold"),pady=5)
        lblName.grid(row=0,column=0,sticky="w")
        
        TabletName=ttk.Combobox(DataFrameleft,textvariable=self.nameoftablet,font=("arial",12,"bold"),width=32)
        TabletName["values"]=("Nice","Corona Vaccine","Paracetamol","Acetaminophen","Adderall","Amlodipine","Ativan")
        TabletName.grid(row=0,column=1)
       
        ReferLabel=Label(DataFrameleft,text="Reference No.",font=("arial",12,"bold"),pady=5)
        ReferLabel.grid(row=1,column=0,sticky="w")

        Referentry=Entry(DataFrameleft,textvariable=self.refno,font=("arial",12,"bold"),width=34)
        Referentry.grid(row=1,column=1)

        DoseLabel=Label(DataFrameleft,text="Dose:",font=("arial",12,"bold"),pady=5)
        DoseLabel.grid(row=2,column=0,sticky="w")

        DoseEntry=Entry(DataFrameleft,font=("arial",12,"bold"),textvariable=self.dose,width=34)
        DoseEntry.grid(row=2,column=1)

        Notablet=Label(DataFrameleft,text="No. of Tablets",font=("arial",12,"bold"),pady=5)
        Notablet.grid(row=3,column=0,sticky="w")
        NoTabEntry=Entry(DataFrameleft,font=("arail",12,"bold"),textvariable=self.notablet,width=34)
        NoTabEntry.grid(row=3,column=1)

        LotLabel=Label(DataFrameleft,text="Lot",font=("arial",12,"bold"),pady=5)
        LotLabel.grid(row=4,column=0,sticky="w")
        LotEntry=Entry(DataFrameleft,font=("arail",12,"bold"),textvariable=self.lot,width=34)
        LotEntry.grid(row=4,column=1)

        IssueLabel=Label(DataFrameleft,text="Issue Date",font=("arial",12,"bold"),pady=5)
        IssueLabel.grid(row=5,column=0,sticky="w")
        IssueEntry=Entry(DataFrameleft,textvariable=self.Issuedate,font=("arail",12,"bold"),width=34)
        IssueEntry.grid(row=5,column=1)

        ExpLabel=Label(DataFrameleft,text="Expiry Date",font=("arial",12,"bold"),pady=5)
        ExpLabel.grid(row=6,column=0,sticky="w")
        ExpEntry=Entry(DataFrameleft,textvariable=self.expdate,font=("arail",12,"bold"),width=34)
        ExpEntry.grid(row=6,column=1)

        DailyLabel=Label(DataFrameleft,text="Daily Dose",font=("arial",12,"bold"),pady=5)
        DailyLabel.grid(row=7,column=0,sticky="w")
        DailyEntry=Entry(DataFrameleft,textvariable=self.dailydose,font=("arail",12,"bold"),width=34)
        DailyEntry.grid(row=7,column=1)

        SideLabel=Label(DataFrameleft,text="Side Effect",font=("arial",12,"bold"),pady=5)
        SideLabel.grid(row=8,column=0,sticky="w")
        SideEntry=Entry(DataFrameleft,textvariable=self.sideeffect,font=("arail",12,"bold"),width=34)
        SideEntry.grid(row=8,column=1)

        FurthLabel=Label(DataFrameleft,text="Further Information",font=("arial",12,"bold"),padx=5)
        FurthLabel.grid(row=0,column=2,sticky="w")
        FurthEntry=Entry(DataFrameleft,textvariable=self.furtherinfo,font=("arial",12,"bold"),width=34)
        FurthEntry.grid(row=0,column=3)

        BloodLabel=Label(DataFrameleft,text="Blood Pressure",font=("arial",12,"bold"),padx=5)
        BloodLabel.grid(row=1,column=2,sticky="w")
        BloodEntry=Entry(DataFrameleft,textvariable=self.bloodpressure,font=("arial",12,"bold"),width=34)
        BloodEntry.grid(row=1,column=3)

        StorageLabel=Label(DataFrameleft,text="Storage Advice",font=("arial",12,"bold"),padx=5)
        StorageLabel.grid(row=2,column=2,sticky="w")
        StorageEntry=Entry(DataFrameleft,textvariable=self.storage,font=("arial",12,"bold"),width=34)
        StorageEntry.grid(row=2,column=3)

        MedLabel=Label(DataFrameleft,text="Medication",font=("arial",12,"bold"),padx=5)
        MedLabel.grid(row=3,column=2,sticky="w")
        MedEntry=Entry(DataFrameleft,textvariable=self.medication,font=("arial",12,"bold"),width=34)
        MedEntry.grid(row=3,column=3)

        PatIdLabel=Label(DataFrameleft,text="Patient Id",font=("arial",12,"bold"),padx=5)
        PatIdLabel.grid(row=4,column=2,sticky="w")
        PatIdEntry=Entry(DataFrameleft,textvariable=self.pid,font=("arial",12,"bold"),width=34)
        PatIdEntry.grid(row=4,column=3)

        NHSLabel=Label(DataFrameleft,text="NHS Number",font=("arial",12,"bold"),padx=5)
        NHSLabel.grid(row=5,column=2,sticky="w")
        NHSEntry=Entry(DataFrameleft,textvariable=self.nhs,font=("arial",12,"bold"),width=34)
        NHSEntry.grid(row=5,column=3)

        PatNameLabel=Label(DataFrameleft,text="Patient Name",font=("arial",12,"bold"),padx=5)
        PatNameLabel.grid(row=6,column=2,sticky="w")
        PatNameEntry=Entry(DataFrameleft,textvariable=self.pname,font=("arial",12,"bold"),width=34)
        PatNameEntry.grid(row=6,column=3)

        DOBLabel=Label(DataFrameleft,text="Date of Birth",font=("arial",12,"bold"),padx=5)
        DOBLabel.grid(row=7,column=2,sticky="w")
        DOBEntry=Entry(DataFrameleft,textvariable=self.dob,font=("arial",12,"bold"),width=34)
        DOBEntry.grid(row=7,column=3)
        
        AddressLabel=Label(DataFrameleft,text="Patient Address",font=("arial",12,"bold"),padx=5)
        AddressLabel.grid(row=8,column=2,sticky="w")
        AddressEntry=Entry(DataFrameleft,textvariable=self.paddress,font=("arial",12,"bold"),width=34)
        AddressEntry.grid(row=8,column=3)

        #-----------------------------RightFrame------------------------------------
        # ----------------------------- Right Frame -----------------------------


        # Configure grid layout inside Right Frame
        DataFrameRight.grid_rowconfigure(0, weight=1)
        DataFrameRight.grid_rowconfigure(1, weight=0)
        DataFrameRight.grid_columnconfigure(0, weight=1)

        # Text widget
        self.Prescriptiontextbox = Text(DataFrameRight, font=("arial", 12, "bold"), height=16, width=50)
        self.Prescriptiontextbox.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nsew")

        # Download Button
        self.DownloadButton = Button(DataFrameRight, command=self.save_file,
                             font=("arial", 12, "bold"), text="Download", bg="blue", fg="white", width=20)
        self.DownloadButton.grid(row=1, column=0, pady=(5, 10), sticky="e")


        #-------------------------ButtonFrame-----------------------------------
        Button1=Button(ButtonFrame,command=self.Prescriptionboxdata,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),
                       width=23,padx=2,pady=2)
        Button1.grid(row=0,column=0)

        Button2=Button(ButtonFrame,text=" Insert Patient Data",bg="green",fg="white",font=("arial",12,"bold"),
                       command=self.Presriptiondata,width=23,padx=2,pady=2)
        Button2.grid(row=0,column=1)

        Button3=Button(ButtonFrame,text="Update",bg="green",fg="white",font=("arial",12,"bold"),command=self.update,
                       width=23,height=1,padx=3,pady=2)
        Button3.grid(row=0,column=3)

        Button4=Button(ButtonFrame,text="Delete",command=self.Delete,bg="green",fg="white",font=("arial",12,"bold"),
                       width=23,height=1,padx=3,pady=2)
        Button4.grid(row=0,column=4)

        Button5=Button(ButtonFrame,text="Clear",command=self.clear,bg="green",fg="white",font=("arial",12,"bold"),
                       width=23,height=1,padx=3,pady=2)
        Button5.grid(row=0,column=5)

        Button6=Button(ButtonFrame,text="Exit",command=self.exit,bg="green",fg="white",font=("arial",12,"bold"),
                       width=23,height=1,padx=3,pady=2)
        Button6.grid(row=0,column=6)


        #-------------------------------------Details Frame--------------------------------
        #---------------------Scroll bar---------------------
        
        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        #In Tkinter, the Treeview widget (part of the ttk module) is used to display- 
        #hierarchical or tabular data in rows and columns — similar to a table or a file explorer.
        self.hospital_table=ttk.Treeview(DetailsFrame,column=("Name of Tablet","Reference No.","Dose","No. of Tablets","Lot"
        ,"Issue Date","Exp Date","Daily Dose","Storage Advice","NHS Number","Patient Name","DOB","Patient Address")
                                        ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill="x")
        scroll_y.pack(side=RIGHT,fill="y")
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        self.hospital_table.heading("Name of Tablet",text="Name of Tablet")
        self.hospital_table.heading("Reference No.",text="Reference No.")
        self.hospital_table.heading("Dose",text="Dose")
        self.hospital_table.heading("No. of Tablets",text="No. of Tablets")
        self.hospital_table.heading("Lot",text="Lot")
        self.hospital_table.heading("Issue Date",text="Issue Date")
        self.hospital_table.heading("Exp Date",text="Exp Date")
        self.hospital_table.heading("Daily Dose",text="Daily Dose")
        self.hospital_table.heading("Storage Advice",text="Storage Advice")
        self.hospital_table.heading("NHS Number",text="NHS Number")
        self.hospital_table.heading("Patient Name",text="Patient Name")
        self.hospital_table.heading("DOB",text="DOB")
        self.hospital_table.heading("Patient Address",text="Patient Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("Name of Tablet",width=100)
        self.hospital_table.column("Reference No.",width=100)
        self.hospital_table.column("Dose",width=100)
        self.hospital_table.column("No. of Tablets",width=100)
        self.hospital_table.column("Lot",width=100)
        self.hospital_table.column("Exp Date",width=100)
        self.hospital_table.column("Daily Dose",width=100)
        self.hospital_table.column("Storage Advice",width=100)
        self.hospital_table.column("NHS Number",width=100)
        self.hospital_table.column("Patient Name",width=100)
        self.hospital_table.column("DOB",width=100)
        self.hospital_table.column("Patient Address",width=100)
        self.hospital_table.column("Issue Date",width=100)
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetchdata()

    #-------------------------Fuctionality-------------------------------------------
    def update(self):
        conn=msql.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM hospital WHERE Reference_no=%s",(self.refno.get(),))
        rows=my_cursor.fetchall()
        if len(rows)==0:
            messagebox.showerror("Error","Invalid Data")
        else:
            query="""UPDATE hospital set NameofTablet=%s, dose=%s, no_of_tablets=%s, lot=%s, issue_date=%s,
            expiry_date=%s, daily_dose=%s, storagead=%s, nhs=%s, patient_name=%s, dob=%s, patient_address=%s WHERE Reference_no=%s"""
            values=[self.nameoftablet.get(),
                    self.dose.get(),
                    self.notablet.get(),
                    self.lot.get(),
                    self.Issuedate.get(),
                    self.expdate.get(),
                    self.dailydose.get(),
                    self.storage.get(),
                    self.nhs.get(),
                    self.pname.get(),
                    self.dob.get(),
                    self.paddress.get(),
                    self.refno.get()]
            messagebox.showinfo("Success","Your data has been updated")
            my_cursor.execute(query,values)
        conn.commit()
        conn.close()
        self.fetchdata()
        
        
    def Presriptiondata(self):
        if self.nameoftablet.get()=="" or self.refno.get()=="":
            messagebox.showerror(title="Error",message="All fields are required")
        else:
            conn=msql.connect(host="localhost",username="root",password="1234",database="mydata")
            mycursor=conn.cursor()
            query="INSERT INTO hospital VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values=[self.nameoftablet.get(),
                    self.refno.get(),
                    self.dose.get(),
                    self.notablet.get(),
                    self.lot.get(),
                    self.Issuedate.get(),
                    self.expdate.get(),
                    self.dailydose.get(),
                    self.storage.get(),
                    self.nhs.get(),
                    self.pname.get(),
                    self.dob.get(),
                    self.paddress.get()]
            mycursor.execute(query,values)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Data has been inserted")
            self.fetchdata()
    def fetchdata(self):
        conn=msql.connect(host="localhost",username="root",password="1234",database="mydata")
        mycursor=conn.cursor()
        mycursor.execute("SELECT * FROM hospital")
        rows=mycursor.fetchall()
        if len(rows):
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
                conn.commit()
        conn.close()
    #we want that when we click the cursor in treeview the data will be filled with that data
    def get_cursor(self,even):
        cursor_row=self.hospital_table.focus()#fetches the cursor in data table
        content=self.hospital_table.item(cursor_row) #fetches all the data of the cursor row
        row=content['values']
        self.nameoftablet.set(row[0])
        self.refno.set(row[1])
        self.dose.set(row[2])
        self.notablet.set(row[3])
        self.lot.set(row[4])
        self.Issuedate.set(row[5])
        self.expdate.set(row[6])
        self.dailydose.set(row[7])
        self.storage.set(row[8])
        self.nhs.set(row[9])
        self.pname.set(row[10])
        self.dob.set(row[11])
        self.paddress.set(row[12])

    def Prescriptionboxdata(self):
        self.Prescriptiontextbox.insert(END,"Name of Tablet:\t\t\t"+self.nameoftablet.get())
        self.Prescriptiontextbox.insert(END,"\nReference no.:\t\t\t"+self.refno.get())
        self.Prescriptiontextbox.insert(END,"\nDose:\t\t\t"+self.dose.get())
        self.Prescriptiontextbox.insert(END,"\nNumber of Tablets:\t\t\t"+self.notablet.get())
        self.Prescriptiontextbox.insert(END,"\nLot:\t\t\t"+self.lot.get())
        self.Prescriptiontextbox.insert(END,"\nIssue date:\t\t\t"+self.Issuedate.get())
        self.Prescriptiontextbox.insert(END,"\nExpiry Dtae:\t\t\t"+self.expdate.get())
        self.Prescriptiontextbox.insert(END,"\nDaily Dose:\t\t\t"+self.dailydose.get())
        self.Prescriptiontextbox.insert(END,"\nSide Effect:\t\t\t"+self.sideeffect.get())
        self.Prescriptiontextbox.insert(END,"\nFurther Information:\t\t\t"+self.furtherinfo.get())
        self.Prescriptiontextbox.insert(END,"\nStorage Advice:\t\t\t"+self.storage.get())
        self.Prescriptiontextbox.insert(END,"\nBlood Pressure:\t\t\t"+self.bloodpressure.get())
        self.Prescriptiontextbox.insert(END,"\nPatient Id:\t\t\t"+self.pid.get())
        self.Prescriptiontextbox.insert(END,"\nNHS Number:\t\t\t"+self.nhs.get())
        self.Prescriptiontextbox.insert(END,"\nPatient Name:\t\t\t"+self.pname.get())
        self.Prescriptiontextbox.insert(END,"\ndate of Birth:\t\t\t"+self.dob.get())
        self.Prescriptiontextbox.insert(END,"\nPatient address:\t\t\t"+self.paddress.get())
    def Delete(self):
        conn=msql.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM hospital WHERE Reference_no=%s",(self.refno.get(),))
        rows=my_cursor.fetchall()
        if len(rows)==0:
            messagebox.showerror("Error","Invalid Data")
        else:
            query="DELETE FROM hospital WHERE Reference_no=%s"
            value=(self.refno.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            messagebox.showinfo("Success","Data Deleted")
        self.fetchdata()
        conn.commit()
        conn.close()
        
    def clear(self):
        self.nameoftablet.set("")
        self.refno.set("")
        self.dose.set("")
        self.notablet.set("")
        self.lot.set("")
        self.Issuedate.set("")
        self.expdate.set("")
        self.dailydose.set("")
        self.storage.set("")
        self.nhs.set("")
        self.pname.set("")
        self.dob.set("")
        self.paddress.set("")
        self.sideeffect.set("")
        self.furtherinfo.set("")
        self.bloodpressure.set("")
        self.pid.set("")
        self.medication.set("")
        self.Prescriptiontextbox.delete(1.0,"end")
    def exit(self):
        i_exit=messagebox.askyesno("Hospital Management System","Do you really want to exit")
        if i_exit>0:
           root.destroy()
           return
    def save_file(self):
        content=self.Prescriptiontextbox.get(1.0,END)
        if content.strip()=="":
            messagebox.showerror("Error","Prescription is Empty")
            return
        file_path=filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files",".txt")],
            title="Save Prescription as"
        )
        if file_path:
            try:
                with open(file_path,"w") as file:
                    file.write(content)
                messagebox.showinfo("Success","Prescription succesfully downloaded")
            except Exception as e:
                messagebox.showerror("Error",f"Unable to save file\n{str(e)}")
            
            


        
if __name__=="__main__":
    root=Tk()
    ui=hospital(root)
    root.mainloop()