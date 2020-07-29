from json import load


class FileParserModel:
    @staticmethod
    def get_json_from_file(file):
        """Get json from file"""

        with open(file) as json_file:
            data = load(json_file)

        return data

    @staticmethod
    def get_cases(data):
        """Get the lines from json data"""

        if not "cases" in data:
            raise Exception('Invalid json format')

        return data['cases']

    @staticmethod
    def parse_results(data):
        """Parse results to mimick stdin"""

        result = []

        for case in data:
            partial_result = []
            for line in case:
                partial_result.append(" ".join([str(elem) for elem in line]))

            result.append(partial_result)

        return result