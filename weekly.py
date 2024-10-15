from bs4 import BeautifulSoup
import requests
import time
import re


def scraper(link):

    url=link
    page=requests.get(url)
    #page.text is the entire html
    print(page.text)
    # Extract data
    soup=BeautifulSoup(page.text, "html.parser")
    #turns page.text into a soup object

    big=[]
    dates=soup.find_all("tr")
    
    for date in dates:
        small=[]

        
        
        stats = date.find_all("td")
        
        for stat in date:
            
            small.append(stat)

        big.append(small)
        print(big)
    
scraper("https://finance.yahoo.com/quote/EQIX/history")