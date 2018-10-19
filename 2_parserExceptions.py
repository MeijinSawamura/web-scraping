#Basic web scraper with exception checks

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:                                                     #1st block to check if path not found (/pages/..)
        html = urlopen(url)
    except HTTPError as e:  
        return None
    try:                                                     #2nd block to check if server/attributes not found
        bsObj = BeautifulSoup(html.read(), "html.parser")    #will error if server not found
        title = bsObj.body.h1                                #if attribute not found, eg. bsObj.newAttribute
    except AttributeError as e:
        return None
    return title

title = getTitle("https://www.pythonscraping.com/pages/page1.html")

if title == None:
    print("Title could not be found.")
else:
    print(title)
    
