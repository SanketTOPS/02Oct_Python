import re

mystr="This is Python!"

x=re.search('Python',mystr)
print(x)

if x:
    print("Match done!")
else:
    print("Error!")