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
                if os.path.isfile(filename) == False:
                    with open(filename,"w") as f:
                        csv.DictWriter(f,fieldname).writeheader()
                with open(filename,"a") as f:
                    csv.DictWriter(f,fieldname).writerow(row)
            else:
                with open("{}/misc.csv".format(base),"a") as f:
                    csv.DictWriter(f,fieldname).writerow(row)

def country():
    # Read csv and process
    base = "analytics/country"
    with open("./studentinfo_cs384.csv","r") as infile:
        reader = csv.DictReader(infile)
        fieldname = reader.fieldnames
        next(reader,None) # skip header
        for row in reader:
            filename = "{}/{}.csv".format(base,row.get("country").lower())
            if os.path.isfile(filename) == False:
                with opecn(filename,"w") as f:
                    csv.DictWriter(f,fieldname).writeheader()
            with open(filename,"a") as f:
                csv.DictWriter(f,fieldname).writerow(row)
def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
