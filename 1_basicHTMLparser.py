#Basic html parser

from urllib.request import urlopen
from bs4 import BeautifulSoup

#Stores html page
html = urlopen("https://www.pythonscraping.com/pages/page1.html")

html1 = urlopen("https://www.pythonscraping.com/pages/page1.html")


#Prints contents of page stored
print(html.read())
print()

#Extracting data from html page stored


bsObj = BeautifulSoup(html1.read(), "html.parser") #features="lxml")
print(bsObj.h1)
