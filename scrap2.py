import requests
import pandas as pd
from bs4 import BeautifulSoup

"""this function get the html data to string"""
def get_html_data(url):
    r = requests.get(url)
    if r.status_code == 200:
        None
    else:
        print(r.status_code)
    result = r.text
    return result

"""this function get url for every single books in a page to a list
output will be ['https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html', 
'https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',....,
'https://books.toscrape.com/catalogue/soumission_998/index.html']"""
def get_url_books(url):
    html_str = get_html_data(url)
    soup = BeautifulSoup(html_str, features="html.parser")
    list_result = []
    html_list = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for html in html_list:
        url_result = html.find("h3").find("a")["href"]
        url_result = url+url_result
        list_result.append(url_result)
    return list_result

"""this function is scrapping the data from a page"""
def scrap_books_data(url):
    html_data = get_html_data(url)
    soup = BeautifulSoup(html_data,features="html.parser")
    html = soup.find("article")
    title = html.find("h1").get_text()
    image = html.find("img")["src"]
    rating = html.p["class"][-1]
    desc = html.find_all("p")[-1].get_text()
    td = html.find_all("td")
    upc = td[0].get_text()
    type = td[1].get_text()
    priceExTax = td[2].get_text().replace("Â£","")
    priceInTax = td[3].get_text().replace("Â£","")
    tax = td[4].get_text().replace("Â£","")
    stocks = td[5].get_text()
    reviews = td[6].get_text()
    categories = soup.find_all("a")[-1].get_text()
    value_dict = {
    "title":title,
    "rating":rating,
    "categories":categories,
    "description":desc,
    "upc":upc,
    "type":type,
    "price exclude tax":priceExTax,
    "price include tax":priceInTax,
    "tax":tax,
    "availability":stocks,
    "number of reviews":reviews,
    "image":image
    }
    return value_dict

url_l = ["https://books.toscrape.com/"]
"""this will give us a list of web page that will be scraped"""
for i in range(2,21):
    next_page_url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    url_l.append(next_page_url)

"""this give us all url of books for 20 pages"""
url_list = []
for i in url_l:
    str_url = str(i)
    url_books = get_url_books(str_url)
    url_list.extend(url_books)

dict_result = []
for i in url_list:
    str_url = str(i)
    scrap = scrap_books_data(str_url)
    dict_result.append(scrap)

df = pd.DataFrame(dict_result)
df.to_excel("bookstoscrape.xlsx", index=False)