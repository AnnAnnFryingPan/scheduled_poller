import time
from abc import ABCMeta, abstractmethod


class Poller(object):
    """
    Base class for classes that polls a task regularly, with a constant minimum time interval between each poll.
    Warning: Each polling interval is the maximum of a) polling_interval_secs and b) the time taken to do the task.
            (so the polling interval might be longer than polling_interval_secs
    ToDo: An alternative name might be ScheduledTask

    """
    __metaclass__ = ABCMeta
    def __init__(self, polling_interval_secs):
        """
            Construct a new Poller object (Poller is an abstract class)

            :param polling_interval_secs: time interval (seconds) between scheduled runs.
            :raises polling_interval_secs must be greater than 0 or a ValueError will be returned.
            :type polling_interval_secs: float

            Warning: Each polling interval is the maximum of a) polling_interval_secs and b) the time taken to do the task.
            (so the polling interval might be longer than polling_interval_secs


        """

        self.running = False
        if(polling_interval_secs > 0.0):
            self.polling_interval_secs = polling_interval_secs
        else:
            raise ValueError("Polling interval must be greater than 0 seconds.")


    @abstractmethod
    def do_work(self):
        """
            Perform the work to be done, during each poll (aka 'scheduled task')

            :raises This procedure must be overridden or it will raise a NotImplemenetedError

        """
        raise NotImplementedError("Must override method: do_work")


    def start(self):
        """
            Start the poller. This will run the do_work procedure every self.polling_interval_secs seconds
            If the do_work procedure takes longer than polling_interval_secs, the next poll will take place as
            soon as the task has finished:
                Each polling interval is the maximum of a) polling_interval_secs and b) the time taken to do the task.

        """
        self.running = True
        while self.running:
            start = time.clock()

            self.do_work()

            work_duration = time.clock() - start
            time.sleep(max(0, self.polling_interval_secs - work_duration))

    def stop(self):
        """
            Stop the poller.  

        """
        self.running = False
