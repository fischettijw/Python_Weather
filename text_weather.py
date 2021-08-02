# Weather

# region Links
# https://www.geeksforgeeks.org/how-to-extract-weather-data-from-google-in-python/
'''
In this article, we will see how to extract weather data from google.
Google does not have its own weather API, it fetches data from
weather.com and shows it when you search on Google.
So, we will scrape the data from Google.
'''
# endregion links
# importing library
from bs4 import BeautifulSoup
import requests
import os
os.system('cls')


# enter city name
city = "34482"

# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# formatting data
data = str.split('\n')
time = data[0]
sky = data[1]

# getting all div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text

# getting other required data
pos = strd.find('Wind')
other_data = strd[pos:]

# printing all data
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)
