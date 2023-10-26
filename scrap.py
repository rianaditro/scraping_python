import requests
import pandas as pd 
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

def get_html_data(url):
    r = requests.get(url)
    """if r.status_code == 200:
        print("request works")"""
    result = r.text
    return result

#from url to string html
html_data = get_html_data(url)

#from string format to bs format, make easier to read
soup = BeautifulSoup(html_data, features="html.parser")

#the target content is on tag <li> and class col-xs-6 col-sm-4 col-md-3 col-lg-3
#this code will trim the html only on target content, reduce the size
html_target = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
#convert the html to the dictionary format

list_result = []
for html in html_target:
    # url = https://books.toscrape.com/
    # link = catalogue/its-only-the-himalayas_981/index.html
    link = html.find("a")["href"]
    link = url+link #complete link
    title = html.find("h3").find("a")["title"]
    price = html.find("p", class_="price_color").get_text().replace("Â£","")
    rating = html.p["class"][-1]
    stock = html.find("p", class_="instock availability").get_text().strip()
    image = html.find("img")["src"]
    image = url+image

    #convert string rating to int
    if rating == "One":
        rating = 1
    elif rating == "Two":
        rating = 2
    elif rating == "Three":
        rating = 3
    elif rating == "Four":
        rating = 4
    elif rating == "Five":
        rating = 5
    

    value_dict = {
        "link":link,
        "title":title,
        "price":price,
        "rating":rating,
        "stock":stock,
        "image":image
        }
    list_result.append(value_dict)

"""
html.find("h3")
<h3>
<a href="catalogue/its-only-the-himalayas_981/index.html" 
title="It's Only the Himalayas">
It's Only the Himalayas</a>
</h3>

html.find("title") -> title is not a tag
None
"""

#convert dictionary result to dataframe
df = pd.DataFrame(list_result)
df.to_excel("bookstoscrape.xlsx", index=False)