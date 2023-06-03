# Offline Tester
This directory contains the code and supporting files for an offline tester for solutions to the
Google Foobar Challenge.  It runs under Python 2.7 and Python 3.10.

Offline Tester runs at the command line and generates text output.

```
python3 offline_tester.py
```
or

```
python2 offline_tester.py
```

#  Principle Command Line Argument
All command line arguments are optional.  The following is the argument most likely to be used under normal usage.

```
--challenge=<comma-separated list of challenges | ALL>
```

#  Overview of Contents

There is a subdirectory for each Foobar challenge.  In each directory will be a set of files with names of
the form 'solutionX.py'.  These are the solutions for that challenge.  There are two additional files
called 'solutions.json' and 'testCases.json'.  Offline Tester reads these JSON files to determine which
solutions to run ('solutions.json') on what test cases ('testCases.json').

##  Test Cases

As checked out from the repo, the 'testCases.json' files in the OfflineTester directory are stubs.  The only
test cases are those test cases that appear in the Google Foobar Challenge problem statements.
**These stub 'testCases.json' files should be replaced by the corresponding 'testCases.json' files in the
[ChallengesAndSolutions](https://github.com/1969-07-20/GoogleFoobarChallenge/tree/master/ChallengesAndSolutions)
directory in order for the Offline tester to exercise the full suite of test cases.**

#  Adding a New Solution

##  Add code to package (directory) for the challenge

Put the code in a new module (file) for the challenge.  For example, to test a new solution to the
Braille Translation challenge, put the new code in a file similar to './Level1_BrailleTranslation/solution0.py'.
('solution0.py' is an arbitrary choice for file name.  Offline Tester will accept any reasonable file name as
long as it is located in the directory dedicated to the challenge e.g. '/Level1_BrailleTranslation/'.)

Offline Tester requires two things from the module.

1. A function the tester can call.  The function is typically called 'solution()' or 'answer()', but Offline Tester will accept any function name.
2. A variable 'source_url' containing a string, even a zero length one.  Offline Tester will print out string as a means of communicating to the user where the solution came from.

The following is a notional solution for adding two numbers.

```
source_url = "https://example.com/foobar.py"

def solution(a, b):
    return(a + b)
```

##  Add entry for new solution to 'solutions.json'

The contents of 'solutions.json' provide information about the solutions to be run.  Offline Tester will
attempt to run any solution with an entry in 'solutions.json'.  Any solution which does not have an
entry in the challenge's 'solutions.json' file is ignored.

The following is an example of a solutions.json entry.:

```
    {
        "file":   "Level1_BrailleTranslation.solution0",
        "entry":  "solution",
        "dep":    ["numpy"]
    },
```

1. The 'file' field tells the Offline Tester the solution's code is located in the file './Level1_BrailleTranslation/solution0.py' relative to the current working directory.  .
2. The 'entry' field tells the Offline Tester to call the function 'solution()' with the arguments containing the inputs to the challenge.
3. The 'dep' field tells the Offline Tester which packages external to the standard python distribution that this solution requires.  If the online tester cannot load any package in this list it will not attempt to execute this solution.  Currently, numpy is the only external package that Offline Tester supports.


#  How to Add New Test Cases

Each test case has a separate entry in the 'testCases.json' file.  The following is an example for the corner case
of a zero-length string for the Braille Translation challenge.

```
    {
        "desc": "Corner case:  zero length input",
        "source": "https://github.com/1969-07-20/GoogleFoobarChallenge",
        "input": [""],
        "output": ""
    },
```

1.  The 'desc' field is a description of the test for the user's benefit.  Offline Tester includes this in the text output for the test case but otherwise ignores it.
2.  Similar to the 'desc' field, the 'source' field is used to communicate to the user where the test case came from.  Other than including it in the printout for the test case, Offline Tester ignores it.
3.  The 'input' field is a list of the arguments for the test case passed to the solution.  This list must be present and all arguments must be items in this list.  In the above example, the list has a single element, a zero-length string.
4.  The 'output' field is the correct output.  Offline Tester compares the result returned from the solution to the contents of the 'output' field.  If they are the same, then the Offline Tester considers the solution to have succeeded.  If they are different, Offline Tester considers
it to be a failure.

NOTE:  The contents must be well-formed JSON.  The JSON reader used during development of the Offline Tester was much
pickier than Python.  For example, the JSON reader required strings to be delimited by double quotes (") and not single
quotes (') and no comma after the last item in a list.
