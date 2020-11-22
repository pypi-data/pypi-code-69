# -*- coding: UTF-8 -*-
from ..py_api_b import PyApiB
from ..py_mix.threadU import ThreadU
from ..py_mix.datetimeU import DatetimeU
datatimeU = DatetimeU()
threadU = ThreadU()


class CtrlCU(PyApiB):
    """
    信号相关工具
    """
    @staticmethod
    def produce(key=None):
        return PyApiB._produce(key, __class__)

    def sigint_handler(self, signum, frame):
        self.is_sigint_up = True

    def on(self):
        import signal
        self.is_sigint_up = False
        signal.signal(signal.SIGINT, self.sigint_handler)
        signal.signal(signal.SIGTERM, self.sigint_handler)
        return self

    def isExit(self):
        return self.is_sigint_up
      
    def loopdo(self, fun, *args):
        self.on()
        while not self.isExit():
            fun(args)
      
    def loopdoseconds(self, fun, *args):
        self.on()
        import time
        self.oldTime = datatimeU.dataStr()
        while not self.isExit():
            time.sleep(0.3)
            n = datatimeU.dataStr()
            if self.oldTime != n:
                self.oldTime = n
                fun(args)
                # threadU.asyncDo(fun, args).start()
                
    def loopdoWhen(self, whenStr, fun, *args, **kwargs):
        """
        # whenStr Y|m||d|H|M|S|w
        
        """
        self.on()
        import time
        self.oldTime = datatimeU.dataStr()
        while not self.isExit():
            time.sleep(0.3)
            n = datatimeU.dataStr()
            if self.oldTime != n:
                self.oldTime = n
                if whenStr and datatimeU.isNow(whenStr):
                    threadU.asyncDo(fun, *args, **kwargs).start()
                    