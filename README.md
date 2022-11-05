

This finite automaton is written in Python.

For the purposes of the assignment, the folder path is: '/tmp/marelle-leon'




>>> EXECUTABLE



1. ---- create executable

        $ pip install -e /tmp/marelle-leon/FiniteAutomatonProj

2. ---- run finite automaton

        $ FAInteractive

3. ---- run random passcode cracking

        $ RCInteractive




>>> UNIT TEST COVERAGE



1. ---- if you don't already have the python coverage module intalled, run this:

        $ pip install coverage

2. ---- enter project directory

        cd FiniteAutomatonProj

3. ---- run tests

        $ coverage run -m unittest discover

4. ---- view coverage

        $ coverage report

