#https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

import urllib2
import re
from bs4 import BeautifulSoup

#Take html parsed output from BeautifulSoup and run regex matches returning
#a string as an output depending on result
def FindStock(html):
	if html.findAll(text=re.compile("^.*in stock")):
		return "in stock"
	elif html.findAll(text=re.compile("In stock")):
		return "in stock"
	else:
		return "out of stock"

#Test page with in stock message but no stock number
#quote_page = "https://www.johnlewis.com/mulberry-bayswater-strap-small-classic-grain-bag/p3591088"

#Test page with television
#quote_page = "https://www.johnlewis.com/sony-bravia-kd75zf9-led-hdr-4k-ultra-hd-smart-android-tv-75-inch-with-freeview-hd-youview-black/p3753523"

#Out of stock item
#quote_page = "https://www.johnlewis.com/mulberry-continental-leather-wallet/rosewater/p3399210"

#Test page with in stock message & stock number
quote_page = "https://www.johnlewis.com/mulbery-darley-classic-grain-leather-small-satchel-bag/p3830135"

#Perform get for page code of specified URL
page = urllib2.urlopen(quote_page)

#Parse page code using Beautiful soup
var = BeautifulSoup(page, 'html.parser')

#Perform find using BeautifulSoup for the first entry of x with particular
#attributes
price_box = var.find('p', attrs={'class': 'price price--large'})
name_box = var.find('h1', attrs={'class': 'product-header__title'})
stock_box = FindStock(var)    

print "\n\n\t\t\tATTENTION ANNE-MARIE!!!\n\n\nThe %s " \
"is %s & costs only %s!!!" % (name_box.text.strip(), stock_box, price_box.text.strip())




