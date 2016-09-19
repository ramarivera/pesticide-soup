from tests.test_site_managers.test_greenpeace_manager import TestGreenpeaceManager
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestGreenpeaceManager('test_generator_default'))
    return suite


if __name__ == "__main__":
    resultado = unittest.TextTestRunner(verbosity=5,descriptions=True)
    resultado.run(suite())
