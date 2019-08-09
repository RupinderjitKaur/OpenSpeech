from foo import *
import mysql.connector
import re
user = []
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd = "",
        database = "search_engine"
    )

cursor = mydb.cursor()

def get_apps():
    cursor.execute("""SELECT `app_id`, `name` FROM `applications`""")
    return(cursor.fetchall())

def get_appicon(*app_id):
    cursor.execute("""SELECT `pic_path` FROM `application_icons` where `app_id`=%s""", app_id)
    return(cursor.fetchone())

def get_app_parameters(*app_id):
    cursor.execute("""SELECT `module`, `function` FROM `application_parameters` where `app_id`=%s""", app_id)
    return(cursor.fetchone())

def get_app_dictionary():
    data=get_apps()
    app_dict={}
    for i in data:
        path=get_appicon(i[0])
        prmts=get_app_parameters(i[0])
        app_dict[i[1]]=(path[0], prmts[0], prmts[1])
    return app_dict

def add_user(data):

    cursor.execute("""insert into `users` (`name`, `d_city`, `email`, `pswd`, `phone`, `allowed_status`) values (%s, %s, %s, %s, %s, %s)""", data)
    mydb.commit()

def add_admin(data):

    cursor.execute("""insert into `admins` (`name`, `email`, `password`) values (%s, %s, %s)""", data)
    mydb.commit()

def verify(data):

    cursor.execute("""SELECT * FROM `users` where email=%s and pswd=%s""", data)
    data=cursor.fetchone()
    if(data and data[6]!=1):
        return 'false'
    return( (data[0], data[1], data[2], data[3], data[4], data[5]) )

def verify_admin(data):

    cursor.execute("""SELECT `admin_id` FROM `admins` where email=%s and password=%s""", data)
    return(cursor.fetchone())

def get_admin(*admin_id):

    cursor.execute("""SELECT * FROM `admins` where admin_id=%s""", admin_id)
    return(cursor.fetchone())

def edit_admin(data):

    cursor.execute("""UPDATE `admins` set `name`=%s, `email`=%s, `password`=%s where `admin_id`=%s""", data)
    mydb.commit()

def add_weather_history(data):

    cursor.execute("""insert into `weather_history` (`u_id`, `city`) values (%s, %s)""", data)
    mydb.commit()

def add_youtube_history(data):

    cursor.execute("""insert into `youtube_history` (`u_id`, `video_id`, `title`, `img_url`, `published_at`) values (%s, %s, %s, %s, %s)""", data)
    mydb.commit()

def get_youtube_recents(*u_id):

    cursor.execute("""SELECT `video_id`, `title`, `img_url`, `published_at` from `youtube_history` where `u_id`=%s order by `created_at` desc limit 6""", u_id)
    return(cursor.fetchall())

def add_unknowns(data):

    cursor.execute("""insert into `unknown_keywords` (`user_id`, `keyword`) values (%s, %s)""", data)
    mydb.commit()

def get_unknown_keywords():
    
    cursor.execute("""SELECT * FROM `unknown_keywords""")
    return(cursor.fetchall())

def getkeywords():
    
    cursor.execute("""SELECT * FROM `keywords""")
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

    cursor.execute("""Select * from known""")
    words=cursor.fetchall()
    w=None
    for i in words:
        if int(i[1])==id_:
            res=re.search(i[4], inp)
            if res is not None:
                w=i
                break
            
    getattr(globals()[w[2]](), w[3])()
