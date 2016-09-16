from gibd.web_scrapping.site_managers.base_manager import BaseManager
from gibd.web_scrapping.model.site import Site
from gibd.web_scrapping.model.sites.greenpeace import Greenpeace
from bs4 import BeautifulSoup,Tag


class GreenpeaceManager(BaseManager):
# un metodo para conseguir todos los links
# otro para comprobar si el url puede ser tratado por este manager

    def __init__(self):
        baseurl = u"http://www.greenpeace.org"
        index = u"http://www.greenpeace.org/argentina/es/noticias"
        BaseManager.__init__(self, baseurl, index)
        self.sopa = ""

    def can_process(self, url: str) -> bool:
        return True

    def get_site(self, url: str) -> Site:
        sopa = self._get_sopa(url)
        return Greenpeace(url, sopa)

    def get_sites(self, level: int):
        if not self.sopa:
            self.sopa = self._get_sopa(self.index)

        links = self.sopa.find_all(self.__noticias)
        filtro = set([self.baseurl + l.get("href") for l in links])
        result = [self.get_site(res) for res in filtro]

        while level:
            level -= 1

        return result

    @staticmethod
    def __noticias(tag: Tag) -> bool:
        aux = tag.get("href", "")
        res = tag.name == "a" and "/argentina/es/noticias" in aux and len(aux) > 23
        if res:
            pass
        return res
