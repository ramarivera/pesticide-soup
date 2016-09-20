from time import sleep
from urllib.request import Request, urlopen
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from contextlib import closing
from selenium.webdriver import PhantomJS  # pip install selenium
from web_scrapping.model.site import Site
from multiprocessing import Pool, Process, Manager
from functools import partial


class BaseManager(ABC):

    _pjs_path = r".\phantomjs\phantomjs.exe"

    def __init__(self, baseurl, index):
        self.baseurl = baseurl
        self.index = index
        self._input = Manager().Queue()
        self._output = Manager().Queue()
        self._workers = []

    def _get_sopa(self, url: str, needjs=False) -> BeautifulSoup:
        if not needjs:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with closing(urlopen(req)) as webpage:
                soup = BeautifulSoup(webpage, "html.parser")
        else:
            with closing(PhantomJS(BaseManager._pjs_path)) as pjs:
                pjs.get(url)
                sleep(3)
                soup = BeautifulSoup(pjs.page_source, "html.parser")
        return soup

    @abstractmethod
    def can_process(self, url: str) -> bool:  pass

    @abstractmethod
    def get_site(self, url: str) -> Site:  pass

    def enqueue(self, *args):
        self._input.put(args)

    def start_work(self, func):
        wrapper = partial(self._wrapper, func)
        input = []
        while not self._input.empty():
            input.append(self._input.get())
        with Pool(processes=4) as pl:
            pl.starmap(wrapper, input)

    def get_results(self):
        aux = []
        while not self._output.empty():
            aux.append(self._output.get())
        return aux

    def _wrapper(self, func, *args):
        aux = func(args)
        if hasattr(aux,"__iter__"):
            for smth in aux:
                self._output.put(smth)
        else:
            self._output.put(aux)


if __name__ == "__main__" : pass



