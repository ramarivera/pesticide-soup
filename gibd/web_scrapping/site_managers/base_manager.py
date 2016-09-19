from time import sleep
from urllib.request import Request, urlopen
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from contextlib import closing
from selenium.webdriver import PhantomJS, Firefox  # pip install selenium
from web_scrapping.model.site import Site
from web_scrapping.site_managers.worker import Worker
from functools import partial
from queue import Queue
from web_scrapping.cross_cutting.cc_logging import cclogging
from web_scrapping.cross_cutting.counter import Counter

class BaseManager(ABC):

    _pjs_path = r".\phantomjs\phantomjs.exe"
    logger = cclogging.getLogger()

    def __init__(self, baseurl, index):
        self.baseurl = baseurl
        self.index = index
        self._input = Queue()
        self._output = Queue()
        self._workers = []

    def _get_sopa(self, url: str, needjs=False) -> BeautifulSoup:
        if not needjs:
            self.logger.debug("Iniciando urllib")
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with closing(urlopen(req)) as webpage:
                soup = BeautifulSoup(webpage, "html.parser")
            self.logger.debug("Cerrando urllib")
        else:
            self.logger.debug("Iniciando PJS")
            try:
                pjs = PhantomJS(BaseManager._pjs_path)
                #pjs = Firefox()
                pjs.get(url)
                sleep(3)
                soup = BeautifulSoup(pjs.page_source, "html.parser")
            finally:
                self.logger.debug("Cerrando PJS")
                pjs.close()
                pjs.quit()
        return soup

    @abstractmethod
    def can_process(self, url: str) -> bool:  pass

    @abstractmethod
    def get_site(self, url: str) -> Site:  pass

    def enqueue(self, *args):
        self._input.put(args)

    def start_work(self, func):
        self.logger.debug("Preparando para ejecutar {0}".format(func.__name__))
        wrapper = partial(self._wrapper, func)
        counter = Counter()
        for i in range(8):
            self.logger.debug("Creando worker {}".format(i+1))
            worker = Worker(self._input, self._output, counter)
            worker.prepareworker(wrapper)
            worker.start()
            self._workers.append(worker)

    def get_results(self):
        self._input.join()
        self._stop_work()
        aux = []
        while not self._output.empty():
            aux.append(self._output.get())
        return aux

    def _stop_work(self):
        for w in self._workers:
            self._input.put("STOP")
        for w in self._workers:
            #print(dir(w))
            self.logger.debug("Join en worker {}".format(w.name))
            w.join()
        self._workers = []

    def _wrapper(self, func, *args):
        aux = func(*args)
        if hasattr(aux, "__iter__"):
            for smth in aux:
                self._output.put(smth)
        else:
            self._output.put(aux)



