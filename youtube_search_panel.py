from tkinter import *
import webbrowser
import urllib.request
import json
import requests
from PIL import Image,ImageTk
from io import BytesIO
from threading import Thread
import speech_recognition as sr

class YPanel:

    def __init__(self):

        self.panel=Tk()
        self.a = self.panel.winfo_screenwidth()
        self.b = self.panel.winfo_screenheight()
        self.c=self.xp(97)
        self.d=self.yp(11.57)

        self.panel.geometry('{}x{}'.format(self.b, self.a))
        self.panel.title("Youtube Search")
        self.panel.config(bg="#232323")
        self.panel.resizable(height=False,width=False)

        self.icon=PhotoImage(file="C:\\Users\\HP\\Desktop\\OpenSpeech\\you_icon.png")
        self.icon_label=Label(self.panel, image=self.icon, bg="#232323")
        self.icon_label.place(x=self.xp(1.9), y=self.yp(2.3))

        self.ask_label=Label(self.panel, text="YouTube", bg="#232323", fg="#E4E4E4", font=("Bahnschrift SemiBold Condensed", self.yp(4.6)))
        self.ask_label.place(x=self.xp(16.9), y=self.yp(2.31))

        self.video=StringVar(self.panel)
        self.vid_entry=Entry(self.panel, bg="#393939", fg="#E4E4E4", font=("Bahnschrift", self.yp(2.89)), textvariable=self.video)
        self.vid_entry.place(x=self.xp(17.2), y=self.yp(10.4))

        self.srcbtn=Button(self.panel, text="Search", fg="#E4E4E4", bg="#393939", command=self.search1, font=("Bahnschrift", self.yp(1.85)))
        self.srcbtn.place(x=self.xp(41), y=self.yp(10.53))

        self.mic_pic=PhotoImage(file="C:\\Users\\HP\\Desktop\\OpenSpeech\\mic-icon.png")
        self.srcbtn=Button(self.panel, image=self.mic_pic, command=self.record)
        self.srcbtn.place(x=self.xp(48.09), y=self.yp(4.05))

        self.panel.bind("<Button-1>", self.openvideo)
        self.panel.state('zoomed')
        
        self.panel.mainloop()

    def record(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
                print ('Say Something!')
                audio = r.listen(source,timeout=4,phrase_time_limit=2)

        try:    
            text = r.recognize_google(audio)
            print(text)
            self.video.set(text)
            self.search1()
        except:
            print("Error:")

    def xp(self, a):
        return int(a/100*self.a)

    def yp(self, a):
        return int(a/100*self.b)
    
    def search1(self):
        Thread(target=self.search).start()

    def search(self):

        mx_vid=6
    
        keyword = self.video.get().replace(" ", "+")
        print(keyword, "***")
        youtube = """
                https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={}&q={}&type=video&key=AIzaSyAr1-gR4vdWQn9ZbwAqjIBbU4Gp9mznnBo
        """.format(mx_vid,keyword)
        print(youtube)
        jdata = urllib.request.urlopen(youtube)
        data = str(jdata.read(),'utf-8')
        self.udict = json.loads(data)
        self.display()

    def display(self):

        mx_vid=6        
        h=self.yp(20.25)
        self.thmb=[]
        self.thumbnail=[]
        self.title=[]
        self.canvas=[]
        for i in range(mx_vid):
            img_url = self.udict["items"][i]["snippet"]["thumbnails"]["default"]["url"]
            response = requests.get(img_url)
            img_data = response.content

            globals()["tk_d"+str(i)]= (Canvas(self.panel, height=self.d, width=self.c, bg="#393939"))
            globals()["tk_d"+str(i)].place(x=self.xp(1.3), y=h)
            
            self.thmb.append(ImageTk.PhotoImage(Image.open(BytesIO(img_data))))
            #self.udict["items"][i]["snippet"]["thumbnails"]["default"]["url"]))
            globals()["tk_d"+str(i)].create_image(self.cx(0.67), self.cy(7), anchor='nw', image=self.thmb[i])

            globals()["tk_d"+str(i)].create_text(self.cx(10), self.cy(15), text=self.udict["items"][i]["snippet"]["title"], fill="#E4E4E4", font=("Bahnschrift", self.cy(20)),anchor='w')
            globals()["tk_d"+str(i)].create_text(self.cx(10), self.cy(50), text=self.udict["items"][i]["snippet"]["publishedAt"], fill="#E4E4E4", font=("Bahnschrift", self.cy(15)),anchor='w')

            h=h+self.cy(110)

    def cx(self, a):
        return int(a/100*self.c)

    def cy(self, a):
        return int(a/100*self.d)
    
    def openvideo(self, obj):
        mx_vid = 6
        x = self.panel.winfo_pointerx()
        y = self.panel.winfo_pointery()
        abs_coord_x = self.panel.winfo_pointerx() - self.panel.winfo_rootx()
        abs_coord_y = self.panel.winfo_pointery() - self.panel.winfo_rooty()
        if y>self.yp(20.25) and (abs_coord_x>self.xp(1.3) and abs_coord_x<self.xp(98.7) ):
            y = abs_coord_y-self.yp(20.25)
            y = y//self.cy(110)      
            webbrowser.open("https://www.youtube.com/watch?v="+self.udict["items"][y]["id"]["videoId"])
if __name__=="__main__":
    d = YPanel()
        
