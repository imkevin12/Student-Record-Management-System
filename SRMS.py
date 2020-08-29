from future.moves.tkinter import *
from tkinter import ttk, messagebox
import os

class Student:
    def __init__(self):
        self.root = Tk()
        self.root.title("Student Record Management System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(0, 0)
        self.root.iconbitmap('srms.ico')


        # Title
        title = Label(self.root, text="Student Record Management System", bd=8, relief=GROOVE, font=("impact", 25, "bold"), bg="#273746", fg="white")
        title.pack(side=TOP, fill=X)

        # *************** Student Registration Frame *************** #
        Std_Frame = Frame(self.root, bd=10, relief=GROOVE)
        Std_Frame.place(x=20, y=80, width=860, height=480)

        std_title = Label(Std_Frame, text="Student Registration Form", font=("times new roman", 25, "bold"))
        std_title.grid(row=0, columnspan=4, pady=10)

        # *************** All Variable *************** #
        self.stdIdVar = StringVar()
        self.firstnameVar = StringVar()
        self.lastnameVar = StringVar()
        self.challanVar = StringVar()
        self.dobVar = StringVar()
        self.emailVar = StringVar()
        self.genderVar = StringVar()
        self.cityVar = StringVar()
        self.courseVar = StringVar()
        self.stateVar = StringVar()
        self.idproofVar = StringVar()
        self.contactVar = StringVar()
        self.paymentVar = StringVar()

        # Student ID
        stdId_lbl = Label(Std_Frame, text="Student ID", font=("times new roman", 20, "bold")).grid(row=1, columnspan=2, padx=20, pady=10, sticky='w')
        stdId_entry = Entry(Std_Frame, textvariable=self.stdIdVar, bd=4, relief=SUNKEN, width=31, font="arial 18 bold").grid(row=1, columnspan=4, pady=10)

        # First Name
        firstname_lbl = Label(Std_Frame, text="First Name", font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=10, sticky='w')
        firstname_entry = Entry(Std_Frame, textvariable=self.firstnameVar, bd=4, relief=GROOVE, width=18, font="arial 15").grid(row=2, column=1, pady=10)

        # Last Name
        lastname_lbl = Label(Std_Frame, text="Last Name", font=("times new roman", 15, "bold")).grid(row=2, column=2, padx=20, pady=10, sticky='w')
        lastname_entry = Entry(Std_Frame, textvariable=self.lastnameVar, bd=4, relief=GROOVE, width=18, font="arial 15").grid(row=2, column=3, pady=10)

        # Challan Number
        challan_lbl = Label(Std_Frame, text="Challan No.", font=("times new roman", 15, "bold")).grid(row=3, column=0, padx=20, pady=10, sticky='w')
        challan_entry = Entry(Std_Frame, textvariable=self.challanVar, bd=4, relief=GROOVE, width=18, font="arial 15").grid(row=3, column=1, pady=10)

        # DOB (dd/mm/yyyy)
        dob_lbl = Label(Std_Frame, text="D.O.B", font=("times new roman", 15, "bold")).grid(row=3, column=2, padx=20, pady=10, sticky='w')
        dob_entry = Entry(Std_Frame, textvariable=self.dobVar, bd=4, relief=GROOVE, width=18, font="arial 14").grid(row=3, column=3, pady=10)

        # Email
        email_lbl = Label(Std_Frame, text="Email", font=("times new roman", 15, "bold")).grid(row=4, column=0, padx=20, pady=10, sticky='w')
        email_entry = Entry(Std_Frame, textvariable=self.emailVar, bd=4, relief=GROOVE, width=18, font="arial 15").grid(row=4, column=1, pady=10)

        # Gender
        gender_lbl = Label(Std_Frame, text="Gender", font=("times new roman", 15, "bold")).grid(row=4, column=2, padx=20, pady=10, sticky='w')
        gender_combo = ttk.Combobox(Std_Frame, textvariable=self.genderVar, state="readonly", width=17, font="arial 14")
        gender_combo.grid(row=4, column=3, pady=10)
        gender_combo['values'] = ("Male", "Female", "Other")

        # City
        city_lbl = Label(Std_Frame, text="City", font=("times new roman", 15, "bold")).grid(row=5, column=0, padx=20, pady=10, sticky='w')
        city_entry = Entry(Std_Frame, textvariable=self.cityVar, bd=4, relief=GROOVE, width=18, font="arial 15").grid(row=5, column=1, pady=10)

        # Course
        course_lbl = Label(Std_Frame, text="Course", font=("times new roman", 15, "bold")).grid(row=5, column=2, padx=20, pady=10, sticky='w')
        course_combo = ttk.Combobox(Std_Frame, textvariable=self.courseVar, state="readonly", width=17, font="arial 14")
        course_combo.grid(row=5, column=3, pady=10)
        course_combo['values'] = ("BCA", "B.Sc", "B.Tech CS", "MCA", "M.Sc", "M.Tech CS")

        # State
        state_lbl = Label(Std_Frame, text="State", font=("times new roman", 15, "bold")).grid(row=6, column=0, padx=20, pady=10, sticky='w')
        state_entry = Entry(Std_Frame, textvariable=self.stateVar, bd=4, relief=GROOVE, width=18, font="arial 15").grid(row=6, column=1, pady=10)

        # ID Proof
        idproof_lbl = Label(Std_Frame, text="ID Proof", font=("times new roman", 15, "bold")).grid(row=6, column=2, padx=20, pady=10, sticky='w')
        idproof_combo = ttk.Combobox(Std_Frame, textvariable=self.idproofVar, state="readonly", width=17, font="arial 14")
        idproof_combo.grid(row=6, column=3, pady=10)
        idproof_combo['values'] = ("Aadhar Card", "Voter ID", "PAN Card", "Driving License", "Student ID Card")

        # Contact Number
        contact_lbl = Label(Std_Frame, text="Contact Number", font=("times new roman", 15, "bold")).grid(row=7, column=0, padx=20, pady=10, sticky='w')
        contact_entry = Entry(Std_Frame, textvariable=self.contactVar, bd=4, relief=GROOVE, width=18, font="arial 15").grid(row=7, column=1, pady=10)

        # Payment Mode
        payment_lbl = Label(Std_Frame, text="Payment Mode", font=("times new roman", 15, "bold")).grid(row=7, column=2, padx=20, pady=10, sticky='w')
        payment_combo = ttk.Combobox(Std_Frame, textvariable=self.paymentVar, state="readonly", width=17, font="arial 14")
        payment_combo.grid(row=7, column=3, pady=10)
        payment_combo['values'] = ("Cash", "Internet Banking", "Debit Card", "Credit Card")

        # *************** Button Frame *************** #
        Button_Frame = Frame(self.root, bd=10, relief=GROOVE, bg="lightgrey")
        Button_Frame.place(x=200, y=580)

        save_button = Button(Button_Frame, text="Save", command=self.save, font=("times new roman", 15, "bold"), bd=5, width=12, bg="#BFC9CA", fg="black").grid(row=0, column=0, padx=10, pady=10)
        delete_button = Button(Button_Frame, text="Delete", command=self.delete, font=("times new roman", 15, "bold"), bd=5, width=12, bg="#BFC9CA", fg="black").grid(row=0, column=1, padx=10, pady=10)
        clear_button = Button(Button_Frame, text="Clear", command=self.clear, font=("times new roman", 15, "bold"), bd=5, width=12, bg="#BFC9CA", fg="black").grid(row=0, column=2, padx=10, pady=10)
        logout_button = Button(Button_Frame, text="Logout", command=self.logout, font=("times new roman", 15, "bold"), bd=5, width=12, bg="#BFC9CA", fg="black").grid(row=0, column=3, padx=10, pady=10)
        exit_button = Button(Button_Frame, text="Exit", command=self.exit, font=("times new roman", 15, "bold"), bd=5, width=12, bg="#BFC9CA", fg="black").grid(row=0, column=4, padx=10, pady=10)

        # *************** All Files Frame *************** #
        File_Frame = Frame(self.root, bd=10, relief=GROOVE)
        File_Frame.place(x=890, y=80, width=450, height=480)

        file_title = Label(File_Frame, text="All Files", font=("times new roman", 20, "bold"))
        file_title.pack(side=TOP, fill=X)
        scroll_y = Scrollbar(File_Frame, orient=VERTICAL)
        self.file_list = Listbox(File_Frame, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH, expand=1)
        self.show()
        self.file_list.bind("<ButtonRelease-1>", self.get_cursor)
        self.root.mainloop()

    def save(self):
        present = "no"
        if self.stdIdVar.get() == "":
            messagebox.showerror("Error", "Student ID must be required!!")
        else:
            file = os.listdir("E:/dell/Python/Temp/data")
            if len(file) > 0:
                for i in file:
                    if i.split('.')[0] == self.stdIdVar.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno("Update", "This file is already exists \nDo you want to update?")
                    if ask > 0:
                        self.saveas()
                        messagebox.showinfo("Success!", "Student Record has been updated successfully!!")
                        self.show()
                else:
                    self.saveas()
                    messagebox.showinfo("Saved!", "New Student Record has been inserted successfully!!")
                    self.show()
            else:
                self.saveas()
                messagebox.showinfo("Saved!", "Student Record has been inserted successfully!!")
                self.show()

    def saveas(self):
        file = open("E:/dell/Python/Temp/data/" + str(self.stdIdVar.get()) + ".txt", "w")
        file.write(
            str(self.stdIdVar.get()) + "," +
            str(self.firstnameVar.get()) + "," +
            str(self.lastnameVar.get()) + "," +
            str(self.challanVar.get()) + "," +
            str(self.dobVar.get()) + "," +
            str(self.emailVar.get()) + "," +
            str(self.genderVar.get()) + "," +
            str(self.cityVar.get()) + "," +
            str(self.courseVar.get()) + "," +
            str(self.stateVar.get()) + "," +
            str(self.idproofVar.get()) + "," +
            str(self.contactVar.get()) + "," +
            str(self.paymentVar.get()) + ","
        )
        file.close()

    def show(self):
        files = os.listdir("E:/dell/Python/Temp/data/")
        self.file_list.delete(0, END)
        if len(files) > 0:
            for file in files:
                self.file_list.insert(END, file)

    def get_cursor(self, event):
        data = self.file_list.curselection()
        file = open("E:/dell/Python/Temp/data/" + self.file_list.get(data))
        values = []
        for i in file:
            values = i.split(",")
        self.stdIdVar.set(values[0])
        self.firstnameVar.set(values[1])
        self.lastnameVar.set(values[2])
        self.challanVar.set(values[3])
        self.dobVar.set(values[4])
        self.emailVar.set(values[5])
        self.genderVar.set(values[6])
        self.cityVar.set(values[7])
        self.courseVar.set(values[8])
        self.stateVar.set(values[9])
        self.idproofVar.set(values[10])
        self.contactVar.set(values[11])
        self.paymentVar.set(values[12])

    def delete(self):
        present = "no"
        if self.stdIdVar.get() == "":
            messagebox.showerror("Error", "Student ID must be required!!")
        else:
            file = os.listdir("E:/dell/Python/Temp/data/")
            if len(file) > 0:
                for i in file:
                    if i.split('.')[0] == self.stdIdVar.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno("Delete", "Are you sure?")
                    if ask > 0:
                        os.remove("E:/dell/Python/Temp/data/" + self.stdIdVar.get() + ".txt")
                        messagebox.showinfo("Success!", "Deleted Successfully!!")
                        self.show()
                else:
                    messagebox.showerror("Error", "No such file exists!")

    def clear(self):
        self.stdIdVar.set("")
        self.firstnameVar.set("")
        self.lastnameVar.set("")
        self.challanVar.set("")
        self.dobVar.set("")
        self.emailVar.set("")
        self.genderVar.set("")
        self.cityVar.set("")
        self.courseVar.set("")
        self.stateVar.set("")
        self.idproofVar.set("")
        self.contactVar.set("")
        self.paymentVar.set("")

    def logout(self):
        ask = messagebox.askyesno("Logout?", "Are you sure?")
        if ask > 0:
            self.root.destroy()
            import admin

    def exit(self):
        ask = messagebox.askyesno("Exit", "Are you sure?")
        if ask > 0:
            self.root.destroy()