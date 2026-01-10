# Method 1 if you dont want to us ethe csv lib

# students =[]


# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name , "house":home}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students , key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")

#     # below is euqvalent to th get_name function so no worries

# for student in sorted(students , key=lambda student: student["name"], reverse=True):
#     print(f"{student['name']} is in {student['house']}")


# # Learned about how to make the csv file and what it does and how it is 
# # is similar to json file i just need more practice on dict


# -------Method 2 ---------

import csv

students =[]

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"] , "home": row["home"]})

for student in sorted(students, key = lambda student:student["name"]):
    print(f"{student['name']}is from {student['home']}")
# we use dict reader becuase this will help us to oragnise the csv file in the spreadsheet manner
# and we will use this by making the column names on the top of the csv file