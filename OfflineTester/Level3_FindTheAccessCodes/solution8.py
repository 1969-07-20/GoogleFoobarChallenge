'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gist.github.com/christophercrouzet/421fc9bdf646c93d099c109d6740cea1"


#  Mod:
#  - Changed xrange() to range()


#!/usr/bin/env python2.7

"""Find the Access Codes
In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need
access to it. But the only door leading to the LAMBCHOP chamber is secured with
a unique lock system whose number of passcodes changes daily. Commander Lambda
gets a report every day that includes the locks' access codes, but only she
knows how to figure out which of several lists contains the access codes. You
need to find a way to determine which list contains the access codes once
you're ready to go in.
Fortunately, now that you're Commander Lambda's personal assistant, she's
confided to you that she made all the access codes "lucky triples" in order to
help her better find them in the lists. A "lucky triple" is a tuple (x, y, z)
where x divides y and y divides z, such as (1, 2, 4). With that information,
you can figure out which list contains the number of access codes that matches
the number of locks on the door when you're ready to go in (for example, if
there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access
codes).
Write a function answer(l) that takes a list of positive integers l and counts
the number of "lucky triples" of (lst[i], lst[j], lst[k]) where i < j < k.
The length of l is between 2 and 2000 inclusive.  The elements of l are between
1 and 999999 inclusive.  The answer fits within a signed 32-bit integer. Some
of the lists are purposely generated without any access codes to throw off
spies, so if no triples are found, return 0.
For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6],
[1, 3, 6], making the answer 3 total.
Note
----
    This solution won't pass the test because deemed too slow.
"""

from bisect import insort_left
from itertools import combinations


def answer(l):
    indices = {}
    setdefault_ = indices.setdefault
    for i, x in enumerate(l):
        setdefault_(x, []).append(i)

    out = 0
    highest_value = max(l)
    for i, x in enumerate(l):
        multiples = []
        for m in range(1, int(highest_value / x) + 1):
            if x * m in indices:
                for j in indices[x * m]:
                    if i < j:
                        insort_left(multiples, (j, x * m))

        if multiples:
            multiples = [m[1] for m in multiples]
            for pair in combinations(multiples, 2):
                out += pair[1] % pair[0] == 0

    return out
