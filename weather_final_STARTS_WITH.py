# region Links
# https://www.youtube.com/watch?v=xKukOMtPWwk
# STARTS WITH   https://stackoverflow.com/questions/14257717/python-beautifulsoup-wildcard-attribute-id-search/14257743
# cursors  https://stackoverflow.com/questions/45184462/how-do-i-change-my-cursor-to-a-hand-only-when-it-is-hovering-over-a-label
# Google   https://www.geeksforgeeks.org/how-to-extract-weather-data-from-google-in-python/
# endregion Links

# region Imports
# from subprocess import check_call

import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label
from PIL import ImageTk, Image
from webbrowser import open_new
import os
os.system('cls')

# endregion Imports

# region Functions


def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    locationLabel['text'] = soup.find(
        'h1', class_=lambda L: L and L.startswith('CurrentConditions--location--')).text
    # locationLabel['text'] = soup.find(
    #     'h1', class_=lambda L: L and L.startswith('CurrentConditions--location--')).text
    locationLabel['text'] = "Ocala, FL  (34482)"

    temperatureLabel['text'] = soup.find(
        'span', class_=lambda L: L and L.startswith('CurrentConditions--tempValue--')).text

    time = soup.find('div', class_=lambda L: L and L.startswith(
        'CurrentConditions--timestamp--')).text

    weatherPredictionLabel['text'] = soup.find(
        'div', class_=lambda L: L and L.startswith('CurrentConditions--phraseValue--')).text + " " + time

    chanceOfRainLabel['text'] = soup.find(
        'div', class_=lambda L: L and L.startswith('CurrentConditions--precipValue--')).text

    master.after(60000, getWeather)
    master.update()


def openWeather_com(event):
    open_new(url)
    getWeather()


# endregion Functions

# region Weather URL
# url = "https://weather.com/en-IN/weather/today/l/c1fdfe2faebb2ccb5a78b819603546132468abbe5fd6c1a7063c0722438b5446"
url = r"https://weather.com/en-IN/weather/today/l/c1fdfe2faebb2ccb5a78b819603546132468abbe5fd6c1a7063c0722438b5446?par=google&temp=f"

# endregion Weather URL

# region root Tkinter window
master = Tk()
master.title("Weather in Ocala (34482)")
master.configure(background='white', highlightthickness=2)
master.iconbitmap('weather_icon.ico')

img = Image.open('weather_icon.png').resize((150, 150))
img = ImageTk.PhotoImage(img)
master.resizable(height=False, width=False)
# endregion root Tkinter window

# region GUI Define widgets
locationLabel = Label(master, font=("calibri bold", 28),
                      bg=("white"))
temperatureLabel = Label(master, font=("calibri bold", 70),
                         bg=("white"))
imgLabel = Label(master, image=img, bg='white')

weatherPredictionLabel = Label(master, font=(
                               "calibri bold", 24), bg='white')

chanceOfRainLabel = Label(master, font=(
                          "calibri bold", 18), bg='white',
                          fg='#0645AD', cursor='hand2')

# endregion GUI Define widgets

# region GUI Put Widget on Window
locationLabel.grid(row=0, sticky='NEW', padx=100)

temperatureLabel.grid(row=1, sticky='W', padx=40)

imgLabel.grid(row=1, sticky='E', pady=(20, 0))

weatherPredictionLabel.grid(row=2, sticky='EW')

chanceOfRainLabel.grid(row=3, sticky='EW', pady=(0, 20))

# endregion GUI Put Widget on Window

# region GUI Events & MISC
chanceOfRainLabel.bind("<Button-1>", openWeather_com)
getWeather()

# endregion GUI Events & MISC

master.mainloop()
