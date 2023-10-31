from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd



def access_url(url):
    session = HTMLSession()
    r = session.get(url) #response [200]
    r.html.render()
    soup = BeautifulSoup(r.html.html,"html.parser")
    return soup


def html_file(text):
    with open(f"output.html", "w", encoding="UTF-8") as file:
        file.writelines(text)


def html_parse(soup): #fungsinya buat apa, for parsing, the output or return value, should be a dictionary. ex = {"title":ÖSTANÖ} dst
    title = soup.find("div", class_="d-flex flex-row").get_text().strip()
    price = soup.find("p", class_="itemBTI display-6").get_text().replace("Rp", "").replace(".", "").strip()
    desc = soup.find("span", class_="itemFacts font-weight-normal").get_text()

    dict_result = {"title":title,
                   "price":price,
                   "desc":desc,
                    }
    return dict_result


if __name__ == "__main__": 
    url = "https://www.ikea.co.id/in/produk/kursi-makan/kursi-berpelapis/ostano-art-30568901"
    soup = access_url(url)
    html_file(soup.prettify())
    print(html_parse(soup))
    


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


#soup = BeautifulSoup(r.html.html, "html.parser")

#return soup
"""soup = BeautifulSoup(r, "html.parser")

quote = soup.find_all("div" ,class_="quote")
result = []
for i in quote:
    author = i.find("small", class_="author").get_text()
    text = i.find("span", class_="text").get_text()
    dict = {"author":author,
            "quote":text}
    result.append(dict)

df = pd.DataFrame(result)"""
#print(df)