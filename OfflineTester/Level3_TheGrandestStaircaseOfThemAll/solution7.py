# -*- coding: utf-8 -*-

'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/wrbyepct/The-grandest-staircase-of-them-all/blob/master/solution/solution_revised.py"


#  Mod:
#  - convert answer to int upon return


"""
Informal Structured Outline



Problem type:
    Behavior spotting


The gist of the problem:
    Simply find out how many possible stair variations given any bricks


Input range:
    bricks ≥ 3


Concerned target:
   How many possible variations on n steps stair?
       E.g. if the bricks can form at most 3-step stair
                then you have to know how many 2-step and 3-step stair variations respectively
            If it is 4-step stair at most, then it's 2-step + 3-step + 4-step



Goal:
     Find the formula to describe the stair behavior



What we have known:
    1. We know for 2-step stair, it's fairly easy, for example:
            If given 10 bricks, 2-step possible stairs are:
                9, 1
                8, 2
                7, 3
                6, 4

    2. In fact, we can find 2-step stair variation pattern is like the following:
               Bricks    3  4  5  6  7  8  9  10
        ------------------------------------------
           Variations    1  1  2  2  3  3  4   4

    3. Looks like the growth rate of the variation(V) is half of the bricks(B):
            B: 8 - 3 = 5          B: 9 - 3 = 6
            V: 3 - 1 = 2          V: 4 - 1 = 3

    4. So we can get the formula of 2-step is:
            //  Half of the distance plus the stating value: 1
            V = roundDown((B - 3) / 2) + 1

    5. But what if we want to know its 3-step variation?
        E.g.
            Given 10 bricks, what's the 3-step variation count?
                We can imagine it's just 2-step variation of 7 brick sit on top a 3 bricks base:
                    Looks like this:
                        #
                        ##
                        ##
                        ##
                        ###
                But what about an example like this?
                        #
                        #
                        ##
                        ###
                        ###
                Again, it's like 2-step variation of 4 bricks sit on top a 3 bricks base,
                which is 1.
    6.  But can we go further? Like 2-step variation of 1 brick?
        E.g.
            #
            ###
            ###
            ###
            This is an illegal stair.
            So no such thing is 2-step of 1 brick, and so is 2-step of 2 bricks

    7.  So now we know: If we want to know 3-step variation of 10 bricks, the pattern would be like this:
            3Step(10) = 3Step(7) + 2Step(7)
            3Step(7)  = 3step(4) + 2Step(4)
            3step(4)  = 4 - 3 < 3 -> impossible stair = 0
            2Step(7)  = roundDown((7 - 3) / 2) + 1 = 3
            2Step(4)  = roundDown((4 - 3) / 2) + 1 = 1
            3Step(10) = 1 + 3 = 4

    8.  The 3-step pattern goes the same with 4-step and up:
        E.g.
            4Step(10) = 4Step(6) + 3Step(6)
            4Step(6) = 6 - 4 < 3 -> impossible stair = 0
            3Step(6) = 3Step(3) + 2Step(3)
            3Step(3) = 3 - 3 < 3 -> impossible stair = 0
            2Step(3) = 1
            4Step(10) = 0 + 1 = 1

    9.  The general formula non-2-step stair counts can be written like this:
            V: variations
            B: Bricks
            S: Steps
            V(B, S) = V(B - S, S) + V(B - S, S - 1)



Conclusion:
    This will be a recursive formula, basically it keeps asking the previous bricks to get the 2-step variation
    There are 2 main formula:
        b: number of bricks
        s: specific n-step stair variation
        v: The variation of given n step
        1. 2-step variation:
            when s = 2
            v = roundDown((b - 3) / 2) + 1
        2. n-step variation:
            when s > 2
            v = variation(b - s, s) + variation(b - s, s - 1)
            E.g.
                If we were to find the 4-step variations of 21 bricks, it would be
                v = variation(21 - 4, 4) + variation(21 - 4, 3)
                Which means if you want to find 4-step variations of 21 bricks,
                    you will have to find 4-step variations of 17 bricks and 3-step variation of 17 bricks



Must do in order to achieve the goal:

    First, if given n brick, we have to know the max step variations it can build
             E.g.
                If given 19 bricks, the max step is 5
    Second, There some cases need to be addressed:
            Given b bricks and ask for s step variation:
            1. If we are asking for s = 2 steps variations -> roundDown((b - 3) / 2) + 1
            2. If we are asking for s ≥ 2 steps variations ->
                a. If the s step is not possible to build by b - s bricks -> variation(b - s, s - 1)
                    E.g.
                        Given 10 bricks and ask for 4-step variation:
                            so we would need count of 4-step of 6 and 3-step of 6
                                and the former is not possible
                                but the latter is always possible
                b. If the s step is possible to build by b - s bricks -> variation(b - s, s) + variation(b - s, s - 1)


    Finally, because this is a recursive function, it will grow to too many stacks if the n becomes large
    Instead of just calculating it recursively, it's better to build stair counts from start

    The way to achieve it is to create a list to keep the record of every step count
    E.g.
        3 bricks -> { 2-step:1, 3-step:0 }
        10 bricks -> { 2-step:4, 3-step: 4, 4-step: 1}


===============================================================



Formal Description


-------------Definitions--------------
stair_record: Dict  // The dictionary of bricks, records the step variations of the bricks
                        E.g. The  count of the 10 bricks will be the following
                                { 10: { 2: 4, 3: 4, 4: 1} }

least_brick: Dict  // The record of the minimum amount of bricks to build the specified step variation
GivenBricks: Int
bricks: Int
max_steps: Int
steps: Int
count: Int
variation(bricks, steps):
    IF
       steps = 2 -> roundDown((bricks - 3) / 2) + 1

       steps > 2 ->
       IF
           // The first condition means the specified step variation is impossible for this amount of bricks
            E.g.
                4-step variation is impossible for 7 bricks to build
                but 3-step variation is possible
           steps ∉ stair_record[bricks - steps] ->
                stair_record[bricks - steps][steps - 1]

           steps ∈ stair_record[bricks - steps] ->
                stair_record[bricks - steps][steps] + stair_record[bricks - steps][steps - 1]
       FI
    FI

---------------Steps-------------------
stair_record := { 3: { 2:1 }, 4:{ 2:1 }, 5:{ 2:2 } }; // Build the basic bricks record like 3, 4, 5 bricks
n := GivenBricks;
bricks := 6;
count := 3;
max_steps := 3;

{ bricks < n ∧ count = { Σ steps| 2 ≤ steps ≤ max_steps: variation(bricks, steps) } }
DO bricks < n:

    stair_record[bricks] := {};   // In python you have to assign it as dictionary first
    s := 2;
    { s ≤ max_steps ∧ { ∀i | 2 ≤ i < s: stair_record[bricks][i] = variation(brick, s) }
    DO s ≤ max_steps:
        stair_record[bricks][s] := variation(bricks, s);
        s := s + 1
    OD
                      // It means that every step variation of  the bricks have record now
    { s > max_steps ∧ { ∀i | 2 ≤ i < s: stair_record[bricks][i] = variation(bricks, s) };
    bricks := bricks + 1;
    max_steps := maxStep(bricks);
    count := { Σ steps| 2 ≤ steps ≤ max_steps: variation(bricks, steps) }
OD
{ bricks = n  ∧ count = { Σ steps| 2 ≤ steps ≤ max_steps: variation(bricks, s) } }

"""
from math import floor

