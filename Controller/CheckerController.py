from Controller.FileChooserController import FileChooserController
from Model.ExecutorFactory import ExecutorFactory
from Model.FileParserModel import FileParserModel
from Model.TestComparer import TestComparer


class CheckerController:
    @staticmethod
    def main_check(tested_file=None, results_file=None, tests_file=None, language=None):
        """Main check function"""

        ### Returned variables
        final_result = []
        stats = {"success": 0, "failed": 0}

        ### Get values if parameters were not passed
        # Get filename
        if tested_file is None:
            file_name = FileChooserController.get_tested_file()
        else:
            file_name = tested_file

        # Get tests file
        if tests_file is None:
            tests = FileChooserController.get_tests()
        else:
            tests = FileParserModel.get_json_from_file(tests_file)

        # Get results file
        if results_file is None:
            results = FileChooserController.get_results()
        else:
            results = FileParserModel.get_json_from_file(results_file)

        # Get language
        if language is None:
            language = FileChooserController.get_language()


        ### Get tests and results
        # Parse cases into lines
        cases = FileParserModel.get_cases(tests)

        # Parse results into lines
        results = FileParserModel.parse_results(FileParserModel.get_cases(results))

        ### Process tests and results
        # Get executor
        executor = ExecutorFactory.get_executor(language)

        # Loop through test cases
        test_results = []
        index = 0
        for case in cases:
            current_result = []

            # Open subprocess
            executor(file_name)

            # Format lines for stdin
            inp = ""
            for line in case:
                if isinstance(line, list):
                    inp += " ".join([str(elem) for elem in line]) + "\n"
                elif isinstance(line, str) or isinstance(line, int):
                    inp += str(line) + "\n"

            try:
                # Add lines to stdin
                executor.communicate(inp)

                # Add output to test results
                test_results.append(executor.output.split("\n"))

                current_result = executor.output.split("\n")
            except TimeoutError as err:
                # Add error to test results
                test_results.append(str(err))
                current_result = [(str(err))]

            # Compare with results
            res = TestComparer.compare(current_result, results[index])

            # Add to final result and statistics
            final_result.append(f"Test {index + 1}: {res}")
            if res == "Success":
                stats["success"] += 1
            else:
                stats["failed"] += 1

            index += 1

        return [final_result, stats]
