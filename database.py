import sqlite3

def connection():
    con=sqlite3.connect("appointments.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS schedule(id INTEGER PRIMARY KEY,name TEXT,about TEXT,place TEXT,phone_number INTEGER,date INTEGER,time INTEGER)")
    con.commit()
    con.close()


def insert(name,about,place,phone_number,date,time):
    con=sqlite3.connect("appointments.db")
    cur=con.cursor()
    cur.execute("INSERT INTO schedule VALUES(NULL,?,?,?,?,?,?)",(name,about,place,phone_number,date,time))
    con.commit()
    con.close()

def view():
    con=sqlite3.connect("appointments.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM schedule")
    result=cur.fetchall()
    con.close()
    return result


def search(name=None,about=None,place=None,phone_number=0,date=None,time=None):
    con=sqlite3.connect("appointments.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM schedule WHERE name=? OR about=? OR place=? OR phone_number=? OR date=? OR time=?",(name,about,place,phone_number,date,time))
    result=cur.fetchall()
    con.close()
    return result

def delete(name=None,about=None,place=None,phone_number=0,date=None,time=None):
    con=sqlite3.connect("appointments.db")
    cur=con.cursor()
    cur.execute("DELETE FROM schedule WHERE name=? OR about=? OR place=? OR phone_number=? OR date=? OR time=?",(name,about,place,phone_number,date,time))
    con.commit()
    con.close()

def update(name,about,place,phone_number,date,time):
    con=sqlite3.connect("appointments.db")
    cur=con.cursor()
    cur.execute("UPDATE schedule SET  name=?, about=?, place=?, phone_number=?, date=?, time=?  WHERE name=? OR about=? OR place=?",(name,about,place,phone_number,date,time,name,about,place))
    con.commit()
    con.close()


