students =[]


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name , "house":house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students , key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")

    # below is euqvalent to th get_name function so no worries

for student in sorted(students , key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")


# Learned about how to make the csv file and what it does and how it is 
# is similar to json file i just need more practice on dict