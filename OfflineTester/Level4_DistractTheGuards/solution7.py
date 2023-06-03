'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://gist.github.com/hariketsheth/ea73398e4e4c2f9ca0b5f519ed695fee"


#  Mod:
#  - Changed xrange() to range()
#  - Changed answer to integer upon return to caller


"""
Distract the Trainers
=====================

The time for the mass escape has come, and you need to distract the bunny trainers so that the workers can make it out! Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the trainers are fond of bananas. And gambling. And thumb wrestling.

The bunny trainers, being bored, readily accept your suggestion to play the Banana Games.

You will set up simultaneous thumb wrestling matches. In each match, two trainers will pair off to thumb wrestle. The trainer with fewer bananas will bet all their bananas, and the other trainer will match the bet. The winner will receive all of the bet bananas. You don't pair off trainers with the same number of bananas (you will see why, shortly). You know enough trainer psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of trainers will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose interest and go back to supervising the bunny workers, and you don't want THAT to happen!

For example, if the two trainers that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to training bunnies.

How is all this useful to distract the bunny trainers? Notice that if the trainers had started with 1 and 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

Now your plan is clear. You must pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb wrestling loop!

Write a function solution(banana_list) which, given a list of positive integers depicting the amount of bananas the each trainer starts with, returns the fewest possible number of bunny trainers that will be left to watch the workers. Element i of the list will be the number of bananas that trainer i (counting from 0) starts with.

The number of trainers will be at least 1 and not more than 100, and the number of bananas each trainer starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(1,1)
Output:
    2

Input:
solution.solution([1, 7, 3, 21, 13, 19])
Output:
    0

-- Java cases --
Input:
solution.solution(1,1)
Output:
    2

Input:
Solution.solution([1, 7, 3, 21, 13, 19])
Output:
    0
"""
class Graph:
    def __init__(self,banana_list):
        self.list_len = len(banana_list)
        self.graph = list([0]*self.list_len for i in range(self.list_len))
        for i in range(self.list_len):
            for j in range(self.list_len):
                if i < j: 
                    self.graph[i][j] = self.dead_lock(banana_list[i], banana_list[j])
                    self.graph[j][i] = self.graph[i][j]  

    def gcd(self, x, y):
       while(y): x, y = y, x % y
       return x

    def dead_lock(self, x,y):
        if x == y: return 0
        l = self.gcd(x,y)
        if (x+y) % 2 == 1: return 1
        x,y = x/l,y/l
        x,y = max(x,y), min(x,y)    
        return self.dead_lock(x-y,2*y)

    def bpm(self, u, matchR, seen):
        for v in range(self.list_len):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True
 
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False

    def maxGaurdPair(self):
        matchR = [-1] * self.list_len
        result = 0
        for i in range(self.list_len):
            seen = [False] * self.list_len
            if self.bpm(i, matchR, seen):
                result += 1
        return self.list_len- 2*(result/2)


def solution(l):
    return int(Graph(l).maxGaurdPair())
