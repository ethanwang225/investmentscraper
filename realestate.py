from bs4 import BeautifulSoup
import requests
import time
import re
import yfinance as yf
#make file
csv=open("real_estate_sector.csv", "w", encoding="utf-8")


url="https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_real-estate?count=25&offset=0"
page=requests.get(url)
#page.text is the entire html

# Extract data
soup=BeautifulSoup(page.text, "html.parser")
#turns page.text into a soup object


all_companies=soup.find_all("tr")


#labels of stats
title_text = all_companies[0]
title_text.find_all("th")

titles = []

for title in title_text:
    titles.append(title.text)
titles.remove(titles[9])# remove 52 week thing
   


titles.append("returnOnEquity")
titles.append("reutrnOnAssets")
titles.append("forwardEPS")
titles.append("debtToEquity")
titles.append("quickRatio")
titles.append("revenueGrowth")
titles.append("ebitdaMargins")


tickers=[]
# Write to file
# Titles
for i in range(len(titles)):
    text = titles[i] + "," # Add a comma in between data so they're in different boxes
    csv.write(text.rstrip('\n')) # Remove the new line so its on the same line
csv.close()
def scraper(link):

    url=link
    page=requests.get(url)
    #page.text is the entire html

    # Extract data
    soup=BeautifulSoup(page.text, "html.parser")
    #turns page.text into a soup object


    all_companies=soup.find_all("tr")
    for company in all_companies:
        # print(player.text)
        #.text here removes the html tags
        csv=open("real_estate_sector.csv", "a", encoding="utf-8")
    # append mode/ doesn't erase everything once you write
        returnOnEquity=None
        returnOnAssets=None
        forwardEPS=None
        debtToEquity=None
        quickRatio=None
        revenueGrowth=None
        ebitdaMargins=None
        
        # try:
        #     href_line= company.find("a")
        #     if href_line:
        #         href=href_line.get("href")
        #         individual_page="https://finance.yahoo.com/"+ href
        #         #wait 3 seconds until you make another request to not get banned
        #         # time.sleep(2)
        #         individual_html=requests.get(individual_page)
        #         indi_soup=BeautifulSoup(individual_html.text, "html.parser")
        #         company_page= indi_soup.find("div", {"id": "div_faq"})
                
        #         # born_in=FAQ_player.find("p", text=re.compile("born in"))

                

        #         #-1 gives the end of the list (exlusive of the period)
        #         # place= born_in.text[born_in.text.index(", ")+2: -1]



        # except:
        #     print("player did not have individual page, skipping")
        stats = company.find_all("td")
        for i in range(len(stats)):
            
            stat_text=stats[i].text
            if i==0:
                ticker=stat_text
                company_ticker=yf.Ticker(ticker)
                company_dc=company_ticker.info
              
                if 'returnOnEquity' in company_dc:
                    returnOnEquity=str(company_dc['returnOnEquity'])+","
                if 'returnOnAssets' in company_dc:
                    returnOnAssets=str(company_dc['returnOnAssets'])+","
                if 'forwardEps' in company_dc:
                    forwardEPS=str(company_dc['forwardEps'])+","
                if 'debtToEquity' in company_dc:
                    debtToEquity=str(company_dc['debtToEquity'])+","
                if 'quickRatio' in company_dc:
                    quickRatio=str(company_dc['quickRatio'])+","
                if 'revenueGrowth' in company_dc:
                    revenueGrowth=str(company_dc['revenueGrowth'])+","
                if 'ebitdaMargins' in company_dc:
                    ebitdaMargins=str(company_dc['ebitdaMargins'])+","



                

            if "+" in stat_text:
                stat_text=stat_text.replace("+","")
            if i>1:
                if "M" in stat_text:
                    stat_text=stat_text.replace("M","")
                    if i>2:    
                        stat_text=float(stat_text)*1000000
                        stat_text=str(stat_text)
                elif "B" in stat_text:
                    stat_text=stat_text.replace("B","")
                    if i>2:
                        stat_text=float(stat_text)*1000000000
                        stat_text=str(stat_text)

            if i==1:
                stat_text=stat_text.replace(",", "")
            if i==5:
                stat_text=stat_text.replace(",", "")
            if i==6:
                stat_text=stat_text.replace(",", "")
           
            
            csv.write(stat_text.rstrip('\n'))
        if returnOnEquity:
            csv.write(returnOnEquity.rstrip('\n'))

        if returnOnAssets:
            csv.write(returnOnAssets.rstrip('\n'))
        if forwardEPS:
            csv.write(forwardEPS.rstrip('\n'))
        if debtToEquity:
            csv.write(debtToEquity.rstrip('\n'))
        if quickRatio:
            csv.write(quickRatio.rstrip('\n'))
        if revenueGrowth:
            csv.write(revenueGrowth.rstrip('\n'))
        if ebitdaMargins:
            csv.write(ebitdaMargins.rstrip('\n'))
            print(ebitdaMargins)
            


        
            
        csv.write("\n")
        csv.close()

scraper("https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_real-estate?count=25&offset=0")
print(tickers)
    #when you want to create a new folder
    #open the folder, and then go to view-> command palette-> select python interpreter-> select the one that works