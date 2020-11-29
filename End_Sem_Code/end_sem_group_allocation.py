import re
import csv

def group_allocation(filename, number_of_groups):
    ###################################################
    # Part A : reading Btech_2020_master_data.csv file and storing students inside dict
    # students (dict) with key as branch and values as array of students
    in_file = open(filename,'r')
    branch_strength_writter = csv.DictWriter(open(branch_strength_filename,"w"),[ 'BRANCHCODE', 'STRENGTH']) 
    branch_strength_writter.writeheader()
    students = dict() # dict of students with key as branch and values as array of students
    for row in csv.DictReader(in_file):
        raw_branch = re.findall(r'2001(\D+)',row["Roll"])
        if len(raw_branch) == 1:
            branch = raw_branch[0]
            students.setdefault(branch,[]).append(row)
    in_file.close() # closing opened file to save Memory
    ###################################################
filename = "Btech_2020_master_data.csv"
branch_strength_filename = "branch_strength.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)