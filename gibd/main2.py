from web_scrapping.site_managers.greenpeace_manager import GreenpeaceManager as gm
from web_scrapping.model.noticia import Noticia
from web_scrapping.persistence.base import Base,engine,Session
from web_scrapping.persistence.noticia_mapper import mapper
import pickle

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def load_object(filename):
    with open(filename, 'rb') as input2:
        return pickle.load(input2)

def site2notic(algo):
    notic = Noticia(algo.get_url())
    notic.fecha = algo.get_date()
    notic.titulo = algo.get_title()
    notic.texto = algo.get_content()
    return notic

filtro = 'http://www.greenpeace.org/argentina/es/noticias/1-millon-de-firmas-para-causas-ambientales-/'
base = u"http://www.greenpeace.org"
path = base + u"/argentina/es"
filepath = 'archivo.gibd'
sopas = {}
resultset = {}

manager = gm()
sitios = []
noticias = []
#print(manager.get_site(filtro).prettify())

if input("Leer de la Web? ").upper() == "Y":
    rest = []
    rest.append(manager.get_sites(0, 5))

    #for i in range(0, 5):
    #    print("Buscando {0}".format(i))
    #    rest.append(manager.get_sites(i, 1))
    #    #rest.append(manager.get_site(filtro))

    print("Encontrados {0} resultados".format(len(rest)))
    sitios = [site for lista in rest for site in lista]
#    sitios = rest
    for algo in sitios:
        noticias.append(site2notic(algo))
    save_object(noticias, filepath)
else:
    noticias = load_object(filepath)

if input("Crear todo?").upper() == "Y":
    session = Session()
    Base.metadata.create_all(engine)
    session.commit()

if input("Intentar guardar?").upper() == "Y":
    session = Session()
    for noti in noticias:
        session.add(noti)
    session.commit()

