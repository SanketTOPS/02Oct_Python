import re

email=input("Enter an Email:")

#sanket@gmail.com
email_pattern="^[a-z0-9_.]+[@]+[a-z]+[\.]+[a-z]{2,4}$"

x=re.findall(email_pattern,email)
if x:
    print("Email address is valid!")
else:
    print("Error!Invalid Email address!")