import sqlite3

try:
    db=sqlite3.connect("newdb.db") #create/connect a database
    print("Database connected!")
except Exception as e:
    print(e)

#Table Create
tbl_create="create table studinfo(id integer primary key autoincrement,name text,city text)"

try:
    db.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('mitesh','baroda'),('nirav','surat'),('ashok','jamnagar'),('hitesh','rajkot')"
try:
    db.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)
"""

#Update Data
"""update_data="update studinfo set name='prasiddh' where name='mitesh'"
try:
    db.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where name='hitesh'"
try:
    db.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

#Show data
cr=db.cursor()
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)
    """for i in data:
        print(i)"""
    for i in data:
        print(i[1])
except Exception as e:
    print(e)
    