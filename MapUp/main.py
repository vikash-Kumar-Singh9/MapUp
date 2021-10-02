#Using python, scrape the toll data. If you have been using selenium till now,it might not be useful since rates vary frequently. Explore the xhr requests of the webpage


import requests
from bs4 import BeautifulSoup

URL = "https://www.expresslanes.com/map-your-trip"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
scrap=soup.find_all('div')
print(scrap)

#You'll find a json file from where these toll rates are getting updated. Decode the json file and transform it to a df


import pandas as pd

# get json using developer tool
df = pd.read_json('data.json') 


print(df.to_string()) 

#Load the data into a csv with all the entry and exit combinations along with the toll rates at that moment

df.to_csv('output.csv')
