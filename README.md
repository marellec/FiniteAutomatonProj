

This finite automaton is written in Python.
It has been tested on macos 12.5.1.
For the purposes of the assignment, the folder path is: 

        '/tmp/marelle-leon'

### EXECUTABLE

1. create executable

        $ python -m pip install -e /tmp/marelle-leon/FiniteAutomatonProj

2. run finite automaton

        $ FAInteractive

3. run random passcode cracking

        $ RCInteractive

### UNIT TEST COVERAGE

1. if you don't already have the python coverage module intalled, run this:

        $ python -m pip install coverage

2. enter project directory

        $ cd FiniteAutomatonProj

3. run tests

        $ coverage run -m unittest discover

4. view coverage

        $ coverage report


## WHAT IT DOES

This finite automaton will lock/unlock when given the correct passcode and lock/unlock code within a string of characters, read left to right.
The random cracking program brute forces the passcode and unlock code without knowing the length and by guessing random numbers with equal probability 0-9.

### INFO

Author: Marelle Leon
