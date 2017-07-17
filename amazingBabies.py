from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re




# For domestic cats
def getCatFacts():
    html = urlopen("http://en.wikipedia.org/wiki/Cat")
    bsObj = BeautifulSoup(html, "html.parser")
    catFacts = bsObj.findAll("p")
    return catFacts

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
    # moreFacts = "y"
    #
    # allCatFacts = getCatFacts()
    #
    #
    #
    # while(moreFacts == "y"):
    #
    #
    #     singleFact = re.sub(r'\[\d+\]', '', allCatFacts[random.randint(0, len(allCatFacts) - 1)].get_text())
    #
    #     print(singleFact)
    #     print("\n")
    #     moreFacts = input("continue (y/n)?: ")

    getCatList()
        

main()
