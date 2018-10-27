from setuptools import setup

setup(name='poller',
      version='0.2',
      description='Base class for classes that poll a task regularly, with a constant minimum time interval between each poll. Each polling interval is the maximum of a) polling_interval_secs and b) the time taken to do the task.',
      url='https://github.com/AnnAnnFryingPan/poller',
      author='Ann Gledson',
      author_email='anngledson@gmail.com',
      license='MIT',
      packages=['poller'],
      zip_safe=False)
