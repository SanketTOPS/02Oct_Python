fl=open('newtemp.txt','a')
n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter an ID:")
    nm=input("Enter a Name:")
    ct=input("Enter a City:")

    fl.write(f"\nID:{id}\nName:{nm}\nCity:{ct}\n")
    fl.write("=======================")