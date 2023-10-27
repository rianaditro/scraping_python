import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

main_url = "https://books.toscrape.com/"

def get_html_str(url):
    r = requests.get(url)
    if r.status_code == 200:
        None
    else:
        print(r.status_code)
        print(url)
    result = r.text
    return result

def get_url_from_a_page(url,catalogue):
    if catalogue is True:
        main_url = "https://books.toscrape.com/catalogue/"
    else:
        main_url = "https://books.toscrape.com/"
    html_str = get_html_str(url)
    soup = BeautifulSoup(html_str,"html.parser")
    list_books_url = []
    html_li = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for html in html_li:
        books_url = html.find("h3").find("a")["href"]
        books_url = main_url+books_url
        list_books_url.append(books_url)
    return list_books_url

def scrap(url):    
    page = get_html_str(url)
    soup = BeautifulSoup(page, features="html.parser")
    created = soup.find_all("meta")[1]["content"]
    categories = soup.find("ul", class_="breadcrumb").find_all("li")[2].get_text().strip()
    title = soup.find("ul", class_="breadcrumb").find_all("li")[3].get_text().strip()
    image = soup.find("img")["src"].replace("../../",main_url)
    p = soup.find_all("p")
    stock = p[1].get_text()
    stock = re.findall(r'\d+',stock)[0]
    rating_str = p[2]["class"][-1]
    desc = p[3].get_text()
    td = soup.find_all("td")
    upc = td[0].get_text()
    product_type = td[1].get_text()
    priceExTax = td[2].get_text().replace("Â£","")
    priceInTax = td[3].get_text().replace("Â£","")
    tax = td[4].get_text().replace("Â£","")
    reviews = td[6].get_text()
    
    value_dict = {
        "url":url,
        "title":title,
        "rating":rating_str,
        "stock":stock,
        "upc":upc,
        "created":created,
        "categories":categories,
        "product type":product_type,
        "price exclude tax":priceExTax,
        "proce include tax":priceInTax,
        "tax":tax,
        "number of reviews":reviews,
        "image":image,
        "decsription":desc
    }
    return value_dict

#list of all books link    
home = get_url_from_a_page(main_url,False)

for i in range(2,6):
    next_page = main_url+f"catalogue/page-{i}.html"
    next_url = get_url_from_a_page(next_page,True)
    home.extend(next_url)

result_list = []
for i in home:
    try:
        scrap_dict = scrap(i)
        result_list.append(scrap_dict)
    except IndexError:
        continue

df = pd.DataFrame(result_list)
df.to_excel("scrap.xlsx", index=False)