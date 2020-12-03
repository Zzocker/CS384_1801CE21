from tkinter import *
import datastore
from tkinter import messagebox

def show_password(var,entry):
    if var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

class login_system:
    def __init__(self,root):
        self.user_ds = datastore.user_datastore()
        login_frame = Frame(root, height=1080, width=1920, bg="azure", relief="ridge")
        login_frame.pack()
        ##################################################################################################
        Label(login_frame, text="LOGIN", fg="red" ,bg="azure", font=("Helvetica", 30, "bold italic underline")).place(
            x=420, y=175)
        Label(login_frame, text="Enter Roll: ", bg="azure", font=("Times New Roman", 20)).place(x=420,y=240)
        self.e_roll = Entry(login_frame, width=30)
        self.e_roll.place(x=620,y=250)
        Label(login_frame, text="Enter Password: ", bg="azure", font=("Times New Roman", 20)).place(x=420,y=290)
        self.e_pass = Entry(login_frame, width=30, show="*")
        self.e_pass.place(x=620,y=300)
        show_password_var = IntVar()
        Checkbutton(login_frame, text='Show Password', bg="azure", fg="royalblue4",
                                  font=("Helvetica", 10, "bold italic"), variable=show_password_var, onvalue=1,
                                  offvalue=0,command=lambda: show_password(show_password_var,self.e_pass)).place(x=615,y=330)
        ####################################################################################################
        Button(login_frame, text="Login", width=20, height=3, fg="royalblue4", bg="lavender",
                           font=("Helvetica", 10, "bold italic"),command=self.__login).place(x=620, y=360)
        Button(login_frame, text="Register", width=20, height=3, fg="royalblue4", bg="lavender",
                            font=("Helvetica", 10, "bold italic"),command=register_system).place(x=420, y=360)
    def __login(self):
        res  = self.user_ds.check_cred(self.e_roll.get(),self.e_pass.get())
        if res.get("success") == False:
            messagebox.showerror("Error",res.get("msg"))
        else:
            user = self.user_ds.get_user(self.e_roll.get()).get("data")
            print(user)
        pass

class register_system:
    def __init__(self):
        register_screen = Tk()
        self.user_ds = datastore.user_datastore()
        register_screen.geometry("675x375")
        register_screen.title("Registration")
        register_screen.config(bg="azure")
        register_screen.resizable(0,0)
        #################################################
        f = Frame(register_screen, height=720, width=980, bg="azure", relief="ridge")
        f.pack()
        #################################################
        Label(f, text="Register Yourself", bg="azure",font=("Helvetica", 30, "bold italic underline")).place(x=50, y=20)
        Label(f, text="Name : ", bg="azure", font=("Times New Roman", 20)).place(x=50,y=70)
        Label(f, text="Roll : ", bg="azure", font=("Times New Roman", 20)).place(x=50,y=120)
        Label(f, text="Whatsapp Number : ", bg="azure", font=("Times New Roman", 20)).place(x=50,y=170)
        Label(f, text="Password : ", bg="azure", font=("Times New Roman", 20)).place(x=50,y=220)
        self.e_name = Entry(f, width=30)
        self.e_roll = Entry(f, width=30)
        self.e_wh_num = Entry(f, width=30)
        self.e_pass = Entry(f, width=30,show="*")
        self.e_name.place(x=300,y=70)
        self.e_roll.place(x=300,y=120)
        self.e_wh_num.place(x=300,y=170)
        self.e_pass.place(x=300,y=220)
        show_password_var = IntVar(f)
        Checkbutton(f, text='Show Password', bg="azure", fg="royalblue4",
                                  font=("Helvetica", 10, "bold italic"), variable=show_password_var, onvalue=1,
                                  offvalue=0,command=lambda: show_password(show_password_var,self.e_pass)).place(x=295,y=250)
        Button(f, text="Register", width=20, height=3, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 10, "bold italic"), command=self.__register).place(x=50,y=280)
        Button(f, text="Return", width=20, height=3, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 10, "bold italic"), command=lambda:register_screen.destroy()).place(x=300,y=280)
        ###########################################################
        register_screen.mainloop()
    def __register(self):
        ok = self.user_ds.register(
            self.e_roll.get(),
            self.e_pass.get(),
            self.e_name.get(),
            self.e_wh_num.get()
        )
        if ok :
            messagebox.showinfo("Success","successfully registered")
        else:
            messagebox.showerror("Error","{} already exists".format(self.e_roll.get()))

root = Tk()
root.geometry("1350x750")
root.title("Quiz Portal")
root.config(bg="azure")
root.resizable(0,0)
login_system(root)
root.mainloop()