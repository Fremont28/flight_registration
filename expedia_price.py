#Expedia Prices for one-way flights from Miami to Bogota 

import requests 
from bs4 import BeautifulSoup
import json
from lxml import html  
import argparse 

page_link="https://www.expedia.com/Flights-Search?trip=oneway&leg1=from%3AMiami%2C%20FL%20(MIA-All%20Airports)%2Cto%3ABogota%2C%20Colombia%20(BOG-El%20Dorado%20Intl.)%2Cdeparture%3A08%2F09%2F2018TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&mode=search"
#fetch the content from the url
page_response=requests.get(page_link,timeout=5)
page_content=BeautifulSoup(page_response.content,"html.parser")

#extract elements
flights=page_content.find_all(class_="icon-container")
flights

#access span for prices 
prices=page_content.find_all('span',{'class':'full-bold no-wrap'})
for price in prices:
    print(price.string)
