import sqlite3 as sql 
con = sql.connect('mydb_ms.db')

def database(con):
    csr = con.cursor()
    csr.execute("CREATE TABLE tble(id num , name varchar , year int)")
    csr.execute("INSERT INTO tble VALUES(1,'Krishnanand', '2a')")
    csr.execute("INSERT INTO tble VALUES(2,'mohit', '1a')")
    csr.execute("INSERT INTO tble VALUES(3,'Aashish kumar', '1b')")
    csr.execute("INSERT INTO tble VALUES(4,'Prakash Jaiswal', '2a')")
    
    
    csr.execute("SELECT name FROM tble")
    [print (longitude) for longitude in csr.fetchall()]
    

    csr.execute("SELECT * FROM tble WHERE year = '1b'")
    [print (latitude) for latitude in csr.fetchall()]

    con.commit()

database(con)



