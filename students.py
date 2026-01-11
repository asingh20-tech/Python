def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student [1]}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    return [name,house] # learned about the concept of tuple immutable 


if __name__ == "__main__":
    main() 