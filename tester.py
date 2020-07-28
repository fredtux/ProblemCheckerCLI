from Controller.CheckerController import CheckerController
from sys import argv

if len(argv) >= 2:
    tested_file = argv[1]
else:
    tested_file = None

if len(argv) >= 3:
    results_file = argv[2]
else:
    results_file = None

CheckerController.main_check(tested_file, results_file)
