class student:
    stid=12
    stnm="Sanket"

    def myfunc(self):
        print("This is Student class")
    
    def getsum(self,a,b):
        print("Sum:",a+b)

#Objcet
st=student()
print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()
st.getsum(45,23)