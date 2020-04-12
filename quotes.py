# git url ------------ git@github.com:vicnoo/webscraping.git

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = uReq(quotes_page)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
quotes = page_soup.findAll("div",{"class":"quotes"})
len(quotes)
#print(quotes[1].text.strip())
##print(len(quotes))
for quote in quotes:
    fav_quote = quote.findAll("p",{"class":"aquote"})
    aquote = fav_quote[0].text.strip()
    f = open("quote.txt","a")
    f.write(aquote + '\n')
    f.close()
    fav_quote = quote.findAll("p",{"class":"author"})
    author = fav_quote[0].text.strip()
    f = open("author.txt","a")
    f.write(author + '\n')
    f.close()
    print(aquote)
    print(author)

