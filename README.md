# constant-checker-Pylint
A Pylint checker to check conventional Python CONSTANT variables

To use this checker, please install Pylint and Python 3.7+\
Then put the constant_checker.py into the the Pylint package path /pylint/checkers/ \
Follow the instructions at Pylint.ory

I provide my test file `test_constant.py`, which is transformed from a simple caesar cipher implementation provided at the [Pylint Tutorial page] (https://pylint.pycqa.org/en/latest/tutorial.html)

Use

    pylint --disable=all --enable=constant-value-change test_constant.py

to run Pylint with only constant checker

Note: 
All test results were produced under

    pylint 2.12.2 (with default configuration)
    astroid 2.9.0
    Python 3.9.7
