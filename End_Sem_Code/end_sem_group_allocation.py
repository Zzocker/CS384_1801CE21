import re
import csv

def group_allocation(filename, number_of_groups):
    ###################################################
    # Part A : reading Btech_2020_master_data.csv file and storing students inside dict
    # students (dict) with key as branch and values as array of students
    in_file = open(filename,'r')
    branch_strength_writer = csv.DictWriter(open(branch_strength_filename,"w"),[ 'BRANCHCODE', 'STRENGTH']) 
    branch_strength_writer.writeheader()
    students = dict() # dict of students with key as branch and values as array of students
    for row in csv.DictReader(in_file):
        raw_branch = re.findall(r'2001(\D+)',row["Roll"])
        if len(raw_branch) == 1:
            branch = raw_branch[0]
            students.setdefault(branch,[]).append(row)
    in_file.close() # closing opened file to save Memory
    ###################################################
    # Part B : writing strength of students presents in different branches inside branch_strength.csv file
    stu_strength = dict() # studente strength dict (branch : number of students)
    for key in students:
        stu_strength[key]=len(students[key])
    sorted_stu = sorted(stu_strength,key=lambda branch: (-stu_strength[branch],branch)) # sorted branch array
    for branch in sorted_stu:
        branch_strength_writer.writerow({
            'BRANCHCODE' :  branch.upper(),
            'STRENGTH' : stu_strength[branch]
    })

filename = "Btech_2020_master_data.csv"
branch_strength_filename = "branch_strength.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)