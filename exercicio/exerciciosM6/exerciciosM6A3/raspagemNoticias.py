from time import time
from requests_html import HTMLSession

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://raspagem.herokuapp.com/noticias/"
navegador = Chrome(service=Service(ChromeDriverManager().install()))
navegador.get(url)
link = navegador.find_element("ul li a")
link.click()
time.sleep(20 * 1000)


# url = "https://raspagem.herokuapp.com/noticias/"
# sessao = HTMLSession()
# request = sessao.get(url)
# link = request.html.find("ul li a")
# for links in link :
#     print(links.attrs["href"])