class FileChooserView:
    class Decorators():
        @classmethod
        def stdout_format(cls, func):
            def wrapper(*args, **kwargs):
                return f"{func(*args, **kwargs)} "
            return wrapper

    @staticmethod
    @Decorators.stdout_format
    def tested_file_text():
        """Text for choosing file to be tested"""

        return "Which file will be tested?"

    @staticmethod
    @Decorators.stdout_format
    def results_file_text():
        """Text for choosing results file"""

        return "Which file contains the results?"

    @staticmethod
    @Decorators.stdout_format
    def tests_file_text():
        """Text for choosing tests file"""

        return "Which file contains the tests?"

    @staticmethod
    @Decorators.stdout_format
    def language_text():
        """Text for choosing language"""

        return "Which language is the algorithm written into?"