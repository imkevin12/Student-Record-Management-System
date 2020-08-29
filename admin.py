from future.moves.tkinter import *
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Management System")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap('srms.ico')

        # *************** All Variables *************** #
        self.usernameVar = StringVar()
        self.passwordVar = StringVar()

        # *************** Login Freame *************** #
        F1 = Frame(self.root, bd=10, relief=GROOVE)
        F1.place(x=360, y=150, width=500, height=300)

        # Title
        title = Label(F1, text="Administration Login", font=("times new roman", 30, "bold")).grid(row=0, columnspan=2, pady=20)

        # Username
        username_lbl = Label(F1, text="Username", compound=LEFT, font=("times new roman", 20, "bold")).grid(row=1, column=0, padx=20, pady=10)
        username_entry = Entry(F1, textvariable=self.usernameVar, bd=5, relief=GROOVE, font=("", 15)).grid(row=1, column=1, padx=20, pady=10)

        # Password
        password_lbl = Label(F1, text="Passsord", compound=LEFT, font=("times new roman", 20, "bold")).grid(row=2, column=0, padx=20, pady=10)
        password_entry = Entry(F1, textvariable=self.passwordVar, bd=5, relief=GROOVE, show="*", font=("", 15)).grid(row=2, column=1, padx=20, pady=10)

        # Login Button
        btn = Button(F1, text="Login", command=self.login, width=10, font=("times new roman", 14, "bold"), bd=2, relief=GROOVE, bg="#BFC9CA", fg="black")
        btn.place(x=45, y=220)

        # Reset Button
        btn = Button(F1, text="Reset", command=self.reset, width=10, font=("times new roman", 14, "bold"), bd=2, relief=GROOVE, bg="#BFC9CA", fg="black")
        btn.place(x=185, y=220)

        # Exit Button
        btn = Button(F1, text="Exit", command=self.exit, width=10, font=("times new roman", 14, "bold"), bd=2, relief=GROOVE, bg="#BFC9CA", fg="black")
        btn.place(x=325, y=220)

    def login(self):
        if self.usernameVar.get()=="imkevin12" and self.passwordVar.get()=="12345":
            messagebox.showinfo("Success!", "Welcome to Kevin's File Based Student Record System!")
            self.root.destroy()
            import SRMS
            SRMS.Student()
        else:
            messagebox.showerror("Error!", "Invalid username or password!")

    def reset(self):
        self.usernameVar.set("")
        self.passwordVar.set("")

    def exit(self):
        option = messagebox.askyesno("Exit!", "Do you want to exit?")
        if option > 0:
            self.root.destroy()
        else:
            return


root = Tk()
obj = Login(root)
root.mainloop()