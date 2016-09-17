from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import filtros



fitro = ""
base = u"http://www.greenpeace.org"
path = base + u"/argentina/es"
sopas = {}
resultset = {}


def get_sopa(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    soup = BeautifulSoup(webpage, "html.parser")
    return soup


def reload():
    global filtro
    soup = get_sopa(path)
    links = soup.find_all("a")
    filtro = [base + l.get("href") for l in links if "/argentina/es/noticias" in l.get("href")]
    filtro = set(filtro)


def process(link: str):
    global resultset, sopas
    dicc = {}
    sopa = get_sopa(link)
    #print(type(sopa))
    resultset = sopa.find_all(filtros.happen_box)

    dicc["resultados"] = resultset
    dicc["sopa"] = sopa
    sopas[link] = dicc

# reload()
# for i in filtro:
#     print (i)
#

filtro = 'http://www.greenpeace.org/argentina/es/noticias/A-un-ano-del-derrame-en-San-Juan-las-organizaciones-ambientalistas-continuan-exigiendo-el-cierre-de-la-mina-Veladero-/'

process(filtro)

sanjuan = sopas[filtro]["resultados"]

titulos = [tag for tag in sanjuan if filtros.titulo_noticia(tag)]




input()
