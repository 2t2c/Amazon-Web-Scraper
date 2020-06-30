from bs4 import BeautifulSoup
import requests
import re

url = "https://www.amazon.in/s?"

data = input("Search: ")
n = int(input("Number: "))

search_url = url + "k=" + data
print("Search URL: ",search_url, "\n")

user_agent = {"User-Agent": "Mozilla/5.0 "
                            "(Windows NT 10.0; Win64; x64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/80.0.3987.163 Safari/537.36"}

source = requests.get(search_url, headers = user_agent).text
soup = BeautifulSoup(source,"lxml")
global ITEMS , LINKS
ITEMS = []
LINKS = []

for items in soup.findAll("a", class_= "a-link-normal a-text-normal", limit=n):
    # href = items["href"]
    # print(items["href"],"\n")

    a = str(items.span)
    # print(a,"\n")
    b = re.split('>', a)
    # print(b[1], "\n")
    c = str(b[1])
    d = re.split('<', c)
    # print(d[0], "\n")
    title = d[0]

    if title not in ITEMS :
        ITEMS.append(title)
    else: pass

    # print(title, "\n")

    try:
        # href = items.attrs
        # print(href,"\n")
        link = "https://www.amazon.in" + items["href"]

        if link not in LINKS:
            LINKS.append(link)
        else: pass

        # print(link, "\n")
    except:
        pass
try:
    for i in range(n):
        print("Item {}: ".format(i+1), ITEMS[i])
        print("Link {}: ".format(i+1), LINKS[i])
        print()
except:
    pass

