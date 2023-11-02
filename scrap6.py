from requests_html import AsyncHTMLSession

url = "https://www.ikea.co.id/in/produk/kursi-makan/kursi-berpelapis/"

asession = AsyncHTMLSession()

async def get_links(url):
    r = await asession.get(url)
    await r.html.arender()
    return r
a = asession.run(get_links(url), get_links(url))

links = a.html.absolute_links
print(len(links))
