'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://rajat19.github.io/foobar/elevator-maintenance"


class Elevator:
    def __init__(self, elevator):
        div = list(map(int, elevator.strip().split('.')))
        self.str = elevator
        self.major = div[0]
        self.minor = div[1] if len(div) > 1 else -1
        self.revision = div[2] if len(div) > 2 else -1

    def __lt__(self, other):
        if self.major < other.major: return True
        if self.major > other.major: return False
        if self.minor < other.minor: return True
        if self.minor > other.minor: return False
        if self.revision < other.revision: return True
        if self.revision > other.revision: return False


def solution(l):
    els = []
    for elevator in l:
        els.append(Elevator(elevator))
    els.sort()
    return [el.str for el in els]
