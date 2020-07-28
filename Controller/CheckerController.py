from Controller.FileChooserController import FileChooserController
from Model.FileParserModel import FileParserModel
from sys import executable
from subprocess import Popen, PIPE
from os import getcwd, path

class CheckerController:
    @staticmethod
    def main_check(tested_file=None, results_file=None):
        """Main check function"""

        # Get filename
        if tested_file is None:
            file_name = FileChooserController.get_tested_file()
        else:
            file_name = tested_file

        # Get results file
        if results_file is None:
            results = FileChooserController.get_results()
        else:
            results = FileParserModel.get_json_from_file(results_file)

        # Parse json into lines
        lines = FileParserModel.get_lines(results)

        # Run file
        print(executable + " " + getcwd() + file_name)
        proc = Popen(executable + " " + file_name, stdin=PIPE)

        # Add lines to stdin
        for line in lines:
            if isinstance(line, list):
                proc.communicate(" ".join(line))
            if isinstance(line, str):
                proc.communicate(line)
