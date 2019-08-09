from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
from threading import Thread
import main
import speech_recognition as sr
import re
from foo import *

class NavigationPanel:

    def __init__(self):

        self.panel = Tk()

        self.a = self.panel.winfo_screenwidth()
        self.b = self.panel.winfo_screenheight()

        self.panel.geometry('{}x{}'.format(self.b, self.a))
        self.panel.title("Navigate")
        self.panel.resizable(height=False, width=False)
        self.panel.state('zoomed')

        self.canvas = Canvas(self.panel, height=self.b, width=self.a)
        self.canvas.place(x=0, y=0)

        im = Image.open("upanelbckg.jpg")
        self.bckg = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg)

        img=Image.open("city_mic.png")
        img = img.resize((self.xp(5), self.yp(15)), Image.ANTIALIAS)
        self.mic_pic = ImageTk.PhotoImage(img)
        self.mic_btn = Button(self.canvas, image=self.mic_pic, command=self.listen)
        self.mic_btn.place(x=self.xp(18), y=self.yp(5))

        self.app_searched = StringVar(self.canvas)
        self.search_field = Entry(self.canvas, bg="#FFFFFF", fg="#384E7E", font=("Candara", self.yp(3.5)), textvariable=self.app_searched)
        self.search_field.place(x=self.xp(25), y=self.yp(10))

        self.submit_btn=Button(self.canvas, text="Submit", command=self.submit, bg="white", fg="black", font=('Candara', self.yp(3.5), "bold"))
        self.submit_btn.place(x=self.xp(56), y=self.yp(8))
        
        self.apps=main.get_app_dictionary()

        self.d=self.yp(25)
        self.c=self.xp(15)
        
        self.app_icon=[]
        i=0
        for a in self.apps.keys():
            img=Image.open(self.apps[a][0])
            img = img.resize((self.cx(80), self.cy(65)), Image.ANTIALIAS)
            self.app_icon.append(ImageTk.PhotoImage(img))
        self.show_apps()

        self.panel.mainloop()

    def show_apps(self):

        self.flag=0

        nx=self.xp(8)

        i=0
        
        open_app = lambda f: (lambda p: self.open(f))

        for a in self.apps.keys():

            globals()["canvas"+str(i)]=Canvas(self.panel, height=self.d, width=self.c, bg="white")
            globals()["canvas"+str(i)].place(x=nx, y=self.yp(40))

            txt=a.capitalize()
            if len(txt) > 10:
                txt=txt[0:10]+".."
            globals()["canvas"+str(i)].create_text(self.cx(50), self.cy(85), text=txt, fill="#384E7E", font=("Candara", self.cy(15)), anchor="center")
            globals()["canvas"+str(i)].create_image(self.cx(50), self.cy(37.5), anchor='center', image=self.app_icon[i])
            globals()["canvas" + str(i)].bind("<Button-1>", open_app(a))
            
            nx+=self.xp(23)
            i=i+1

    def xp(self, a):
        return int(a / 100 * self.a)

    def yp(self, a):
        return int(a / 100 * self.b)

    def cx(self, a):

        return int((a * self.c) / 100)

    def cy(self, a):

        return int((a * self.d) / 100)

    def submit(self):
        
        self.flag=1
        i=0
        for a in self.apps.keys():
            globals()["canvas"+str(i)].destroy()
            i=i+1
            
        inp=self.app_searched.get().lower()
        j=None
        for i in self.apps.keys():
            res=re.search(i, inp)
            if res is not None:
                j=i
                break
        if j is None:
            tup = (main.user[0], self.app_searched.get())
            main.add_unknowns(tup)
            self.app_searched.set("App Not Found")
            self.show_apps()
            
        else:
            open_app = lambda f: (lambda p: self.open(f))
            globals()["canvas"+str(0)]=Canvas(self.panel, height=self.d, width=self.c, bg="white")
            globals()["canvas"+str(0)].place(x=self.xp(10), y=self.yp(40))

            txt=j.capitalize()
            if len(txt) > 10:
                txt=txt[0:10]+".."
            globals()["canvas"+str(0)].create_text(self.cx(50), self.cy(85), text=txt, fill="#384E7E", font=("Candara", self.cy(15)), anchor="center")
            
            globals()["img"+str(0)]=Image.open(self.apps[j][0])
            globals()["img"+str(0)] = globals()["img"+str(0)].resize((self.cx(80), self.cy(65)), Image.ANTIALIAS)
            globals()["img"+str(0)] = ImageTk.PhotoImage(globals()["img"+str(0)])
            globals()["canvas"+str(0)].create_image(self.cx(50), self.cy(37.5), anchor='center', image=globals()["img"+str(0)])
            globals()["canvas" + str(0)].bind("<Button-1>", open_app(j))
            
    def listen(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
                audio = r.listen(source, timeout=5, phrase_time_limit=2)
        try:    
            text = r.recognize_google(audio)
            self.app_searched.set(text)
            self.submit()
        except:
            print("ERROR")

    def open(self, a):
        if self.flag:
            globals()["canvas" + str(0)].destroy()
            self.show_apps()
        getattr(globals()[self.apps[a][1]](), self.apps[a][2])()
