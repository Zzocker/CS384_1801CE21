import csv
import os
import student_class as st

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

grader = {
    "AA":  10,
    "AB":  9,
    "BB":  8,
    "BC":  7,
    "CC":  6,
    "CD":  5,
    "DD":  4,
    "F" :  0,
    "I" :  0
}


def individual():
    """
    1. creates <roll_no>_individual.csv files inside grades folder
    2. fill those files with contents
    3. creats student_map (dict type) <roll_no> (Key) > st.Student(value)
    4. returns student_map
    """
    student_map = dict()
    reader = getreader()
    base = "./grades"
    filds = reader.fieldnames
    mis_writer = csv.DictWriter(open('./misc.csv','w'),filds)
    mis_writer.writeheader()
    header = ["Subject","Credits","Type","Grade","Sem"]
    for row in reader:
        roll = row.get("roll")
        ok = True
        for k in filds:
            if (k not in ['sl','timestamp','year']) and (row.get(k)=="" or row.get(k)==None):
                mis_writer.writerow(row)
                ok=False
                break
        if ok:
            individula_filename = '{}/{}_individual.csv'.format(base,roll)
            if os.path.isfile(individula_filename) == False:
                ind_writer =open(individula_filename,"w")
                ind_writer.write('Roll: {},,,,\n'.format(roll))
                ind_writer.write('Semester Wise Details,,,,\n')
                ind_writer.write(','.join(header))
                ind_writer.write('\n')
                ind_writer.close()
            infile = open(individula_filename,"a")
            writer = csv.DictWriter(infile,header)
            value = {
            "Subject" : row.get("sub_code"),
            "Credits" : row.get("total_credits"),
            "Type" : row.get("sub_type"),
            "Grade" : row.get("credit_obtained"),
            "Sem" : row.get("sem")
            }
            writer.writerow(value)
            infile.close()
            student_map.setdefault(roll,st.Student()).add_grade(int(row.get("sem")),int(row.get("total_credits")),grader.get(row.get("credit_obtained")))
    return student_map

def overall(student_map):
    """
    1. creates <roll_no>_overall.csv files inside grades folder
    2. fill those files with contents
    """
    base = "./grades"
    header = ["Semester","Semester Credits","Semester Credits Cleared","SPI","Total Credits","Total Credits Cleared","CPI"]
    for roll in student_map:
        overall_filename = '{}/{}_overall.csv'.format(base,roll)
        infile = open(overall_filename,"w")
        infile.write('Roll: {},,,,,,\n'.format(roll))
        infile.write(','.join(header))
        infile.write('\n')
        writer = csv.DictWriter(infile,header)
        student = student_map.get(roll)
        for sem in range(1,student.get_current_sem()+1):
            value = {
                "Semester" : sem,
                "Semester Credits" : student.get_sem_total_credits(sem),
                "Semester Credits Cleared" : student.get_sem_total_credits(sem),
                "SPI" : '{:.2f}'.format(student.get_spi(sem)),
                "Total Credits" : student.get_total_credit(sem),
                "Total Credits Cleared" : student.get_total_credit(sem),
                "CPI" : '{:.2f}'.format(student.get_cpi(sem))
            }
            writer.writerow(value)
        infile.close()

if __name__ == "__main__":
    clean()
    overall(individual())