import csv
import re
import os

def course():
    # Read csv and process
    swticher = {
        "01" : "btech",
        "11" : "mtech",
        "12" : "msc",
        "21" : "phd"
    }
    base = "analytics/course"
    if os.path.isdir(base) == False:
        os.makedirs(base)
    # remove
    with open("./studentinfo_cs384.csv","r") as infile:
        pattern = re.compile("[0-9]{4}[a-zA-Z]{2}[0-9]{2}")
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None)
        for row in reader:
            if re.match(pattern,row.get("id")):
                roll_no =row.get("id")
                year = roll_no[:2]
                curs = swticher.get(roll_no[2:4])
                branch = roll_no[4:6].lower()
                foldername = "{}/{}/{}".format(base,branch,curs)
                try:
                    os.makedirs(foldername)
                except:
                    pass
                filename = "{}/{}_{}_{}.csv".format(foldername,year,branch,curs)
                with open(filename,"w") as f:
                    csv.DictWriter(f,fieldname).writeheader()
    
    with open("./studentinfo_cs384.csv","r") as infile:
        pattern = re.compile("[0-9]{4}[a-zA-Z]{2}[0-9]{2}")
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        misfile = open("{}/misc.csv".format(base),"w")
        miswritter = csv.DictWriter(misfile,fieldname)
        miswritter.writeheader()
        next(reader,None)
        for row in reader:
            if re.match(pattern,row.get("id")):
                roll_no =row.get("id")
                year = roll_no[:2]
                curs = swticher.get(roll_no[2:4])
                branch = roll_no[4:6].lower()
                foldername = "{}/{}/{}".format(base,branch,curs)
                try:
                    os.makedirs(foldername)
                except:
                    pass
                filename = "{}/{}_{}_{}.csv".format(foldername,year,branch,curs)
                with open(filename,"a") as f:
                    csv.DictWriter(f,fieldname).writerow(row)
            else:
                with open("{}/misc.csv".format(base),"a") as f:
                    csv.DictWriter(f,fieldname).writerow(row)

def country():
    # Read csv and process
    base = "analytics/country"
    if os.path.isdir(base) == False:
        os.makedirs(base)    
    # remove
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None) # skip header
        for row in reader:
            filename = "{}/{}.csv".format(base,row.get("country").lower())
            with open(filename,"w") as f:
                csv.DictWriter(f,fieldname).writeheader()
    
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None) # skip header
        for row in reader:
            filename = "{}/{}.csv".format(base,row.get("country").lower())
            with open(filename,"a") as f:
                csv.DictWriter(f,fieldname).writerow(row)

def email_domain_extract():
    # Read csv and process
    base = "analytics/email_domain"
    if os.path.isdir(base) == False:
        os.makedirs(base)
    # Remove
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None) # skip header
        for row in reader:
            email = row.get("email")
            domain = email.split("@")[1].split(".")[0]
            filename = "{}/{}.csv".format(base,domain)
            with open(filename,"w") as f:
                csv.DictWriter(f,fieldname).writeheader()
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None) # skip header
        for row in reader:
            email = row.get("email")
            domain = email.split("@")[1].split(".")[0]
            filename = "{}/{}.csv".format(base,domain)
            with open(filename,"a") as f:
                csv.DictWriter(f,fieldname).writerow(row)

def gender():
    # Read csv and process
    base = "analytics/gender"
    if os.path.isdir(base) == False:
        os.makedirs(base)
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        m = open("{}/male.csv".format(base),"w")
        mwritter = csv.DictWriter(m,fieldname)
        mwritter.writeheader()
        f= open("{}/female.csv".format(base),"w")
        fwritter = csv.DictWriter(f,fieldname)
        fwritter.writeheader()
        for row in reader:
            if row.get("gender").lower() == "male":
                mwritter.writerow(row)
            elif row.get("gender").lower() == "female":
                fwritter.writerow(row)

def dob():
    # Read csv and process
    base = "analytics/dob"
    if os.path.isdir(base) == False:
        os.makedirs(base)
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None)
        switters = {
            1 : csv.DictWriter(open("{}/bday_1995_1999.csv".format(base),"w"),fieldname),
            2 : csv.DictWriter(open("{}/bday_2000_2004.csv".format(base),"w"),fieldname),
            3 : csv.DictWriter(open("{}/bday_2005_2009.csv".format(base),"w"),fieldname),
            4 : csv.DictWriter(open("{}/bday_2010_2014.csv".format(base),"w"),fieldname),
            5 : csv.DictWriter(open("{}/bday_2015_2020.csv".format(base),"w"),fieldname)
        }
        for i in range(len(switters)):
            switters.get(i+1).writeheader()
        for row in reader:
            if re.match(re.compile("[0-9]{2}-[0-9]{2}-[0-9]{4}"),row.get("dob")):
                year = row.get("dob").split("-")[-1]
                case = -1
                if 1995 <= int(year) <= 1999:
                    case = 1
                elif 2000 <= int(year) <= 2004:
                    case = 2
                elif 2005 <= int(year) <= 2009:
                    case = 3
                elif 2010 <= int(year) <= 2014:
                    case = 4
                elif 2015 <= int(year) <= 2020:
                    case = 5
                if case != -1:
                    switters.get(case).writerow(row)

def state():
    # Read csv and process
    base = "analytics/state"
    if os.path.isdir(base) == False:
        os.makedirs(base)
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None) # skip header
        for row in reader:
            filename = "{}/{}.csv".format(base,row.get("state").lower())
            with open(filename,"w") as f:
                csv.DictWriter(f,fieldname).writeheader() 
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None) # skip header
        for row in reader:
            filename = "{}/{}.csv".format(base,row.get("state").lower())
            with open(filename,"a") as f:
                csv.DictWriter(f,fieldname).writerow(row)

def blood_group():
    # Read csv and process
    base = "analytics/blood_group"
    if os.path.isdir(base) == False:
        os.makedirs(base)
    # remove
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None) # skip header
        for row in reader:
            filename = "{}/{}.csv".format(base,row.get("blood_group").lower())
            with open(filename,"w") as f:
                csv.DictWriter(f,fieldname).writeheader()

    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None) # skip header
        for row in reader:
            filename = "{}/{}.csv".format(base,row.get("blood_group").lower())
            with open(filename,"a") as f:
                csv.DictWriter(f,fieldname).writerow(row)

# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    new_fieldname = ["id","first_name","last_name","country","email","gender","dob","blood_group","state"]
    new_file_list=  []
    base = "analytics"
    if os.path.isdir(base) == False:
        os.makedirs(base)
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        next(reader,None) # skip header
        new_file = open("{}/studentinfo_cs384_names_split.csv".format(base),"w")
        new_file_writer = csv.DictWriter(new_file,new_fieldname)
        new_file_writer.writeheader()
        for row in reader:
            full_name = row.get("full_name").split(" ")
            row["first_name"] = full_name[0]
            row["last_name"] = " ".join(full_name[1:])
            del row["full_name"]
            new_file_list.append(row)
            new_file_writer.writerow(row)
    def get_first_name(stu):
        return stu.get("first_name")
    new_file_list.sort(key=get_first_name)
    with open("{}/studentinfo_cs384_names_split_sorted_first_name.csv".format(base),"w") as outfile:
        writer = csv.DictWriter(outfile,new_fieldname)
        writer.writeheader()
        for value in new_file_list:
            writer.writerow(value)