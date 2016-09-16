from urllib.request import Request, urlopen
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

from gibd.web_scrapping.model.site import Site


class BaseManager(ABC):

    def __init__(self, baseurl, index):
        self.baseurl = baseurl
        self.index = index

    def _get_sopa(self, url) -> BeautifulSoup:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req)
        soup = BeautifulSoup(webpage, "html.parser")
        return soup

    @abstractmethod
    def can_process(self, url: str) -> bool:
        pass

    @abstractmethod
    def get_site(self, url:str) -> Site:
        pass
