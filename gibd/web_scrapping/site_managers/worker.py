from queue import Queue
from threading import Thread


class Worker(Thread):
    def __init__(self, inputq, outputq):
        Thread.__init__(self)
        self.input = inputq
        self.output = outputq
        self.function = None
        self._stop_worker = False

    def prepareworker(self, function):
        self.function = function

    def run(self):
        while not self._stop_worker:
            arg = self.input.get()

            if arg == "STOP":
                self._stop_worker = True
            else:
                self.function(*arg)

            self.input.task_done()
