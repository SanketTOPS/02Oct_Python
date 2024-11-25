import re

username=input("Enter an Username:")

unm_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattern,username)
print(x)
if x:
    print("Username is valid!")
else:
    print("Error!Invalid Username...")