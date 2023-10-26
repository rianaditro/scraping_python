import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

def get_html_data(url):
    r = requests.get(url)
    if r.status_code == 200:
        None
    else:
        print(r.status_code)
    result = r.text
    return result

html_data = get_html_data(url)
soup = BeautifulSoup(html_data,features="html.parser")

html_target = soup.find("article", class_="product_page")

list_result = []
