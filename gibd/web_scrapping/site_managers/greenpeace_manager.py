from web_scrapping.site_managers.base_manager import BaseManager
from web_scrapping.site_managers.worker import Worker
from web_scrapping.model.site import Site
from web_scrapping.model.sites.greenpeace import Greenpeace
from bs4 import Tag
from typing import List, Iterator


class GreenpeaceManager(BaseManager):
    _template = u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page={0}'

    def __init__(self):
        baseurl = u'http://www.greenpeace.org'
        index = u'http://www.greenpeace.org/argentina/es/noticias'
        BaseManager.__init__(self, baseurl, index)
        self.sopas = []

    def can_process(self, url: str) -> bool:
        return True

    def get_site(self, url: str) -> Site:
        sopa = self._get_sopa(url, needjs=False)
        return Greenpeace(url, sopa)

    def get_sites(self, startpage=1, pages=1) -> List[Site]:
        links = []

        for page in GreenpeaceManager._generator(startpage, startpage + pages):
            self.enqueue(page)

        self.start_work(self._get_links_from_site)
        links = self.get_results()

        for l in set([self.baseurl + l for l in links]):
            self.enqueue(l)

        self.start_work(self.get_site)
        result = self.get_results()

        return result

    def _get_links_from_site(self, link) -> List[str]:
        aux = self._get_sopa(link, needjs=True)
        result = [link.h3.a.get("href", "") for link in aux.find_all(self._noticias)]
        return result

    @staticmethod
    def _noticias(tag: Tag) -> bool:
        res = tag.name == "div" and "news-content" in tag.get("class", [])
        if res:
            aux = tag.h3.a.get("href", "")
            res = len(aux) > 23 and aux.startswith("/argentina/es/noticias")
        return res

    @staticmethod
    def _generator(start=1, stop=2) -> Iterator[str]:
        for i in range(start, stop):
            yield GreenpeaceManager._template.format(i)

