from tkinter import *

class UPanel:

    def __init__(self):

        self.panel=Tk()

        self.panel.geometry(' x ')

        self.panel.title("Welcome User!!")
        self.w.resizable(height=False,width=False)

        self.bckg=PhotoImage(file="xxx.png")
        self.canvas = Canvas(self.w, height=xx, width=xx)
        self.canvas.create_image(0, 0, anchor='nw', image=self.bckg)
        self.canvas.place(x=0,y=0)

        self.x=20
        self.y=20

        ask()

        

        self.panel.mainloop()

    def ask(self):

        self.canvas.create_text(self.x, self.y, text="How can I help you?", fill="0E645A", font=('Bahnschrift SemiBold', 40))
        self.y=self.y+60

x=UPanel()
