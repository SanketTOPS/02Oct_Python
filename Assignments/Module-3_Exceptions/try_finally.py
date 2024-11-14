try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",a+b)
except Exception as e:
    print(e)
finally:
    print("This is finally block!")

#print("This is finally block!")