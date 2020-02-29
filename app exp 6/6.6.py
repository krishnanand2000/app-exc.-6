import sqlite3 as sql
con = sql.connect('dbmsxxxx.db')
def database(con):
    cobj = con.cursor()
    cobj.execute("CREATE TABLE tb1(id num , name text)")
    cobj.execute("CREATE TABLE tb2(id num , name text)")
    data1 = [(100 , "AASHISH") , (202 , "KRISHNANAND") , (6969 , "ARUNISH" ) , (9989 , "MOHIT")]
    cobj.executemany("INSERT INTO tb1 VALUES(?,?)" , data1)

    data2 = [(100 , "ASESHANAND ACHARYA") , (205 , "mayank") , (6968 , "ashutosh" ) , (9980 , "krish")]
    cobj.executemany("INSERT INTO tb2 VALUES(?,?)" , data2)

    cobj.execute("SELECT tb1.name ,tb2.name  FROM tb1,tb2 WHERE tb1.id = tb2.id")
    [print (x) for x in cobj.fetchall()]


    con.commit()
database(con)
