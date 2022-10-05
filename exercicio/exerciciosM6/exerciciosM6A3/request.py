from requests_html import HTMLSession

url = "https://www.google.com.br/"
sessao = HTMLSession()
resposta = sessao.get(url)
print(resposta.text)
print(resposta.status_code)
#Simples codigo que pega um site da internet, retornando o codigo HTML da pagina e o status da pagina.