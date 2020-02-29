import sqlite3 as sql
con = sql.connect('mydatabase.db')
def dbms_table(con):
    cobj = con.cursor()
    cobj.execute("CREATE TABLE EMPLOYEE(id int , name text , salary real)")
    cobj.execute("INSERT INTO EMPLOYEE VALUES(1,'Krishnanand', 100000)")

    con.commit()

dbms_table(con)
