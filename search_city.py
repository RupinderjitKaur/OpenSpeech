from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import weather_panel as wp

class SearchPanel:

    def __init__(self, user, theme):

        self.panel=Toplevel()

        self.w = self.panel.winfo_screenwidth()
        self.h = self.panel.winfo_screenheight()

        self.panel.geometry('{}x{}'.format(self.w, self.h))
        self.panel.title("Search City Weather")
        self.panel.resizable(height=False,width=False)
        self.panel.state('zoomed')

        self.canvas = Canvas(self.panel, height=self.h, width=self.w)
        self.canvas.place(x=0,y=0)
        
        self.bckg=ImageTk.PhotoImage(file="themebckg.jpg")
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg)
        
        self.canvas.create_text(self.xp(50), self.yp(15), text="Please Enter the Name of the City" ,fill="black", font=('Candara', self.yp(6.95), "bold"))

        self.city=StringVar(self.canvas)
        self.city_field=Entry(self.canvas, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(5)), textvariable=self.city)
        self.city_field.place(x=self.xp(30), y=self.yp(30))

        self.listen_btn=Button(self.canvas, text="Listen", command=self.listen, bg="white", fg="black", activeforeground="red", font=('Candara', self.yp(5), "bold"))
        self.listen_btn.place(x=self.xp(32), y=self.yp(50))

        self.submit_btn=Button(self.canvas, text="Submit", command=self.submit, bg="white", fg="black", font=('Candara', self.yp(5), "bold"))
        self.submit_btn.place(x=self.xp(55), y=self.yp(50))
        
        self.panel.mainloop()

    def xp(self, a):
        return int(a/100*self.w)

    def yp(self, a):
        return int(a/100*self.h)

    def listen(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
                audio = r.listen(source, timeout=5, phrase_time_limit=2)
        try:    
            text = r.recognize_google(audio)
            self.city.set(text)
            self.submit()
        except:
            print("ERROR")

    def submit(self):

        if self.city.get()=='':
            self.city.set(user[2])
        d = wp.WeatherPanel(0, self.city.get(), 0) #(u_id, city, theme)

if __name__=="__main__":
    d = SearchPanel(0, 0)

#make the background and all font colours variable
