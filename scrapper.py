import requests
from bs4 import BeautifulSoup
from datetime import date

today = date.today()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
page, prices, cardName = ([] for i in range(3))

file = open("prices.txt", "a") #append to file, "w" to overwrite
URLFile = open("URLs.txt").readlines()
URLFile.close()
x = 0

for each in URLFile:
    page.append(requests.get(url=URLFile[x], headers=headers))
    soup = BeautifulSoup(page[x].content, "html.parser")
    if (soup.find('span', attrs={"class": "variant-short-info"}).get_text() == "Out of stock."):
        prices.append("Out of Stock")
    else:
        prices.append(soup.find('span', attrs={"class": "regular price"}).get_text())
    cardName.append(soup.find('h1', attrs={"class": "title"}).get_text())
    file.write(cardName[x] + " | " + prices[x] + " | " + today.strftime("%d/%m/%Y") + "\n")
    x += 1

file.write("-------------------\n")
file.close()
