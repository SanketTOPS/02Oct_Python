import random
fl=open("newtemp.txt","r")

line=fl.read().splitlines()

print(random.choice(line))