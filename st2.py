import csv


name = input("whats your name ?")
home = input("whats your home ?")

with open("student2.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    # this fielname helps us to organise the csv file 
    writer.writerow({"home":home , "name": name})