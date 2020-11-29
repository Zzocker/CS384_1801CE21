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
    ###################################################
    # Part C : separating students and placing them in their respective branch's csv file (eg CS.csv) 
    for branch in students:
        branch_writer = csv.DictWriter(open("{}.csv".format(branch.upper()),"w"),["Roll","Name","Email"])
        branch_writer.writeheader()
        branch_writer.writerows(students[branch])
    ###################################################
    # Part D : Distributing students among groups (in-memory)
    allocation_dict = dict() # (branch : array of number student from this branch pressent each groups)
    for branch in sorted_stu:
        allocation_dict.setdefault(branch,[0] * number_of_groups) # init; 0 student in each group
    for branch in allocation_dict:
        each = stu_strength[branch]//number_of_groups
        stu_strength[branch]-=each*number_of_groups
        for i in range(number_of_groups):
            allocation_dict[branch][i]+=each # distributing floor(num_in_branch_stu/num_of_group) students in each groups
    current_group = 0 
    # distributing remaining students
    for branch in allocation_dict:
        while stu_strength[branch]>0:
            allocation_dict[branch][current_group]+=1
            stu_strength[branch]-=1
            current_group+=1
            current_group%=number_of_groups
    ###################################################
    # Part E : creating group csv files and filling them up with students
    branch_current_index = {key:value for key,value in zip(sorted_stu,[0]*number_of_groups)} # (branch : current index for group distributi)
    stats_grouping_writer = csv.DictWriter(open("stats_grouping.csv","w"),["group","total"]+sorted_stu) # stats_grouping_writer for writing stats into the csv file
    stats_grouping_writer.writeheader()
    for group in range(number_of_groups):
        group_writer = csv.DictWriter(open('Group_G{0:02d}.csv'.format(group+1),"w"),["Roll","Name","Email"])
        group_row=dict()
        group_row["group"] = 'Group_G{0:02d}.csv'.format(group+1)
        group_row["total"] = 0
        group_writer.writeheader()
        for branch in allocation_dict:
            group_writer.writerows(students[branch][branch_current_index[branch]:branch_current_index[branch]+allocation_dict[branch][group]])
            branch_current_index[branch]+=allocation_dict[branch][group]
            group_row[branch.upper()]=allocation_dict[branch][group]
            group_row["total"]+=allocation_dict[branch][group]
        stats_grouping_writer.writerow(group_row)

filename = "Btech_2020_master_data.csv"
branch_strength_filename = "branch_strength.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)