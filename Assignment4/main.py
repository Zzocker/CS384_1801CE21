import csv

def getreader():
    """
    returns csv reader
    """
    infile= open("./acad_res_stud_grades.csv")
    reader = csv.DictReader(infile)
    return reader