from queue import Queue
from threading import Thread, Lock
import itertools
from web_scrapping.cross_cutting.cc_logging import cclogging


class Worker(Thread):
    def __init__(self, inputq, outputq, counter):
        Thread.__init__(self)
        self.input = inputq
        self.output = outputq
        self.function = None
        self.funcname = ""
        self.counter = counter
        self.lock = Lock()
        self._stop_worker = False
        self.logger = cclogging.getLogger()
        self.logger.debug("Iniciando Worker")

    def prepareworker(self, function):
        self.function = function
        self.funcname = self.function.args[0].__name__

    def run(self):
        while not self._stop_worker:
            self.logger.debug("Ejecutando ciclo  numero {1} de {0}".format(self.funcname, self.counter.value()))
            self.counter.increment()
            arg = self.input.get()

            if arg == "STOP":
                self._stop_worker = True
            else:
                self.function(*arg)

            self.input.task_done()
