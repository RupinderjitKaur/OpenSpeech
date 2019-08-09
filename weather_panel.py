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

text_color = "black"


class WeatherPanel:

    def __init__(self, user, city):

        self.panel = Toplevel()

        self.a = self.panel.winfo_screenwidth()
        self.b = self.panel.winfo_screenheight()

        self.panel.geometry('{}x{}'.format(self.b, self.a))
        self.panel.title("Weather Report")
        self.panel.resizable(height=False, width=False)
        self.panel.state('zoomed')
        self.panel.config(bg="white")

        self.user = user
        self.city = city

        self.get_info()

        self.panel.mainloop()

    def get_info(self):

        Thread(target=self.search).start()

    def search(self):

        self.max_days = 7

        city = self.city.replace(" ", "+")

        forecast = """http://api.apixu.com/v1/forecast.json?key=2d9503c2989c4468977105906191707&q={}&days={}""".format(
            city, self.max_days)

        jdata = urllib.request.urlopen(forecast)
        data = str(jdata.read(), 'utf-8')
        self.w_dict = json.loads(data)

        current_time = datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
        current_time = str(current_time).split(" ")

        data = (self.user[0], self.city)

        main.add_weather_history(data)

        self.location = self.w_dict["location"]["name"] + ", " + self.w_dict["location"]["region"] + ", " + \
                        self.w_dict["location"]["country"]

        seconds = self.w_dict["location"]["localtime_epoch"]
        local_time = time.ctime(seconds)
        lt = local_time.split(" ")
        self.days = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday",
                     "Sat": "Saturday", "Sun": "Sunday"}
        print("lt: ", str(lt))
        day = self.days[lt[0]]
        print("day: ", day)
        if(lt[2]==' '):
            t=lt[4].split(":")
        else:
            t = lt[3].split(":")
        print(t)
        if int(t[0]) == 0:
            tm = "12." + str(t[1]) + " am"
        elif int(t[0]) < 12:
            tm = str(t[0]) + "." + str(t[1]) + " am"
        elif int(t[0]) == 12:
            tm = str(t[0]) + "." + str(t[1]) + " pm"
        else:
            tm = str(int(t[0]) - 12) + "." + str(t[1]) + " pm"
        self.time = day + ", " + tm

        self.weather = self.w_dict["current"]["condition"]["text"]

        img_url = "http:" + self.w_dict["current"]["condition"]["icon"]
        response = requests.get(img_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((130, 130), Image.ANTIALIAS)
        self.w_icon = ImageTk.PhotoImage(img)

        self.temp = (str(self.w_dict["current"]["temp_c"]) + str(chr(176)) + "C",
                     str(self.w_dict["current"]["temp_f"]) + str(chr(176)) + "F")
        self.feel = (str(self.w_dict["current"]["feelslike_c"]) + str(chr(176)) + "C", str(self.w_dict["current"]["feelslike_f"]) + str(chr(176)) + "F")

        self.precp = self.w_dict["current"]["precip_mm"]
        self.hmdt = self.w_dict["current"]["humidity"]
        self.wind = self.w_dict["current"]["wind_kph"]

        data = (
        self.location, self.time, self.weather, self.w_icon, self.temp, self.feel, self.precp, self.hmdt, self.wind)

        self.display(data)

    def xp(self, a):
        return int(a / 100 * self.a)

    def yp(self, a):
        return int(a / 100 * self.b)

    def display(self, data):

        self.t_unit = 0

        self.location_label = Label(self.panel, text=data[0], bg="white", fg="black", font=("Arial", self.yp(7)))
        self.location_label.place(x=self.xp(2), y=self.yp(4.2))

        self.time_label = Label(self.panel, text=data[1], bg="white", fg="black", font=("Arial", self.yp(4)))
        self.time_label.place(x=self.xp(2), y=self.yp(15))

        self.image_label = Label(self.panel, image=data[3], bg="white")
        self.image_label.place(x=self.xp(2), y=self.yp(25))

        self.weather_label = Label(self.panel, text=data[2], bg="white", fg="black", font=("Arial", self.yp(4)))
        self.weather_label.place(x=self.xp(2), y=self.yp(21.5))

        self.temp_label = Label(self.panel, text=data[4][self.t_unit], bg="white", fg="black",
                                font=("Arial", self.yp(6)))
        self.temp_label.place(x=self.xp(12), y=self.yp(28))

        if data[5] is not None:
            self.feel_label = Label(self.panel, text="Feels like " + str(data[5][self.t_unit]), bg="white", fg="black",
                                    font=("Arial", self.yp(4)))
            self.feel_label.place(x=self.xp(2.5), y=self.yp(40))

        self.precp_label = Label(self.panel, text="Precipitation: " + str(data[6]) + " mm", bg="white", fg="black",
                                 font=("Arial", self.yp(4)))
        self.precp_label.place(x=self.xp(65), y=self.yp(28))

        self.hmdt_label = Label(self.panel, text="Humidity: " + str(data[7]) + "%", bg="white", fg="black",
                                font=("Arial", self.yp(4)))
        self.hmdt_label.place(x=self.xp(65), y=self.yp(34))

        self.wind_label = Label(self.panel, text="Wind: " + str(data[8]) + " km/h", bg="white", fg="black",
                                font=("Arial", self.yp(4)))
        self.wind_label.place(x=self.xp(65), y=self.yp(40))

        nx = self.xp(1.5)

        self.icon = []
        self.sunset_icon = []
        self.sunrise_icon = []
        self.day_btn = []
        self.max = []
        self.min = []

        self.c = self.xp(13)
        self.d = self.yp(42)

        show_data = lambda f: (lambda p: self.show(f))

        for i in range(0, self.max_days):

            globals()["canvas" + str(i)] = Canvas(self.panel, height=self.d, width=self.c, bg="white")
            globals()["canvas" + str(i)].place(x=nx, y=self.yp(50))

            seconds = self.w_dict["forecast"]["forecastday"][i]["date_epoch"]
            local_time = time.ctime(seconds)
            lt = local_time.split(" ")

            globals()["canvas" + str(i)].create_text(self.cx(50), self.cy(9.65), text=lt[0], fill="black",
                                                     font=("Arial", self.cy(8.3)), anchor="center")

            img_url = "http:" + self.w_dict["forecast"]["forecastday"][i]["day"]["condition"]["icon"]
            response = requests.get(img_url)
            img_data = response.content
            image = Image.open(BytesIO(img_data))
            image = image.resize((self.cx(75.2), self.cy(41.34)), Image.ANTIALIAS)
            self.icon.append(ImageTk.PhotoImage(image))
            globals()["canvas" + str(i)].create_image(self.cx(50), self.cy(35.82), anchor='center', image=self.icon[i])

            weather_text1 = self.w_dict["forecast"]["forecastday"][i]["day"]["condition"]["text"]
            weather_text2 = " "
            if len(weather_text1) > 20:

                while len(weather_text1) > 20:
                    text = weather_text1.rsplit(" ", 1)
                    weather_text1 = text[0]
                    weather_text2 = " " + text[1] + weather_text2
                globals()["canvas" + str(i)].create_text(self.cx(50), self.cy(59.24), text=weather_text1, fill="black",
                                                         font=("Arial", self.cy(4.2)), anchor='center')
                globals()["canvas" + str(i)].create_text(self.cx(50), self.cy(64.75), text=weather_text2, fill="black",
                                                         font=("Arial", self.cy(4.2)), anchor='center')
                h = self.cy(5.51)

            else:
                globals()["canvas" + str(i)].create_text(self.cx(50), self.cy(59.24), text=weather_text1, fill="black",
                                                         font=("Arial", self.cy(4.2)), anchor='center')
                h = 0

            self.max.append((self.w_dict["forecast"]["forecastday"][i]["day"]["maxtemp_c"],
                             self.w_dict["forecast"]["forecastday"][i]["day"]["maxtemp_f"]))
            self.min.append((self.w_dict["forecast"]["forecastday"][i]["day"]["mintemp_c"],
                             self.w_dict["forecast"]["forecastday"][i]["day"]["mintemp_f"]))

            globals()["canvas" + str(i)].create_text(self.cx(50), h + self.cy(67.51),
                                                     text=str(self.max[i][self.t_unit]) + "   " + str(
                                                         self.min[i][self.t_unit]), fill="black",
                                                     font=("Arial", self.cy(5.51)), anchor='center')

            img = Image.open("C:\\Users\\HP\\Desktop\\OpenSpeech\\sunrise.png")
            img = img.resize((self.cx(17.6), self.cy(6.89)), Image.ANTIALIAS)
            self.sunrise_icon.append(ImageTk.PhotoImage(img))
            globals()["canvas" + str(i)].create_image(self.cx(10.01), h + self.cy(74.12), anchor='nw',
                                                      image=self.sunrise_icon[i])

            globals()["canvas" + str(i)].create_text(self.cx(32.56), h + self.cy(75.78),
                                                     text=self.w_dict["forecast"]["forecastday"][i]["astro"]["sunrise"],
                                                     fill="black", font=("Arial", self.cy(4.2)), anchor='nw')

            img = Image.open("C:\\Users\\HP\\Desktop\\OpenSpeech\\sunset.png")
            img = img.resize((self.cx(17.6), self.cy(6.89)), Image.ANTIALIAS)
            self.sunset_icon.append(ImageTk.PhotoImage(img))
            globals()["canvas" + str(i)].create_image(self.cx(10.01), h + self.cy(82.3), anchor='nw',
                                                      image=self.sunset_icon[i])

            globals()["canvas" + str(i)].create_text(self.cx(32.56), h + self.cy(82.67),
                                                     text=self.w_dict["forecast"]["forecastday"][i]["astro"]["sunset"],
                                                     fill="black", font=("Arial", self.cy(4.2)), anchor='nw')
            globals()["canvas" + str(i)].bind("<Button-1>", show_data(i))
            nx += self.xp(14)

    def celsius(self):

        self.t_unit = 0

    def farhenheit(self):

        self.t_unit = 1
        # self.temp_label["text"]

    def cx(self, a):

        return int((a * self.c) / 100)

    def cy(self, a):

        return int((a * self.d) / 100)

    def show(self, i):

        if i == 0:
            data = (self.time, self.weather, self.w_icon, self.temp, self.feel, self.precp, self.hmdt, self.wind)

        else:

            seconds = self.w_dict["forecast"]["forecastday"][i]["date_epoch"]
            local_time = time.ctime(seconds)
            lt = local_time.split(" ")
            day = self.days[lt[0]]

            weather = self.w_dict["forecast"]["forecastday"][i]["day"]["condition"]["text"]

            temp = (str(self.w_dict["forecast"]["forecastday"][i]["day"]["avgtemp_c"])+str(chr(176))+ "C",
                     str(self.w_dict["forecast"]["forecastday"][i]["day"]["avgtemp_f"])+str(chr(176))+ "F")

            precp = self.w_dict["forecast"]["forecastday"][i]["day"]["totalprecip_mm"]
            hmdt = self.w_dict["forecast"]["forecastday"][i]["day"]["avgtemp_c"]
            wind = self.w_dict["forecast"]["forecastday"][i]["day"]["maxwind_kph"]

            data = (day, weather, self.icon[i], temp, None, precp, hmdt, wind)

        self.time_label["text"] = data[0]
        self.weather_label["text"] = data[1]
        self.image_label["image"] = data[2]
        self.temp_label["text"] = data[3][0]

        if data[4] is not None:
            self.feel_label["text"] = "Feels like " + str(data[4][self.t_unit])
        else:
            self.feel_label["text"] = ""

        self.precp_label["text"] = "Precipitation: " + str(data[5]) + " mm"
        self.hmdt_label["text"] = "Humidity: " + str(data[6]) + "%"
        self.wind_label["text"] = "Wind: " + str(data[7]) + " km/h"



if __name__ == "__main__":
    d = WeatherPanel(0, "Jalandhar")
