from web_scrapping.model.site import Site
from bs4 import BeautifulSoup, Tag, ResultSet


class Greenpeace(Site):

    def __init__(self, url, sopa: BeautifulSoup):
        super().__init__(url)
        self._sopa = sopa
        self._rset = None

    def _get_title(self):
        self._set_rset()
        self._title = self._rset.h1.span.text

    def _get_content(self):
        self._set_rset()
        paragraphs = self._rset.find_all(self._pltr)
        self._content = " ".join([tag.text for tag in paragraphs if tag.text and tag.text.strip()])

    def _get_date(self):
        self._set_rset()
        aux1 = self._rset.find_all(self._dateinfo)
        aux = aux1[0].text
        self._date = aux

    def _get_image(self):
        rset = self._set_rset()

    def _happen_box(self, tag: Tag) -> bool:
        aux = tag.name == "div" and "happen-box" in tag.get('class', [])
        return aux

    def _text_div(self, tag: Tag) -> bool:
        aux = tag.name == "div" and "text" in tag.get('class', [])
        if aux:
            pass
        return aux

    def _set_rset(self):
        if not self._rset:
            self._rset = self._sopa.find_all(self._happen_box)[0]

    def _pltr(self, tag: Tag) -> bool:
        aux = tag.name == "p" and not len(tag.find_all("img"))
        return aux


    def _dateinfo(self, tag:Tag) -> bool:
        aux = tag.name == "span" and "author" in tag.get("class", [])
        if aux:
            algo = "hola"
        return aux
