from abc import ABC, abstractmethod


class Site(ABC):

    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_url(self):
        pass

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def get_date(self):
        pass

    @abstractmethod
    def get_image(self):
        pass

    def prettify(self):
        cadena = "Tipo: {0} - URL: {4}\n\tTitulo: {1}\n\tFecha: {2}\n\tContenido: {3}\n"
        return cadena.format(type(self).__name__ ,self.get_title(),self.get_date(),self.get_content(),self.get_url())
