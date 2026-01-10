names = []
students =[]

def main():
    csv_arrangemnet()

def append_files():
        for _ in range(3):
            with open("names.txt","a") as file:
                name = input("whats your name ?")
                file.write(f"{name}\n")

def read_file():
        with open("names.txt","r") as file:
             
            #method 2 
            for line in sorted(file):
                 print("hello", line.rstrip())  
             
        #Method 1     
        #     lines= file.readlines()
        # for line in lines:
        #     print(f"hello,{line}",end="",sep=",") 

def csv_arrangemnet():
     with open ("student.csv") as file: 
          for line in file:
               first,last = line.rstrip().split(",")  
               student ={}
               student["name"] = first
               student["house"] = last
               students.append(student) 

for student in students:
     print(f"{student['first']},{student['last']}")                  

if __name__ == "__main__":
    main()    


     
          
