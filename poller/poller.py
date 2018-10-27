import time
from abc import ABCMeta, abstractmethod


class Poller(object):
    """
    Base class for classes that run
    """
    __metaclass__ = ABCMeta
    def __init__(self, polling_interval_secs):
        self.running = False
        self.polling_interval_secs = polling_interval_secs


    @abstractmethod
    def do_work(self):
        """

        :return:

        """
        raise NotImplementedError("Must override method: do_work")


    def start(self):
        self.running = True
        while self.running:
            start = time.clock()

            self.do_work()

            work_duration = time.clock() - start
            time.sleep(max(0, self.polling_interval_secs - work_duration))

    def stop(self):
        self.running = False
