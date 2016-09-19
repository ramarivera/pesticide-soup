from web_scrapping.site_managers.greenpeace_manager import GreenpeaceManager
import unittest


class TestGreenpeaceManager(unittest.TestCase):

    def setUp(self):
        self.links =  [ u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=0',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=1',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=2',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=3',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=4',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=5',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=6',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=7',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=8',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=9',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=10',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=11',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=12',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=13',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=14',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=15',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=16',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=17',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=18',
                        u'http://www.greenpeace.org/argentina/es/noticias/#tab=0&gvs=false&page=19']

    def test_generator_default(self):
        """
        Prueba si el generador funciona correctamente
        """
        for url in GreenpeaceManager._generator():
            self.assertEqual(url,self.links[0])


