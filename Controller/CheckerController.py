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
        proc = Popen([executable, file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE)

        # Add lines to stdin
        # for line in lines:
        #     if isinstance(line, list):
        #         output = proc.communicate(input=" ".join([str(elem) for elem in line]).encode())[0].decode().strip()
        #     if isinstance(line, str):
        #         output = proc.communicate(input=line.encode())[0].decode().strip()

        inp = ""
        for line in lines:
            if isinstance(line, list):
                inp += " ".join([str(elem) for elem in line]) + "\n"
            elif isinstance(line, str) or isinstance(line, int):
                inp += str(line) + "\n"

        output = proc.communicate(input=inp.encode())[0].decode().strip()

        # output = proc.communicate()[0].decode().strip()
        print(output)
