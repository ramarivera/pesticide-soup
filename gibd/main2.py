from gibd.web_scrapping.site_managers.greenpeace_manager import GreenpeaceManager as gm



filtro = 'http://www.greenpeace.org/argentina/es/noticias/1-millon-de-firmas-para-causas-ambientales-/'
base = u"http://www.greenpeace.org"
path = base + u"/argentina/es"
sopas = {}
resultset = {}

manager = gm()
#print(manager.get_site(filtro).prettify())


rest = manager.get_sites(1)
print("Encontrados {0} resultados".format(len(rest)))

for algo in rest:
    print(algo.prettify())


