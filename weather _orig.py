# region Links
# https://www.youtube.com/watch?v=xKukOMtPWwk
# endregion Links

# region Imports
import sys
from subprocess import check_call
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
    location = soup.find(
        'h1', class_='CurrentConditions--location--2_osB').text
    temperature = soup.find(
        'span', class_='CurrentConditions--tempValue--1RYJJ').text
    weatherPrediction = soup.find('div',
                                  class_='CurrentConditions--phraseValue--17s79').text
    chanceOfRain = soup.find(
        'div', class_='CurrentConditions--precipValue--1RgXi').text
    time = soup.find('div', class_='CurrentConditions--timestamp--3_-CV').text
    locationLabel.config(text="Ocala, FL  (34482)")
    # locationLabel.config(text=location)
    temperatureLabel['text'] = temperature
    # temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction + " " + time)
    chanceOfRainLabel.config(text=chanceOfRain)
    master.after(60000, getWeather)
    master.update()


def openWeather_com(event):
    open_new(url)
    getWeather()


# endregion Functions
# url = "https://weather.com/en-IN/weather/today/l/c1fdfe2faebb2ccb5a78b819603546132468abbe5fd6c1a7063c0722438b5446"
url = "https://weather.com/en-IN/weather/today/l/c1fdfe2faebb2ccb5a78b819603546132468abbe5fd6c1a7063c0722438b5446?par=google&temp=f"


master = Tk()
master.title("Weather in Ocala (34482)")
master.configure(bg='white')
master.iconbitmap('weather_icon.ico')

img = Image.open('weather_icon.png').resize((150, 150))
img = ImageTk.PhotoImage(img)

locationLabel = Label(master, font=("calibri bold", 28),
                      bg=("white"))
locationLabel.grid(row=0, sticky='NEW', padx=100)

temperatureLabel = Label(master, font=("calibri bold", 70),
                         bg=("white"))
temperatureLabel.grid(row=1, sticky='W', padx=40)

imgLabel = Label(master, image=img, bg='white')
imgLabel.grid(row=1, sticky='E', pady=(20, 0))

weatherPredictionLabel = Label(master, font=("calibri bold", 24), bg='white')
weatherPredictionLabel.grid(row=2, sticky='EW')

chanceOfRainLabel = Label(master, font=(
    "calibri bold", 18), bg='white',  fg='#0645AD')
chanceOfRainLabel.grid(row=3, sticky='EW')

chanceOfRainLabel.bind("<Button-1>", openWeather_com)

getWeather()

master.mainloop()
