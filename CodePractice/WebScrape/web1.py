import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://www.newegg.com/p/pl?d=graphic+cards'
uClient = uReq(my_url)
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll('div', {"class":"item-container"})
for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll('a', {"class ":"item-title"})
    product_name = title_container[0].text 

    shipping_container = container.findAll('li', {"class":"price-ship"})
    ship_price = shipping_container[0].text.strip()

    print(brand)
    print(product_name)
    print(ship_price)
uClient.close()