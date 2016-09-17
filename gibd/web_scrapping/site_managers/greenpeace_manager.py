from web_scrapping.site_managers.base_manager import BaseManager
from web_scrapping.model.site import Site
from web_scrapping.model.sites.greenpeace import Greenpeace
from bs4 import Tag
from typing import List, Iterator


class GreenpeaceManager(BaseManager):

    __link_template = u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page={0}'

    def __init__(self):
        baseurl = u'http://www.greenpeace.org'
        index = u'http://www.greenpeace.org/argentina/es/noticias'
        super().__init__(baseurl, index)
        self.sopas = []

    def can_process(self, url: str) -> bool:
        return True

    def get_site(self, url: str) -> Site:
        sopa = self._get_sopa(url)
        return Greenpeace(url, sopa)

    def get_sites(self, startpage=0, pages=1) -> List[Site]:
        sopas = []
        testo = []
        for page in GreenpeaceManager.__generator(startpage, startpage+pages):

            print(page)
            aux = self._get_sopa(page)
            string = aux.prettify()

            if string in testo:
                print("FUUCK")
            else:
                testo.append(string)

            sopas.append(aux)

        for i,string in enumerate(testo):
            with open("hola{0}.html".format(i),"a+",encoding="utf8") as file:
                file.write(string)

        links = [link for sopa in sopas for link in sopa.find_all(self.__noticias)]
        filtro = set([self.baseurl + l.get("href") for l in links])
        result = [self.get_site(res) for res in filtro]

        return result

    @staticmethod
    def __noticias(tag: Tag) -> bool:
        aux = tag.get("href", "")
        res = tag.name == "a" and "/argentina/es/noticias" in aux and len(aux) > 23
        if res:
            pass
        return res

    @staticmethod
    def __generator(start=0, stop=1) -> Iterator[str]:
        for i in range(start, stop):
            yield GreenpeaceManager.__link_template.format(i)
