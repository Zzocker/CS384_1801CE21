from tkinter import *
import datastore
from tkinter import messagebox
import os
import queue
import threading
import csv

def show_password(var,entry):
    if var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

class login_system:
    def __init__(self,root):
        self.user_ds = datastore.user_datastore()
        self.root = root
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
        self.login_frame = login_frame
    def __login(self):
        res  = self.user_ds.check_cred(self.e_roll.get(),self.e_pass.get())
        if res.get("success") == False:
            messagebox.showerror("Error",res.get("msg"))
        else:
            user = self.user_ds.get_user(self.e_roll.get()).get("data")
            self.login_frame.destroy()
            quiz(root,user)
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

class quiz:
    def __init__(self,root,user):
        self.roll = user[0]
        self.user = user
        self.root = root
        f = Frame(root, height=1080, width=1920, bg="azure", relief="ridge")
        f.pack()
        Label(f, text="Which Quiz You Want Give?".format(user[2]), fg="red" ,bg="azure", font=("Helvetica", 30, "bold italic underline")).place(
            x=420, y=175)
        ht =  220
        selected_quiz=StringVar(f)
        for filename in os.listdir("./quiz_wise_questions"):
            if filename.endswith(".csv"):
                Radiobutton(f,text=filename[:-4],variable=selected_quiz,value=filename,bg='azure',
                              font=("Times New Roman", 20)).place(x=520,y=ht)
                ht+=40
        Button(f,text="OK",width=20, height=3, fg="royalblue4", bg="lavender",
                        font=("Helvetica", 10, "bold italic"),command=lambda: [f.destroy(),self.__start_quiz(selected_quiz.get())]).place(x=520,y=ht)
    def __start_quiz(self,filename):
        self.q_ds = datastore.quiz_datastore(filename).get_quiz()
        if self.q_ds.get("valid")== False:
            messagebox.showerror("Error","Empty Quiz")
            quiz(self.root,self.user)
        else:
            self.filename = filename
            self.user_mark_ds = datastore.users_marks_datastore()
        #################################################
            info_frame = Frame(self.root, height=340, width=1920, bg="azure", relief="ridge",bd=20)
            info_frame.place(x=0,y=0)
            Label(info_frame, text="Time Remaining",bg="azure", font=("Helvetica", 48, "bold")).place(
                x=10, y=10)
            self.timer_lb = Label(info_frame,text="",font=("Helvetica",48),fg="green",bg="azure")
            self.timer_lb.place(x=600,y=10)
            Label(info_frame, text="Name",bg="azure", font=("Helvetica", 48, "bold")).place(
                x=10, y=70)
            Label(info_frame,text=": "+self.user[2],font=("Helvetica",48),fg="green",bg="azure").place(x=600,y=70)
            Label(info_frame, text="Roll Number",bg="azure", font=("Helvetica", 48, "bold")).place(
                x=10, y=130)
            Label(info_frame,text=": "+self.user[0],font=("Helvetica",48),fg="green",bg="azure").place(x=600,y=130)
            Label(info_frame,text="*Unattempted Questions(Ctrl+Alt+U);Goto Question(Ctrl+Alt+G);\nFinal Submit(Ctrl+Alt+F);Export Database into CSV(Ctrl+Alt+E)",font=("Helvetica",28),fg="red",bg="azure").place(x=10,y=200)
            self.info_frame = info_frame
            ################################################# Timer
            self.max_timer = self.q_ds.get("q_time")
            self.channel = queue.Queue()
            thread = threading.Thread(target=self.timer)
            thread.start()
            #################################################
            self.response = {key:value for key,value in zip(self.q_ds.get("questions").keys(),[-1]*len(self.q_ds.get("questions")))}
            self.ques_frame = Frame(self.root,height=400, width=1920, bg="azure", relief="ridge",bd=20)
            self.ques_frame.place(x=0,y=350)
            self.q_num = 1
            self.ques = self.create_q(self.q_num)
            self.opts = self.create_options()
            self.display_q(self.q_num)
            self.next_btn = Button(self.ques_frame, text = "Save & Next",width=20, height=3, fg="royalblue4", bg="lavender",
                        font=("Helvetica", 10, "bold italic"),command = self.next)
            self.next_btn.place(x=300,y=250)
            ##################################################
            def goto_event(event):
                self.__go_to()
            self.root.bind("<Control_L><Alt_L><G>",goto_event)
            def submit_event(event):
                self.submit()
            self.root.bind("<Control_L><Alt_L><F>",submit_event)
            def unat_event(event):
                self.__get_unattem()
            self.root.bind("<Control_L><Alt_L><U>",unat_event)
            def export_event(event):
                self.__export_csv()
            self.root.bind("<Control_L><Alt_L><E>",export_event)
    def create_options(self):
        b_val = 0
        b = []
        self.opt_selected = IntVar()
        self.opt_selected.set(-1)
        ht = 50
        while b_val < 4:
            btn = Radiobutton(self.ques_frame, text="", variable=self.opt_selected, value=b_val + 1,bg="azure",font=("Helvetica", 20, "bold"))
            b.append(btn)
            btn.place(x=10,y=ht)
            ht+=50
            b_val = b_val + 1
        self.if_correct_label = Label(self.ques_frame,text="",bg="azure",font=("Helvetica", 20, "bold"))
        self.ng_marking = Label(self.ques_frame,text="",bg="azure",font=("Helvetica", 20, "bold"))
        self.is_com = Label(self.ques_frame,text="",bg="azure",font=("Helvetica", 20, "bold"))
        self.if_correct_label.place(x=600,y=50)
        self.ng_marking.place(x=600,y=100)
        self.is_com.place(x=600,y=150)
        return b
    def create_q(self,ques_num):
        q = self.q_ds.get("questions").get("{}".format(ques_num)).get("question")
        qLabel = Label(self.ques_frame, text=q,bg="azure",font=("Helvetica", 20, "bold"))
        qLabel.place(x=10,y=10)
        return qLabel
    def display_q(self, ques_num):
        b_val = 0
        q = self.q_ds.get("questions").get("{}".format(ques_num))
        self.ques['text'] = "Q"+str(ques_num) + ". " + q.get("question")
        for op in q.get("options"):
            self.opts[b_val]['text'] = op
            b_val = b_val + 1
        self.if_correct_label["text"]="Credits if Correct Option: {}".format(q.get("marks_correct_ans"))
        self.ng_marking["text"] = "Negative Marking: {}".format(q.get("marks_wrong_ans"))
        self.is_com["text"] = "Is compulsory: {}".format(q.get("compulsory"))
    def timer(self):
            min,sec  = divmod(self.max_timer,60)
            self.timer_lb["text"] = ': {:02d}:{:02d}'.format(min, sec)
            if self.max_timer == 0:
                self.channel.put("Stop")
                print("time out")
                self.end_quiz()
                self.result_lb["text"]="Time Out! Here The Result"
                return
            self.timer_lb.after(1000,self.timer)
            self.max_timer-=1
    def next(self):
        if self.q_num >= len(self.q_ds.get("questions")):
            messagebox.showwarning("Warning", "You are at the End.\nPress Ctrl+Alt+F to proceed")
        else:
            self.response["{}".format(self.q_num)]=self.opt_selected.get()
            self.q_num+=1
            self.opt_selected.set(self.response["{}".format(self.q_num)])
            self.display_q(self.q_num)
    def submit(self):
        self.response["{}".format(self.q_num)]=self.opt_selected.get()
        self.end_quiz()
    def end_quiz(self):
        self.ques_frame.destroy()
        self.info_frame.destroy()
        result = self.check_quiz()
        result_frame = Frame(self.root, height=1080, width=1920, bg="azure", relief="ridge",bd=20)
        result_frame.place(x=0,y=0)
        self.result_lb = Label(result_frame, text = "Quiz Submitted! Here The Result",bg="azure",fg="red", font=("Helvetica", 48, "bold"))
        self.result_lb.grid(row=0,sticky=W)
        Label(result_frame, text = "Total Quiz Questions: ",bg="azure", font=("Helvetica", 40, "bold")).grid(row = 1, sticky = W)
        Label(result_frame, text = result.get("total_ques"),bg="azure", font=("Helvetica", 40, "bold")).grid(row = 1, column = 1)
        Label(result_frame, text = "Total Quiz Questions Attempted: ",bg="azure", font=("Helvetica", 40, "bold")).grid(row = 2, sticky = W)
        Label(result_frame, text = result.get("total_attemp"),bg="azure", font=("Helvetica", 40, "bold")).grid(row = 2, column = 1)
        Label(result_frame, text = "Total Correct Questions: ",bg="azure", font=("Helvetica", 40, "bold")).grid(row = 3, sticky = W)
        Label(result_frame, text = result.get("total_Correct"),bg="azure", font=("Helvetica", 40, "bold")).grid(row = 3, column = 1)
        Label(result_frame, text = "Total Wrong Questions: ",bg="azure", font=("Helvetica", 40, "bold")).grid(row = 4, sticky = W)
        Label(result_frame, text = result.get("total_wrong"),bg="azure", font=("Helvetica", 40, "bold")).grid(row = 4, column = 1)
        Label(result_frame, text = "Total Marks Obtained: ",bg="azure", font=("Helvetica", 40, "bold")).grid(row = 5, sticky = W)
        Label(result_frame, text = result.get("total_marks"),bg="azure", font=("Helvetica", 40, "bold")).grid(row = 5, column = 1)
        Button(result_frame, text = "Ok",width=20, height=3, fg="royalblue4", bg="lavender",
                        font=("Helvetica", 10, "bold"),command = lambda:self.root.destroy()).grid(row=6,column=1)
    def check_quiz(self):
        total_marks = 0
        total_quiz_marks = 0
        total_unattempted = 0
        total_cor_ques = 0
        total_wrong_ques = 0
        out_fname = "individual_responses/{}_{}.csv".format(self.filename.split(".csv")[0],self.roll)
        writer = csv.DictWriter(open(out_fname,"w"),fieldnames=["ques_no","question","option1","option2","option3","option4","correct_option","marks_correct_ans","marks_wrong_ans","compulsory","marked_choice","Total","Legend"])
        writer.writeheader()
        for q in self.q_ds.get("questions").values():
            total = 0
            resp = self.response[q.get("ques_no")]
            q["marked_choice"]=resp
            if resp == -1:
                q["marked_choice"] = ""
                q["Legend"] = "Unattempted"
                total_unattempted+=1
            if resp == int(q.get("correct_option")):
                total=int(q.get("marks_correct_ans"))
                q["Legend"] = "Correct Choice"
                total_cor_ques+=1
            elif resp == -1 and q.get("compulsory")=="y":
                total=int(q.get("marks_wrong_ans"))
                q["Legend"] = "Wrong Choice"
                total_wrong_ques+=1
            elif resp != -1 and resp != int(q.get("correct_option")):
                total=int(q.get("marks_wrong_ans"))
                q["Legend"] = "Wrong Choice"
                total_wrong_ques+=1
            q["Total"]=total
            q["option1"] = q.get("options")[0]
            q["option2"] = q.get("options")[1]
            q["option3"] = q.get("options")[2]
            q["option4"] = q.get("options")[3]
            q.pop("options")
            writer.writerow(q)
            total_marks+=total
            total_quiz_marks+=int(q.get("marks_correct_ans"))
        self.user_mark_ds.update_mark(self.roll,self.filename,total_marks)
        temp_dct = {key:value for key,value in zip(writer.fieldnames,[""]*len(writer.fieldnames))}
        temp_dct["Total"] = total_marks
        temp_dct["Legend"] = "Marks Obtained"
        writer.writerow(temp_dct)
        temp_dct["Total"] = total_quiz_marks
        temp_dct["Legend"] = "Total Quiz Marks"
        writer.writerow(temp_dct)
        return {
            "total_ques"  : len(self.q_ds.get("questions")),
            "total_attemp" : len(self.q_ds.get("questions"))-total_unattempted,
            "total_Correct" : total_cor_ques,
            "total_wrong" : total_wrong_ques,
            "total_marks" : total_marks,
            "total_quiz_marks" : total_quiz_marks
        }

    def __go_to(self):
        temp_screen = Tk()
        temp_screen.title("Go To")
        f = Frame(temp_screen)
        f.pack()
        go_to_var = StringVar(f)
        go_to_var.set("")
        Label(f,text = 'Go To').grid(row=0,column=0)
        Entry(f,textvariable = go_to_var,bd = 5).grid(row=0,column=1)
        def jump():
            new_f = Frame(temp_screen)
            new_f.pack()
            if go_to_var.get() != "":
                in_q = go_to_var.get()
                go_to_var.set("")
                if in_q in [i for i in self.response.keys()]:
                    q = self.q_ds.get("questions").get("{}".format(in_q))
                    Label(f,text = "Q{}. {}".format(q.get("ques_no"),q.get("question"))).grid(sticky = W)
                    o_selected = IntVar(f)
                    o_selected.set(-1)
                    for i in range(4):
                        Radiobutton(f, text=q.get("options")[i], variable=o_selected, value=i+1).grid(sticky = W)
                def ano_belo():
                    self.response[q.get("ques_no")]=o_selected.get()
                    if q.get("ques_no") == str(self.q_num):
                        self.opt_selected.set(o_selected.get())
                Button(f,text="Save",command= ano_belo).grid(sticky = W)
        Button(f,text="Jump",command = jump).grid(row=1,column=0)
        Button(f,text="Close X",command=lambda :[temp_screen.destroy()]).grid(row=1,column=1)
    def __export_csv(self):
        self.user_mark_ds.export_csv()
        print("csv files exported")
    def __get_unattem(self):
        temp_screen = Tk()
        temp_screen.geometry("300x100")
        temp_screen.title("Unattempted Questions")
        for q in self.response:
            if self.response[q]==-1:
                Label(temp_screen,text="Q{}".format(q)).pack()
        Button(temp_screen,text="OK",command=lambda :  [temp_screen.destroy()]).pack()
root = Tk()
root.geometry("1350x750")
root.title("Quiz Portal")
root.config(bg="azure")
root.resizable(0,0)
login_system(root)
root.mainloop()