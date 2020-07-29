from Model.FileChooserModel import FileChooserModel
from Model.FileParserModel import FileParserModel
from View.FileChooserView import FileChooserView


class FileChooserController():
    @staticmethod
    def get_tested_file():
        """Get the file to be tested"""

        return FileChooserModel.choose(FileChooserView.tested_file_text())

    @staticmethod
    def get_results():
        """Get results"""

        # Get results file
        results_file = FileChooserModel.choose(FileChooserView.results_file_text())

        # Return json from file
        return FileParserModel.get_json_from_file(results_file)

    @staticmethod
    def get_tests():
        """Get tests"""

        # Get tests file
        tests_file = FileChooserModel.choose(FileChooserView.tests_file_text())

        # Return json from file
        return FileParserModel.get_json_from_file(tests_file)

    @staticmethod
    def get_language():
        """Get language"""

        # Return language
        return FileChooserModel.choose(FileChooserView.language_text())
