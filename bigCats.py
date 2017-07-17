from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Felidae")
bsObj = BeautifulSoup(html, "html.parser")




catList = bsObj.find("table", {"cellspacing":"0"}).\
    findAll("a", {"class" : "mw-redirect", "href" : re.compile("^(/wiki/)((?!:).)*$") })



for list in catList:
    print(list)

print(len(catList))
