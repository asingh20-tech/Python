# docs.python.org/3/tutorial/classes.html
class Student:
    def __init__(self, name , house):
        self.name = name 
        self.house = house

def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name,house)
    return student


if __name__ == "__main__":
    main() 