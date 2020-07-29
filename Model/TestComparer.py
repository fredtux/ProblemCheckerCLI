class TestComparer:
    @staticmethod
    def compare(inp, out):
        if len(inp) != len(out):
            return 'Failed'

        for line_num in range(len(out)):
            if inp[line_num] != out[line_num]:
                return 'Failed'

        return 'Success'
