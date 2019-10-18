import threading
import logging


class Mythiread(threading.Thread):
    def __init__(self, func, *args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        # self.res = apply(self.func, self.args)
        self.res = self.func(*self.args)


def start_thiread(f, *args, **kwargs):
    try:
        t = Mythiread(f, *args, **kwargs)
        t.start()
    except Exception as e:
        logging.error(e)