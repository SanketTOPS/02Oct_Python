class sanket:
    sid=0
    stech=""

    def s_getdata(self):
        self.sid=input("Enter Sanket's ID:")
        self.stech=input("Enter Sanket's Tech.:")

class ashok:
    aid=0
    atech=""

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.atech=input("Enter Ashok's Tech.:")

class hitesh:
    hid=0
    htech=""

    def h_getdata(self):
        self.hid=input("Enter Hitesh's ID:")
        self.htech=input("Enter Hitesh's Tech.:")

class tops(sanket,ashok,hitesh):
    def printdata(self):
        print("-------Sanket's Data------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Tech.:",self.stech)
        print("-------Ashok's Data------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Tech.:",self.atech)
        print("-------Hitesh's Data------")
        print("Hitesh's ID:",self.hid)
        print("Hitesh's Tech.:",self.htech)

tp=tops()
tp.s_getdata()
tp.a_getdata()
tp.h_getdata()
tp.printdata()