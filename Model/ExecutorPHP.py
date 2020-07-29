from sys import executable
from subprocess import Popen, PIPE
from Model.Executor import Executor


class ExecutorPHP(Executor):
    def __init__(self):
        pass

    def __call__(self, file_name):
        """Open subprocess when called"""

        self.subproc = Popen(['php', file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE)

