import csv
import os

def getreader():
    """
    returns csv reader
    """
    infile= open("./acad_res_stud_grades.csv")
    reader = csv.DictReader(infile)
    return reader

def clean():
    """
    removes 
    1. all csv files from grades folder
    2. misc.csv file
    """
    base = "./grades"
    for f in os.listdir(base):
        os.remove('{}/{}'.format(base,f))
    if os.path.isfile('misc.csv'):
        os.remove('./misc.csv')