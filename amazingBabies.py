from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re




# For any cat
def showCatFact(url):
    html = urlopen("http://en.wikipedia.org" + url)
    bsObj = BeautifulSoup(html, "html.parser")

    # Name of cat
    catName = bsObj.find("h1").get_text()

    # list of a <p> elements on page
    catFactList = bsObj.findAll("p")

    catFactSingle = re.sub(r'\[\d+\]', '', catFactList[random.randint(0, len(catFactList) - 1)].get_text())


    print(catName)
    print()
    print(catFactSingle)



def getCatList():
    html = urlopen("http://en.wikipedia.org/wiki/Felidae")

    catUrl = []
    bsObj = BeautifulSoup(html, "html.parser")
    catList = bsObj.find("table", {"cellspacing": "0"}). \
        findAll("a", {"class": "mw-redirect", "href": re.compile("^(/wiki/)((?!:).)*$")})
    for link in catList:
        catUrl.append(link.attrs["href"])
    return catUrl



def main():
    random.seed(datetime.datetime.now())
    moreFacts = "y"





    while(moreFacts == "y"):
        catUrls = getCatList()
        showCatFact(catUrls[random.randint(0, len(catUrls) - 1)])
        moreFacts = input("continue (y/n)?: ")


        

main()
