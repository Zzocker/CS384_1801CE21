import sqlite3
import utils
import csv
import re

class user_datastore:
    def __init__(self):
        self.conn = sqlite3.connect("project1_quiz_cs384")
        self.conn.execute('''CREATE TABLE IF NOT EXISTS project1_registration(
                username VARCHAR(10),
                password VARCHAR(45),
                name VARCHAR(45), 
                whatsapp_number VARCHAR(10)
        )''')
        self.conn.commit()
    def get_user(self,roll):
        found = True
        cur = self.conn.cursor()
        data = cur.execute('''SELECT * FROM project1_registration WHERE username=:roll''',{"roll":roll}).fetchone()
        if data == None:
            found = False
        cur.close()
        return {
            "found" : found,
            "data" : data
        }
    def register(self,roll,text_password,name,whatsapp_number):
        if self.get_user(roll)["found"]:
            return False
        self.conn.execute('''INSERT INTO project1_registration(username,password,name,whatsapp_number) VALUES(?,?,?,?)''',
        [
            (roll),
            (utils.genMD5(text_password)),
            (name),
            (whatsapp_number)
        ])
        self.conn.commit()
        return True
    def check_cred(self,roll,password):
        found = True
        msg = "Logged in"
        data = self.get_user(roll)
        if data.get("found") == False:
            found = False
            msg = "{} not found".format(roll)
        if found and data.get("data")[1] != utils.genMD5(password):
            msg = "invalid Password"
            found = False
        return {
            "success" : found,
            "msg" : msg
        }
    
class quiz_datastore:
    def __init__(self,filename):
        self.filename = "quiz_wise_questions/{}".format(filename)
    def get_quiz(self):
        in_file = open(self.filename,"r")
        reader = csv.DictReader(in_file)
        q_time = int(reader.fieldnames[-1].split("time=")[1][:-1])
        questions = dict()
        for row in reader:
            row.pop(reader.fieldnames[-1])
            options = [row.get("option1"),row.get("option2"),row.get("option3"),row.get("option4")]
            row.pop("option1")
            row.pop("option2")
            row.pop("option3")
            row.pop("option4")
            row["options"] = options
            questions[row.get("ques_no")] = row
        return {
            "questions" : questions,
            "q_time" : q_time*60
        }