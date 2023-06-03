'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/Burke0/Foobar-Challenge-Elevator-Maintenance/blob/main/solution.py"


# The solution function takes a list of elevator versions as input and returns the sorted list.
# It uses a version_key function to convert each version string into a tuple of integers, where each integer represents the major, minor, and revision number of the version. 
# This key function is then used to sort the input list using the built-in sorted function.
# The version_key function works by splitting the version string into its parts using the split method, and then mapping the parts to integers using the map function. Finally, it returns a tuple of the integer parts.
# This solution should work for all valid inputs within the constraints given in the problem statement.

def solution(l):
    def version_key(version):
        parts = version.split('.')
        return tuple(map(int, parts))
    return sorted(l, key=version_key)
