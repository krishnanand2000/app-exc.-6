import sqlite3 as sql
con = sql.connect('newdbms69.db')
def database(con):
    csr = con.cursor()
    csr.execute("CREATE TABLE list(s_no int , name text)")
    data = [(1,"krishnanand"), (2, "mohit") , (3,"arunish Shekhar") , (4, "Shibin Koshy") , (5 , "sanjib ghosh")]
    csr.executemany("INSERT INTO list VALUES(?,?)",data)

    csr.execute("DELETE FROM list.name WHERE s_no = 5")
    
    csr.execute("UPDATE list SET name ='arunish' where s_no = 4")

    csr.execute("ALTER TABLE list ADD COLOUMN reg_no varchar(50)")

    csr.execute("SELECT * FROM list")
    [print (x) for x in csr.fetchall()]
    

    con.commit()
database(con)
