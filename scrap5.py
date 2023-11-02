from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

def access_url(url):
    session = HTMLSession()
    r = session.get(url) #response [200]
    r.html.render()
    text = r.html.html
    return text

def write_html_file(text):
    with open(f"output.html", "w", encoding="UTF-8") as file:
        file.writelines(text)

def read_html_file(file):
    with open(f"{file}","r" ,encoding="UTF-8") as f:
        text = f.read()
    return text

def html_parse(html_file):
    html_file = BeautifulSoup(html_file,"html.parser")
    title = html_file.find("div", class_="d-flex flex-row").get_text().strip()
    price = html_file.find("div", class_="itemPrice-wrapper").get_text().replace("Rp", "").replace(".", "").strip()
    desc = html_file.find("span", class_="itemFacts font-weight-normal").get_text().replace("\n","")
    item_code = html_file.find("span",class_="item-code").get_text().strip()
    designer = html_file.find("div", id="good-to-know").find("div").find_all("div")[-1].get_text().strip()
    measure = html_file.find_all("table", class_="table table-line table-sm")[-1].find_all("td")
    length = measure[5].get_text().strip().replace(" cm", "")
    width = measure[7].get_text().strip().replace(" cm", "")
    height = measure[9].get_text().strip().replace(" cm", "")
    img = html_file.find("img", class_="img-fluid img-nr-0")["src"]

    try:
        details = html_file.find("div", class_="product-desc-wrapper mb-4").p.get_text().strip()
    except AttributeError:
        details = ""
    
    dict_result = {"Nama Produk":title,
                   "Harga":price,
                   "Deskripsi":desc,
                   "No. Artikel":item_code,
                   "Panjang":length,                  
                    "Lebar":width,
                    "Tinggi":height,
                    "Desainer":designer,
                    "Rincian Produk":details,
                    "Gambar":img
                    }
    return dict_result


if __name__ == "__main__": 
    url = "https://www.ikea.co.id/in/produk/peralatan-dapur/perkakas-dapur/idealisk-art-90165968"

    access = access_url(url)

    write = write_html_file(access)
    
    html_file = read_html_file("output.html")
    
    result = html_parse(html_file)

    print(result)
    

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