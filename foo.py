import webbrowser
import youtube_search_panel as ysp
import search_city as sc
import main

class openbrowser:
    
    def __init__(self):
        pass

    def openyoutube(self):

        y=ysp.YPanel(main.user)

    def opengoogle(self):
        
        webbrowser.open("www.google.com")

class openapp:

    def __init__(self):
        pass

    def openweather(self):

        y=sc.SearchPanel(main.user)
