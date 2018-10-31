from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from urllib.request import urlopen



opts = Options()
opts.set_headless()
opts.add_argument("--headless")
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)

#browser = Firefox(options=opts)

url = "https://www.google.com/search?tbm=shop&hl=en-GB"


def getProductURL():
    global url
    
    print("Please enter a product!")
    choice = input()
    url = url + "&q=" + choice
    #print(url)


def listProducts():


    browser.get(url)
    results = browser.find_elements_by_class_name('eIuuYe')
    #images = browser.find_elements_by_tag_name('img')
    l = len(results)

    #print(l)

    print("Select desired product!")

    for i in range(0, l):
        print(str(i+1)+". " + results[i].text)
        
    while True:
        selProduct = input()
        #try:
        selectedProduct = int(selProduct)
        if selectedProduct<=(l+1):
            trackProducts(selectedProduct-1, results)
            break
        else:
            print("Select valid product number.")
            continue
            #break
            #return selectedProduct
        #except:
         #   print("Select valid product number.")
          #  continue


def trackProducts(productNumber, results):
    link = browser.find_element_by_link_text(results[productNumber].text)
    productLink = link.get_attribute('href')

    html = urlopen(productLink)
    bsObj = BeautifulSoup(html, "html.parser")

    price = bsObj.find("span", {"class":"price"})

    
    #browser2 = Firefox(options=opts)
    #browser2.get(productLink)

    #price = browser2.find_element_by_xpath('//span[@class="price"]')
    #price = browser2.find_element_by_xpath('//*[@id="summary-prices"]/span/span')
    print("PRODUCT DETAILS: " + results[productNumber].text)
    print()
    print("PRICE: " + price.get_text())

    print("Item Saved. This product will now be tracked.")
    browser3 = Firefox()
    browser3.get(productLink)

    
    
#for i in range(0, l):
 #   item = results[i]
  #  print(item.text)
   # continue_link = browser.find_element_by_link_text(item.text)
    #print(continue_link.get_attribute('href'))
    #print()
    #image = browser.find_element_by_xpath('//img[@alt="'+item.text+'"]')
    #print(image.get_attribute('src'))

        

def mainFunc():

    while True:
        print("Please select 1 of the following options:")
        print("1. Search product to track.")
        print("2. Enter product URL to track.")
        firstChoice = input()

        try:
            firstChoice = int(firstChoice)
            if(firstChoice == 1 or firstChoice == 2):
                break
            else:
                print("Please enter valid number.")
                continue
        except:
            print("Please enter valid number.")
            continue

    if(firstChoice == 1):
        getProductURL()
        listProducts()
        #productNumber = listProducts()


    else:
        print("TEST")

mainFunc()

print("FINISH")        
