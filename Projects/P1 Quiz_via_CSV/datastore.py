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
    
