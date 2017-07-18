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
    catFactList = bsObj.find("div", {"class":"mw-parser-output"}).findAll("p", recursive = False)

    catFactSingle = re.sub(r'\[\d+\]', '', catFactList[random.randint(0, len(catFactList) - 1)].get_text())


    print(catName)
    print()
    print(catFactSingle)

def getCatPic(url):
    html = urlopen("http://en.wikipedia.org" + url)
    bsObj = BeautifulSoup(html, "html.parser")

    catPicLink = bsObj.find("a", {"class":"image"}).attrs["href"]
    catImageHtml = urlopen("http://en.wikipedia.org" + catPicLink)
    catImageObj = BeautifulSoup(catImageHtml, "html.parser")

    catPic = catImageObj.find("a", {"class": "internal"}).attrs["href"]

    return "https:" + catPic



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
    # random.seed(datetime.datetime.now())
    # moreFacts = "y"
    #
    #
    #
    #
    #
    # while(moreFacts == "y"):
    #     catUrls = getCatList()
    #     showCatFact(catUrls[random.randint(0, len(catUrls) - 1)])
    #     moreFacts = input("continue (y/n)?: ")

    print(getCatPic("/wiki/Bay_cat"))


        

main()
