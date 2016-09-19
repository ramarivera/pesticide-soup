from abc import ABC, abstractmethod


class Site(ABC):

    def __init__(self, url):
        self._url = url
        self._title = None
        self._content = None
        self._date = None
        self._image = None

    @property
    def url(self):
        if not self._url:
            self._get_url()
        return self._url

    @property
    def title(self):
        if not self._title:
            self._get_title()
        return self._title

    @property
    def content(self):
        if not self._content:
            self._get_content()
        return self._content

    @property
    def date(self):
        if not self._date:
            self._get_date()
        return self._date

    @property
    def image(self):
        if not self._image:
            self._get_image()
        return self._image

    @abstractmethod
    def _get_title(self): pass

    @abstractmethod
    def _get_content(self): pass

    @abstractmethod
    def _get_date(self): pass

    @abstractmethod
    def _get_image(self): pass

    def prettify(self):
        cadena = "Tipo: {0} - URL: {4}\n\tTitulo: {1}\n\tFecha: {2}\n\tContenido: {3}\n"
        return cadena.format(type(self).__name__, self.title, self.date, self.content, self.url)
