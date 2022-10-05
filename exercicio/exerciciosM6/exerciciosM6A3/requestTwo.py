from requests_html import HTMLSession

url = "https://raspagem.herokuapp.com/"
sessao = HTMLSession()
request = sessao.get(url)
link = request.html.find("a.stretched-link")
for links in link :
    print(links.attrs["href"])
#Codigo que busca por um conteudo especifico dentro das taga de um site 
