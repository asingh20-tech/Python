# docs.python.org/3/tutorial/classes.html

# to string in java __str__ in py

class Student:
    def __init__(self, name , house, patronus):
        # so with oop it helps us to make our own exceptions
        if not name:
            raise ValueError("Missing Name")
        # if house not in ["Gryffindor","Slytherin","RavenClaw","HufflePuff"]:
        #     raise ValueError("Invalid House"). <--no longer need this 
        
        self.name = name 
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} is {self.house}"
    # help in encapsulation and all that stuff
    @property #getter
    def house(self):
        return self._house
    
    @house.setter #setter
    def house(self,house):
        if house not in ["Gryffindor","Slytherin","RavenClaw","HufflePuff"]:
            raise ValueError("Invalid House")
        self._house= house



def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    student.house= "yoo yoo" 
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input ("Patronus : ")
    student = Student(name,house,patronus)
    return student

if __name__ == "__main__":
    main() 