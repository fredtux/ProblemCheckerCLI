class ExecutorFactory:
    @staticmethod
    def get_executor(type):
        """Executor factory main function"""

        if not isinstance(type, str):
            raise TypeError('Executor type should be a string')

        if type == 'python':
            from Model.ExecutorPython import ExecutorPython
            return ExecutorPython()
        elif type == 'php':
            from Model.ExecutorPHP import ExecutorPHP
            return ExecutorPHP()
        elif type == 'js':
            from Model.ExecutorJS import ExecutorJS
            return ExecutorJS()

        raise Exception('Language not found')
