data=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    city=input("Enter your city:")
    data.append(city)

print(tuple(data))
