from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd


def access_url(url):
    session = HTMLSession()
    r = session.get(url) #response [200]
    r.html.render()
    text = BeautifulSoup(r.html.html,"html.parser")
    return text

def write_html_file(text):
    with open(f"output.html", "w", encoding="UTF-8") as file:
        file.writelines(text)

def read_html_file(file):
    with open(f"{file}","r" ,encoding="UTF-8") as f:
        text = f.read()
    text = BeautifulSoup(text,"html.parser")
    return text


def html_parse(text): #fungsinya buat apa, for parsing, the output or return value, should be a dictionary. ex = {"title":ÖSTANÖ} dst
    title = text.find("div", class_="d-flex flex-row").get_text().strip()
    price = text.find("p", class_="itemBTI display-6").get_text().replace("Rp", "").replace(".", "").strip()
    desc = text.find("span", class_="itemFacts font-weight-normal").get_text().replace("\n","")
    item_code = html_file.find("span",class_="item-code").get_text().strip()
    designer = html_file.find("div", id="good-to-know").find("div").find_all("div")[-1].get_text().strip()
    measure = html_file.find_all("table", class_="table table-line table-sm")[-1].find_all("td")
    length = measure[6].get_text().strip().replace(" cm", "")
    width = measure[7].get_text().strip().replace(" cm", "")
    height = measure[9].get_text().strip().replace(" cm", "")

    dict_result = {"Nama Produk":title,
                   "Harga":price,
                   "Deskripsi":desc,
                   "No. Artikel":item_code,
                   "Ukuran":{"Panjang":length,
                             "Lebar":width,
                             "Tinggi":height},
                    "Desainer":designer,

                    }
    return dict_result


if __name__ == "__main__": 
    url = "https://www.ikea.co.id/in/produk/kursi-makan/kursi-berpelapis/ostano-art-30568901"
    #soup = access_url(url)
    #write_html_file(soup.prettify())
    #text_html = read_html_file("output.html")
    #parse = html_parse(text_html)
    html_file = read_html_file("output.html")
    details = html_file.find("div", class_="product-desc-wrapper mb-4").p.get_text().strip()
    image_list = []
    image = html_file.find_all("div", class_="image-container slick-slide")
    for div in image:
        img = div.find("span").find("img")["data-lazy"]
        image_list.append(img)
    
    print(image_list)

    
#scraping
"""
1. deskripsi produk
2. no. artikel
3. opsional =Bahan sampai rangka dasar
4. desainer
5. url gambar
    dict_result = {"title":title,
                   "price":price,
                   "desc":desc,
                   "Ukuran" : {"kedalaman" : "45cm",
                                "Tinggi" : "76cm dst"}}
"""