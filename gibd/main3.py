from web_scrapping.site_managers.greenpeace_manager import GreenpeaceManager
from web_scrapping.site_managers.algo import get
from web_scrapping.model.noticia import Noticia
from web_scrapping.persistence.base import Base,engine,Session
from web_scrapping.persistence.noticia_mapper import mapper
import pickle
import time

def site2notic(algo):
    notic = Noticia(algo.url)
    notic.fecha = algo.date
    notic.titulo = algo.title
    notic.texto = algo.content
    return notic

noticias = []
test = []

#if input("Crear todo?").upper() == "Y":
if "dY" == "Y":
    session = Session()
    Base.metadata.create_all(engine)
    session.commit()

gm = GreenpeaceManager()

t0 = time.time()
test += gm.get_sites(pages=20)
t1 = time.time()

print (t1-t0)
for algo in test:
    noticias.append(site2notic(algo))

if input("Intentar guardar?").upper() == "Y":
    session = Session()
    for noti in noticias:
        if not session.query(Noticia).filter_by(titulo = noti.titulo).first():
            session.add(noti)
    session.commit()
