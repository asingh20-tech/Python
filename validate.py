# https://docs.python.org/3/library/re.html
import re

email = input("whats your email?").strip()

if re.search(r"^[a-zA-Z0-9_].+{@}.+\.edu$",email):
    print("Valid")
else :
    print("Invalid")   


    #  [] set of characters , [^] complementing the set