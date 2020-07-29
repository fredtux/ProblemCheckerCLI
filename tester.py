from Controller.CheckerController import CheckerController
import argparse

parser = argparse.ArgumentParser(description='This is an alogrithm testing script')
parser.add_argument("-a", "--algo", help="Algorithm to be tested")
parser.add_argument("-t", "--tests", help="Tests json file")
parser.add_argument("-r", "--results", help="Results json file")
parser.add_argument("-l", "--language", help="Programming language of the algorithm")

args = parser.parse_args()

result, stats = CheckerController.main_check(tested_file=args.algo, results_file=args.results, tests_file=args.tests, language=args.language)

print(*result, sep="\n")
print("\n")
print(f"Success: {stats['success']} Fail: {stats['failed']}\nSuccess rate: {stats['success']}/{stats['success'] + stats['failed']}")
