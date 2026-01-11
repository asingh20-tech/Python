import re

url = input("URL: ").strip()

if username := re.search(r"^(https?://)?(www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"username: {username.group(3)}")#or you can do (?:www\.) that just tells that you dont need to put group(3) you can put it group(1)
else :
    print("Invalid")    



# be careful about walrus operator := 
#learned about re.sub too its a substitute things we do 


