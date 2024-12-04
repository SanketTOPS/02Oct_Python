import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='newdb')
    print("Database connected!")
except Exception as e:
    print(e)

cr=db.cursor()
#Table create
tbl_create="create table studinfo(id integer primary key auto_increment,name varchar(20),city varchar(20))"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('mitesh','baroda'),('nirav','surat'),('ashok','jamnagar'),('hitesh','rajkot')"
try:
    cr.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)
"""

#Update Data
"""update_data="update studinfo set name='prasiddh' where name='mitesh'"
try:
    cr.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where name='hitesh'"
try:
    cr.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

#Show data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i)
except Exception as e:
    print(e)
