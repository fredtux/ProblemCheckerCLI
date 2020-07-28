from json import load

class FileParserModel:
    @staticmethod
    def get_json_from_file(file):
        """Get json from file"""

        with open(file) as json_file:
            data = load(json_file)

        return data

    @staticmethod
    def get_lines(data):
        """Get the lines from json data"""

        if not "lines" in data:
            raise Exception('Invalid json format')

        return data['lines']