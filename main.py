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
    print(w)
    print(w[2],w[3])
    getattr(globals()[w[2]](), w[3])()

find_keyword("open google")