stair_record = {3: {2: 1}, 4: {2: 1}, 5: {2: 2}}


def solution(bricks):
    # If it just asks for basic bricks simply return the basic answer
    # So we don't need to waste time calculating all the stuff
    if bricks == 3 or bricks == 4:
        return 1
    if bricks == 5:
        return 2

    # If it's 6 or more, let's calculate all the brick variation one by one
    # and restore them in the record
    # so when we calculate a new brick variations, we can simply draw the answers from the record
    for b in range(6, bricks + 1):
        ms = get_max_steps(b)
        stair_record[b] = {}
        for s in range(2, ms + 1):
            stair_record[b][s] = variation(b, s)

    return int(sum(stair_record[bricks].values()))


def variation(bricks, steps):
    if steps == 2:
        return floor((bricks - 3) / 2) + 1

    # If the step variation doesn't exit in for the amount of the bricks
    # I.e. There's no 3-step variation for only 3 bricks, so we just skip it and draw the answer from 2-step of 3
    if steps not in stair_record[bricks - steps]:
        return stair_record[bricks - steps][steps - 1]

    return stair_record[bricks - steps][steps] + stair_record[bricks - steps][steps - 1]


def get_max_steps(bricks):
    # Get the maximum steps the bricks can build
    bricks = bricks - 3
    steps = 3
    # If this check is false, then it means the bricks is currently not enough to build a base by this amount of bricks
    # So we subtract the step by 1 is the answer
    while bricks >= steps:
        bricks -= steps
        steps += 1
    return steps - 1
