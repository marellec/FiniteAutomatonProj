

This finite automaton is written in Python.

For the purposes of the assignment, the folder path is:

    /tmp/marelle-leon




/* EXECUTABLE */


// create executable

    1. $ pip install -e /tmp/marelle-leon/FiniteAutomatonProj

// run finite automaton

    2. $ FAInteractive

// run random passcode cracking

    3. $ RCInteractive



/* UNIT TEST COVERAGE */


// If you don't already have the python coverage module intalled, run this:

    1. $ pip install coverage

// enter project directory

    2. cd FiniteAutomatonProj

// run tests

    3. $ coverage run -m unittest discover

// view coverage

    4. $ coverage report

