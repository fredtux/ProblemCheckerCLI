from sys import executable
from subprocess import Popen, PIPE
from Model.Executor import Executor


class ExecutorPython(Executor):
    def __init__(self):
        super().__init__()

    def __call__(self, file_name):
        """Open subprocess when called"""

        self.subproc = Popen([executable, file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE)

