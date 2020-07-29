from threading import Event, Thread
from abc import ABC, abstractmethod


class Executor(ABC):
    @property
    def subproc(self):
        return self._subproc

    @subproc.setter
    def subproc(self, value):
        self._subproc = value

    @property
    def output(self):
        return self._output.decode().strip()

    @output.setter
    def output(self, value):
        self._output = value

    @property
    def error(self):
        return self._error.decode().strip()

    @error.setter
    def error(self, value):
        self._error = value

    def communicate(self, data):
        """Communicate to subprocess stdin"""

        # Create new thread
        ev = Event()
        thr = Thread(target=self.worker, args=(data,))
        thr.start()

        # Join thread after 10 seconds
        thr.join(10)
        if thr.is_alive():
            # Kill thread
            ev.set()

            # Kill subprocess
            self.subproc.kill()

            # Set errors
            raise TimeoutError('Timeout Error')

    def worker(self, data):
        """Main worker for communication"""

        self.output, self.error = self.subproc.communicate(input=data.encode())

    @abstractmethod
    def __call__(self):
        pass
