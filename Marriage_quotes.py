from urllib2 import urlopen
from Beautiful_soup import BeautifulSoup
import random

def generacija_stevil(izbira_stevil):
    seznam_stevil = []
    for it in range(0, izbira_stevil):
        while True:
            random_stevilo = random.randint(0,len(quote_list)-1)
            if random_stevilo not in seznam_stevil:
                break
        seznam_stevil.append(random_stevilo)
    return seznam_stevil

main_url = "http://quotes.yourdictionary.com/theme/marriage/"
webpage = urlopen(main_url).read()
#print webpage

nice_webpage = BeautifulSoup(webpage)
#print nice_webpage.html.head.title.string

quotes = nice_webpage.findAll("p", {"class": "quoteContent"})

quote_list = []
for quote in quotes:
    quote = quote.string
    quote_list.append(quote)
    #print quote

number_of_quotes = 5
random_quotes = generacija_stevil(number_of_quotes)
print random_quotes

for i in range(0, len(random_quotes)):
    print quote_list[random_quotes[i]]

