fl=open('temp.txt','w')

id=input("Enter an ID:")
name=input("Enter a Name:")
city=input("Enter a City:")

"""fl.write(id)
fl.write(name)
fl.write(city)"""

fl.write(f"ID:{id}\nName:{name}\nCity:{city}")