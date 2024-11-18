class studinfo:
    stid=12
    stnm="Sanket"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#calling via object
"""st=studinfo()
st.getdata()
st.stid=23
st.stnm="Ashok"
st.getdata()"""

#calling via instance
studinfo().getdata()
studinfo().stid=101
studinfo().stnm="Hitesh"
studinfo().getdata()