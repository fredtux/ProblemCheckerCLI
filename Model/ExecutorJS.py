from subprocess import Popen, PIPE
from Model.Executor import Executor


class ExecutorJS(Executor):
    def __init__(self):
        super().__init__()

    def __call__(self, file_name):
        """Open subprocess when called"""

        self.subproc = Popen(['node', file_name],
                             stdin=PIPE, stdout=PIPE, stderr=PIPE)
