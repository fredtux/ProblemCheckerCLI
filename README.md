# Algorightm checker
The current checker works for Python, PHP and JavaScript _(Node.js)_ only but can be extended for any language

Note that you must have the interpreter for each language already installed

## Usage
For testing purposes the _"testing"_ directory was included and contains the following
1. Test cases
    * testcase.py - algorithm for Python
    * testcase.php - algorithm for PHP
    * testcase.js - algorithm for JavaScript

2. Tests
    * tests.json - contains 2 tests for the test case files

3. Results
    * results.json - contains the results (NOTICE: the first result is correct but the second is incorrect for testing purposes)

### 1. Using arguments
```bash 
    python tester.py --algo testing/testcase.py --tests testing/tests.json --results testing/results.json --language python
```
### 2. Using questions
```bash
    python tester.py
```