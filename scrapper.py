import requests
from bs4 import BeautifulSoup
from datetime import date

today = date.today()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
page, prices, cardName = ([] for i in range(3))

file = open("prices.txt", "a") #append to file, "w" to overwrite
URLFile = open("URLs.txt").readlines()
x = 0

for each in URLFile:
    page.append(requests.get(url=URLFile[x], headers=headers))
    soup = BeautifulSoup(page[x].content, "html.parser")
    if (soup.find('span', attrs={"class": "variant-short-info"}).get_text() == "Out of stock."):
        prices.append("Out of Stock")
    else:
        prices.append(soup.find('span', attrs={"class": "regular price"}).get_text()[5:])

    cardName.append(soup.find('h1', attrs={"class": "title"}).get_text())
    try:
        individualCards = open("library/"+cardName[x]+".txt", "r")
        pulledPrice = individualCards.readlines()
        pulledPriceString = "".join(pulledPrice)

        if (pulledPriceString != prices[x]):
            print(cardName[x] + " has changed price from " + pulledPriceString + " to " + prices[x])
            individualCards.seek(0)
            individualCards.truncate()
            individualCards.write(prices[x])
            individualCards.close()
        else:
            print("There was no price change for " + cardName[x] + " at the price of " + prices[x])
    except:
        individualCards = open("library/" + cardName[x] + ".txt", "w")
        individualCards.write(prices[x])
        individualCards.close()

    file.write(cardName[x] + " | " + prices[x] + " | " + today.strftime("%d/%m/%Y") + "\n")
    x += 1

file.write("-------------------\n")
file.close()
input("Press any key to exit")
