from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
from threading import Thread
import main
import speech_recognition as sr
import re

class NavigationPanel:

    def __init__(self, u_id):

        self.u_id=u_id
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
        
        self.apps={"youtube": ("C:\\Users\\HP\\Desktop\\OpenSpeech\\you_icon.png", "open youtube"), "weather": ("C:\\Users\\HP\\Desktop\\OpenSpeech\\weather_icon.png", ("open weather")), "under construction": ("C:\\Users\\HP\\Desktop\\OpenSpeech\\os.png", None)}

        self.d=self.yp(25)
        self.c=self.xp(15)

        nx=self.xp(10)

        i=0

        self.app_icon=[]

        open_app = lambda f: (lambda p: self.open(f))

        for a in self.apps.keys():

            globals()["canvas"+str(i)]=Canvas(self.panel, height=self.d, width=self.c, bg="white")
            globals()["canvas"+str(i)].place(x=nx, y=self.yp(40))

            txt=a.capitalize()
            if len(txt) > 10:
                txt=txt[0:10]+".."
            globals()["canvas"+str(i)].create_text(self.cx(50), self.cy(85), text=txt, fill="#384E7E", font=("Candara", self.cy(15)), anchor="center")
            
            img=Image.open(self.apps[a][0])
            img = img.resize((self.cx(80), self.cy(65)), Image.ANTIALIAS)
            self.app_icon.append(ImageTk.PhotoImage(img))
            globals()["canvas"+str(i)].create_image(self.cx(50), self.cy(37.5), anchor='center', image=self.app_icon[i])

            globals()["canvas" + str(i)].bind("<Button-1>", open_app(a))
            
            nx+=self.xp(32.5)
            i=i+1

        self.panel.mainloop()

    def xp(self, a):
        return int(a / 100 * self.a)

    def yp(self, a):
        return int(a / 100 * self.b)

    def cx(self, a):

        return int((a * self.c) / 100)

    def cy(self, a):

        return int((a * self.d) / 100)

    def submit(self):

        inp=self.app_searched.get().lower()
        j=None
        for i in self.apps.keys():
            res=re.search(i, inp)
            if res is not None:
                j=i
                break
        if j is None:
            print("App Not Found")
        i=0
        for a in self.apps.keys():
            if a!=j:
                globals()["canvas"+str(i)].destroy()
            else:
                globals()["canvas"+str(i)].place(x=self.xp(10), y=self.yp(40))
            i=i+1
                

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

        if self.apps[a][1] is not None:
            main.find_keyword(self.apps[a][1])
            
if __name__ == "__main__":
    d = NavigationPanel(0)
