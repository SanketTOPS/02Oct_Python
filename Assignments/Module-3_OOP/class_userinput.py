class studinfo:
    stid:int
    stnm:str

    def getdata(self):
        self.stid=input("Enter an ID:")
        self.stnm=input("Enter a Name:")
    
    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

st=studinfo()
st.getdata()
st.printdata()