import random

"""class bank:
    def __init__(self):
        otp=random.randint(1111,9999)
        print(otp)    

b=bank()"""

class bank:
    def __init__(self,otp):
        print(otp)

otp=random.randint(1111,9999)
b=bank(otp)