from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,"html.parser")
#make code more structured
print(soup.prettify())

"""
ImportError: cannot import name 'BeautifulSoup' from partially initialized module 'bs4' (most likely due to 
a circular import) 

because a file named bs4.py -> rename to scrap4.py
"""

print(soup.get_text())