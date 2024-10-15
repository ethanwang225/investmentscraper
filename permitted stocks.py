from bs4 import BeautifulSoup
import requests
import time
import re
import yfinance as yf
import csv



output=open('approved_stats.csv',"w")
keys=["Name","Sector","Ticker","returnOnEquity","returnOnAssets","debtToEquity",
      "quickRatio","revenueGrowth","ebitdaMargins","trailingAnnualDividendYield",
      "twoHundredDayAverage","trailingPE","forwardPE"
      ,"regularMarketPreviousClose","regularMarketOpen","regularMarketDayLow",
      "regularMarketDayHigh","beta","marketCap","trailingAnnualDividendRate",
      "profitMargins","bookValue","trailingEps","pegRatio","trailingPegRatio",
      "grossMargins","operatingMargins","ebitda","freeCashflow","operatingCashflow",
      "earningsGrowth","currentRatio"
      ]
for i in range(len(keys)):
    
    key=keys[i]+","
    output.write(key.rstrip('\n'))
output.write('\n')
csv_data = []

# Open and read the CSV file
with open('finalapproved.csv', mode='r') as file:
    csv_reader = csv.reader(file)  # Create the CSV reader object
    for row in csv_reader:
        csv_data.append(row)
del csv_data[0]
filtered_data = [row for row in csv_data if row[2] == "New York Stock Exchange, Inc."]

# Now filtered_data will contain only the rows where the stock exchange is "New York Stock Exchange, Inc."
sectors=[]
for ken in filtered_data:
    for z in range(len(ken)):
        if z==4:
            nico_collins=ken[z].replace(",","")
            nico_collins+=","
            sectors.append((nico_collins))
counter=0
for row in filtered_data:
    output=open("approved_stats.csv", "a", encoding="utf-8")



    returnOnEquity=""
    returnOnAssets=""
    forwardEPS=""
    debtToEquity=""
    quickRatio=""
    revenueGrowth=""
    ebitdaMargins=""
    trailingAnnualDividendYield=""
    twoHundredDayAverage=""
    trailingPE=""
    forwardPE=""
    regularMarketPreviousClose=""
    regularMarketOpen=""
    regularMarketDayLow=""
    regularMarketDayHigh=""
    beta=""
    marketCap=""
    trailingAnnualDividendRate=""
    profitMargins=""
    bookValue=""
    trailingEps=""
    pegRatio=""
    trailingPegRatio=""
    grossMargins=""
    operatingMargins=""
    ebitda=""
    freeCashflow=""
    operatingCashflow=""
    earningsGrowth=""
    currentRatio=""
    



        # Print each row
    
    for i in range(len(row)):
        if i==0:
            name=row[i]
            name_text=name+","
            output.write(name_text.rstrip('\n'))
        if i ==1:
            output.write(sectors[counter].rstrip('\n'))
        if i ==1:
            ticker=row[1]
            text=ticker+","
            output.write(text.rstrip('\n'))
         
            company=yf.Ticker(ticker)
            company_dc=company.info            
            if 'returnOnEquity' in company_dc:
                returnOnEquity=str(company_dc['returnOnEquity'])+","
                output.write(returnOnEquity.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))
            if 'returnOnAssets' in company_dc:
                returnOnAssets=str(company_dc['returnOnAssets'])+","
                output.write(returnOnAssets.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))
            if 'debtToEquity' in company_dc:
                debtToEquity=str(company_dc['debtToEquity'])+","
                output.write(debtToEquity.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))
            if 'quickRatio' in company_dc:
                quickRatio=str(company_dc['quickRatio'])+","
                output.write(quickRatio.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))
            if 'revenueGrowth' in company_dc:
                revenueGrowth=str(company_dc['revenueGrowth'])+","
                output.write(revenueGrowth.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'ebitdaMargins' in company_dc:
                ebitdaMargins=str(company_dc['ebitdaMargins'])+","
                output.write(ebitdaMargins.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'trailingAnnualDividendYield' in company_dc:
                trailingAnnualDividendYield=str(company_dc['trailingAnnualDividendYield'])+","
                output.write(trailingAnnualDividendYield.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'twoHundredDayAverage' in company_dc:
                twoHundredDayAverage=str(company_dc['twoHundredDayAverage'])+","
                output.write(twoHundredDayAverage.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'trailingPE' in company_dc:
                trailingPE=str(company_dc['trailingPE'])+","
                output.write(trailingPE.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'forwardPE' in company_dc:
                forwardPE=str(company_dc['forwardPE'])+","
                output.write(forwardPE.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'regularMarketPreviousClose' in company_dc:
                regularMarketPreviousClose=str(company_dc['regularMarketPreviousClose'])+","
                output.write(regularMarketPreviousClose.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'regularMarketOpen' in company_dc:
                regularMarketOpen=str(company_dc['regularMarketOpen'])+","
                output.write(regularMarketOpen.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'regularMarketDayLow' in company_dc:
                regularMarketDayLow=str(company_dc['regularMarketDayLow'])+","
                output.write(regularMarketDayLow.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'regularMarketDayHigh' in company_dc:
                regularMarketDayHigh=str(company_dc['regularMarketDayHigh'])+","
                output.write(regularMarketDayHigh.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'beta' in company_dc:
                beta=str(company_dc['beta'])+","
                output.write(beta.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'marketCap' in company_dc:
                marketCap=str(company_dc['marketCap'])+","
                output.write(marketCap.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'trailingAnnualDividendRate' in company_dc:
                trailingAnnualDividendRate=str(company_dc['trailingAnnualDividendRate'])+","
                output.write(trailingAnnualDividendRate.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'profitMargins' in company_dc:
                profitMargins=str(company_dc['profitMargins'])+","
                output.write(profitMargins.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'bookValue' in company_dc:
                bookValue=str(company_dc['bookValue'])+","
                output.write(bookValue.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'trailingEps' in company_dc:
                trailingEps=str(company_dc['trailingEps'])+","
                output.write(trailingEps.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'pegRatio' in company_dc:
                pegRatio=str(company_dc['pegRatio'])+","
                output.write(pegRatio.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'trailingPegRatio' in company_dc:
                trailingPegRatio=str(company_dc['trailingPegRatio'])+","
                output.write(trailingPegRatio.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'grossMargins' in company_dc:
                grossMargins=str(company_dc['grossMargins'])+","
                output.write(grossMargins.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'operatingMargins' in company_dc:
                operatingMargins=str(company_dc['operatingMargins'])+","
                output.write(operatingMargins.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'ebitda' in company_dc:
                ebitda=str(company_dc['ebitda'])+","
                output.write(ebitda.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'freeCashflow' in company_dc:
                freeCashflow=str(company_dc['freeCashflow'])+","
                output.write(freeCashflow.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'operatingCashflow' in company_dc:
                operatingCashflow=str(company_dc['operatingCashflow'])+","
                output.write(operatingCashflow.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'earningsGrowth' in company_dc:
                earningsGrowth=str(company_dc['earningsGrowth'])+","
                output.write(earningsGrowth.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))

            if 'currentRatio' in company_dc:
                currentRatio=str(company_dc['currentRatio'])+","
                output.write(currentRatio.rstrip('\n'))
            else:
                comma=","
                output.write(comma.rstrip('\n'))
                
       
            
                
    counter+=1       
    output.write("\n")
            

        




