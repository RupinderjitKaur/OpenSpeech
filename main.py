from foo import *
import mysql.connector
import re

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd = "",
        database = "search_engine"
    )

cursor = mydb.cursor()

def add_user(data):

    cursor.execute("""insert into `users` (`name`, `d_city`, `email`, `pswd`, `phone`) values (%s, %s, %s, %s, %s)""", data)
    mydb.commit()

def verify(data):

    cursor.execute("""SELECT * FROM `users` where email=%s and pswd=%s""", data)
    return(cursor.fetchone())

def add_history(data):

    cursor.execute("""insert into `weather_history` (`u_id`, `city`, `created_at`) values (%s, %s, %s)""", data)
    mydb.commit()

def getkeywords():
    cursor.execute("SELECT * FROM `keywords")
    return(cursor.fetchall())

def find_keyword(inp):

    inp=inp.lower()
    keywords=getkeywords()
    id_=None
    for i in keywords:
        res=re.search(i[1], inp)
        if res is not None:
            id_=i[0]
            break    

    cursor.execute("Select * from known")
    words=cursor.fetchall()
    w=None
    for i in words:
        if int(i[1])==id_:
            res=re.search(i[4], inp)
            if res is not None:
                w=i
                break
            
    getattr(globals()[w[2]](), w[3])()
