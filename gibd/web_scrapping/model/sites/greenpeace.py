from web_scrapping.model.site import Site
from bs4 import BeautifulSoup,Tag,ResultSet

class Greenpeace(Site):

    def __init__(self, url, sopa: BeautifulSoup):
        Site.__init__(self, url)
        self.__sopa = sopa
        self.__rset = ""

    def get_url(self):
        return self.url

    def get_title(self):
        rset = self.__set_rset()
        if rset and rset[0].h1.span.text:
            return rset[0].h1.span.text
        pass

    def get_content(self):
        rset = self.__set_rset()
        if rset:
            paragraphs = rset[0].find_all(self.__pltr)
            return " ".join([tag.text for tag in paragraphs if tag.text and tag.text.strip()])
        pass

    def get_date(self):
        rset = self.__set_rset()
        if rset:
            texto = rset[0].find_all(self.__date)
            return texto[0].text
        pass

    def get_image(self):
        rset = self.__set_rset()
        pass

    def __happen_box(self, tag: Tag) -> bool:
        aux = tag.name == "div" and "happen-box" in tag.get('class', [])
        if aux:
            pass
        return aux

    def __text_div(self, tag: Tag) -> bool:
        aux = tag.name == "div" and "text" in tag.get('class', [])
        if aux:
            pass
        return aux

    def __set_rset(self) -> ResultSet:
        if not self.__rset:
            self.__rset = self.__sopa.find_all(self.__happen_box)
        return self.__rset

    def __pltr(self, tag: Tag) -> bool:
        aux = tag.name == "p" and not len(tag.find_all("img"))
        if aux:
            pass
        return aux

    def __date(self,tag:Tag) -> bool:
        aux = tag.name == "span" and "author" in  tag.get("class", "")
        if aux:
            pass
        return aux
