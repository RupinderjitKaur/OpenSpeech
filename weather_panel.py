from tkinter import *
import webbrowser
import urllib.request
import json
from PIL import Image, ImageTk
from io import BytesIO
from threading import Thread
import requests
import time
import datetime
import pytz
import main

text_color ="black"

class WeatherPanel:

    def __init__(self, u_id, city, theme):

        self.panel=Tk()
        
        self.a = self.panel.winfo_screenwidth()
        self.b = self.panel.winfo_screenheight()

        self.panel.geometry('{}x{}'.format(self.b, self.a))
        self.panel.title("Weather Report")
        self.panel.resizable(height=False,width=False)
        self.panel.state('zoomed')
        self.panel.config(bg="white")

        self.u_id=u_id
        self.city=city

        self.get_info()
        self.panel.bind("<Button-1>", self.show)
        self.panel.mainloop()

    def get_info(self):

        Thread(target=self.search).start()

    def search(self):

        self.max_days=7

        city=self.city.replace(" ", "+")

        forecast="""http://api.apixu.com/v1/forecast.json?key=2d9503c2989c4468977105906191707&q={}&days={}""".format(city, self.max_days)

        jdata=urllib.request.urlopen(forecast)
        data=str(jdata.read(), 'utf-8')
        self.w_dict=json.loads(data)
        
        current_time=datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
        current_time=str(current_time).split(" ")
        
        data=(self.u_id, self.city, current_time[0])
        
        #main.add_history(data)

        self.location=self.w_dict["location"]["name"]+", "+self.w_dict["location"]["region"]+", "+self.w_dict["location"]["country"]

        seconds=self.w_dict["location"]["localtime_epoch"]
        local_time=time.ctime(seconds)
        lt=local_time.split(" ")
        self.days={"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}
        day=self.days[lt[0]]
        t=lt[3].split(":")
        if int(t[0])==0:
            tm="12."+str(t[1])+" am"
        elif int(t[0])<12:
            tm=str(t[0])+"."+str(t[1])+" am"
        elif int(t[0])==12:
            tm=str(t[0])+"."+str(t[1])+" pm"
        else:
            tm=str(int(t[0])-12)+"."+str(t[1])+" pm"
        self.time=day+", "+tm

        self.weather=self.w_dict["current"]["condition"]["text"]

        img_url="http:"+self.w_dict["current"]["condition"]["icon"]
        response=requests.get(img_url)
        img_data=response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((130, 130), Image.ANTIALIAS)
        self.w_icon=ImageTk.PhotoImage(img)

        self.temp=(self.w_dict["current"]["temp_c"], self.w_dict["current"]["temp_f"])
        self.feel=(self.w_dict["current"]["feelslike_c"], self.w_dict["current"]["feelslike_f"])

        self.precp=self.w_dict["current"]["precip_mm"]
        self.hmdt=self.w_dict["current"]["humidity"]
        self.wind=self.w_dict["current"]["wind_kph"]

        data=(self.location, self.time, self.weather, self.w_icon, self.temp, self.feel, self.precp, self.hmdt, self.wind)
        
        self.display(data)
        
    def xp(self, a):
        return int(a/100*self.a)

    def yp(self, a):
        return int(a/100*self.b)

    def display(self, data):

        self.t_unit=0
        self.canvas = Canvas(self.panel, height=self.b, width=self.a, bg="blue")
        self.canvas.place(x=0,y=0)
        
        self.canvas.create_text(self.xp(2), self.yp(5), text=data[0], fill="black", font=("Arial", self.yp(7)),anchor='w')
        self.canvas.create_text(self.xp(2), self.yp(15), text=data[1], fill="black", font=("Arial", self.yp(4)),anchor='w')
        self.canvas.create_text(self.xp(2), self.yp(23), text=data[2], fill="black", font=("Arial", self.yp(4)),anchor='w')
        self.canvas.create_image(self.xp(5), self.yp(31), anchor='center', image=data[3])
        self.canvas.create_text(self.xp(10), self.yp(31), text=data[4][self.t_unit], fill="black", font=("Arial", self.yp(6)),anchor='w')
        
        if data[5] is not None:
            self.canvas.create_text(self.xp(2.5), self.yp(42), text="Feels like "+str(data[5][self.t_unit]), fill="black", font=("Arial", self.yp(4)),anchor='w')

        

        self.canvas.create_text(self.xp(60), self.yp(20), text="Precipitation: "+str(data[6])+"%", fill="black", font=("Arial", self.yp(4)),anchor='w')
        self.canvas.create_text(self.xp(60), self.yp(28), text="Humidity: "+str(data[7])+"%", fill="black", font=("Arial", self.yp(4)),anchor='w')
        self.canvas.create_text(self.xp(60), self.yp(36), text="Wind: "+str(data[8])+"km/h", fill="black", font=("Arial", self.yp(4)),anchor='w')

        nx=self.xp(1.5)
        
        self.icon=[]
        self.sunset_icon=[]
        self.sunrise_icon=[]
        self.day_btn=[]
        self.max=[]
        self.min=[]

        self.c=self.xp(13)
        self.d=self.yp(40)

        for i in range(0, self.max_days):

            globals()["canvas"+str(i)]=Canvas(self.canvas, height=self.d, width=self.c, bg="white")
            globals()["canvas"+str(i)].place(x=nx, y=self.yp(50))
            
            seconds=self.w_dict["forecast"]["forecastday"][i]["date_epoch"]
            local_time=time.ctime(seconds)
            lt=local_time.split(" ")

            globals()["canvas"+str(i)].create_text(60, 20, text=lt[0], fill="black", font=("Arial", 30), anchor="nw")
            
            img_url="http:"+self.w_dict["forecast"]["forecastday"][i]["day"]["condition"]["icon"]
            response=requests.get(img_url)
            img_data=response.content
            image = Image.open(BytesIO(img_data))
            image = image.resize((150, 150), Image.ANTIALIAS)
            self.icon.append(ImageTk.PhotoImage(image))
            globals()["canvas"+str(i)].create_image(15, 55, anchor='nw', image=self.icon[i])

            globals()["canvas"+str(i)].create_text(100, 220, text=self.w_dict["forecast"]["forecastday"][i]["day"]["condition"]["text"], fill="black", font=("Arial", 15), anchor='center')

            self.max.append((self.w_dict["forecast"]["forecastday"][i]["day"]["maxtemp_c"], self.w_dict["forecast"]["forecastday"][i]["day"]["maxtemp_f"]))
            self.min.append((self.w_dict["forecast"]["forecastday"][i]["day"]["mintemp_c"], self.w_dict["forecast"]["forecastday"][i]["day"]["mintemp_f"]))

            globals()["canvas"+str(i)].create_text(20, 245, text=str(self.max[i][self.t_unit])+"  "+str(self.min[i][self.t_unit]), fill="black", font=("Arial", 20), anchor='w')

            self.sunrise_icon.append(PhotoImage(file="C:\\Users\\HP\\Desktop\\OpenSpeech\\sunrise.png"))
            globals()["canvas"+str(i)].create_image(20, 270, anchor='nw', image=self.sunrise_icon[i])

            globals()["canvas"+str(i)].create_text(45, 275, text=self.w_dict["forecast"]["forecastday"][i]["astro"]["sunrise"], fill="black", font=("Arial", 15), anchor='w')

            self.sunset_icon.append(PhotoImage(file="C:\\Users\\HP\\Desktop\\OpenSpeech\\sunset.png"))
            globals()["canvas"+str(i)].create_image(20, 295, anchor='nw', image=self.sunset_icon[i])

            globals()["canvas"+str(i)].create_text(45, 300, text=self.w_dict["forecast"]["forecastday"][i]["astro"]["sunset"], fill="black", font=("Arial", 15), anchor='w')
            
            nx+=self.xp(14)

    def cx(self, a):      
        
        return int((a*self.c)/100)

    def cy(self, a):
        
        return int((a*self.d)/100)

    def show(self,e):

        self.canvas.destroy()

        x = self.panel.winfo_pointerx()
        y = self.panel.winfo_pointery()
        abs_coord_x = self.panel.winfo_pointerx() - self.panel.winfo_rootx()
        abs_coord_y = self.panel.winfo_pointery() - self.panel.winfo_rooty()
        i=-1
        if abs_coord_x>self.xp(1.5) and (abs_coord_y>self.yp(50) and abs_coord_y<self.yp(90)) and abs_coord_x<self.xp(98.5):
            i = abs_coord_x-self.xp(3)
            print("1: ",i)
            i = i//self.xp(self.xp(14))

        print("2: ",i)

        #i=2

        if i==0:
            data=(self.location, self.time, self.weather, self.w_icon, self.temp, self.feel, self.precp, self.hmdt, self.wind)

        elif i!=-1:
            
            seconds=self.w_dict["forecast"]["forecastday"][i]["date_epoch"]
            local_time=time.ctime(seconds)
            lt=local_time.split(" ")
            day=self.days[lt[0]]

            weather=self.w_dict["forecast"]["forecastday"][i]["day"]["condition"]["text"]

            temp=((self.w_dict["forecast"]["forecastday"][i]["day"]["avgtemp_c"], self.w_dict["forecast"]["forecastday"][i]["day"]["avgtemp_f"]))

            precp=self.w_dict["forecast"]["forecastday"][i]["day"]["totalprecip_mm"]
            hmdt=self.w_dict["forecast"]["forecastday"][i]["day"]["avgtemp_c"]
            wind=self.w_dict["forecast"]["forecastday"][i]["day"]["maxwind_kph"]

            data=(self.location, day, weather, self.icon[i], temp, None, precp, hmdt, wind)

        self.display(data)

if __name__=="__main__":
    d = WeatherPanel(0, "Jalandhar", 0)
