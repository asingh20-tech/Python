# https://docs.python.org/3/library/re.html
import re

email = input("whats your email?").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email, re.IGNORECASE):#re.IGNORECASE,re.MULTILINE,re.DOTALL
    print("Valid")
else :
    print("Invalid")   


    #  [] set of characters , [^] complementing the set
    # \d decimal digit , \s whitespace character, \w word charcater numbers and underscore or [a-zA-Z0-9_ ]
    # A|B either a or b ,, (...) a group  (?...) non-capturing version