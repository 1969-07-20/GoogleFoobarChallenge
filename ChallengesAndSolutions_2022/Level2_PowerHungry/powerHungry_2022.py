'''
solution() is a function that, given the power output of each panel in an
array of panels, determines the maximum power output among all subsets of
those panels.  The power output of a subset is the product of the power
output of the individual panels.

solution() takes one argument which is a list with the numeric power output of
all panels in an array.

It is possible that some of the panels individually have negative power
outputs.  However, as long as there are an even number of panels with negative
power outputs, the product is positive and collectively the power contribution
of the panels with negative output is positive.

So the strategy to maximize the power output is to include as many panels
as possible with the exception of excluding panels under the following
conditions:
a) exclude panels with zero output
b) if there are an odd number of panels with negative power output, exclude
   the one panel with smallest magnitude power output in order to make the
   number of panels with negative output even

Assumption:  This algorithm assumes that no panel has a power output with
magnitude greater than zero and less than one.  The inclusion of such panels
would decrease the overall product of power outputs.
'''

from functools import reduce


def solution(panels):

    #  Get lists of the positive and negative panel outputs
    pos_panels = []
    neg_panels = []

    for panel in panels:
        if panel > 0:
            pos_panels.append(panel)
        elif panel < 0:
            neg_panels.append(panel)

    #  Determine the number of panels with positive, negative and zero output
    num_pos = len(pos_panels)
    num_neg = len(neg_panels)
    num_zero = len(panels) - (num_pos + num_neg)

    #  Handle corner cases where positive outputs are not possible
    if (num_pos == 0):
        if (num_zero >= 1):
            if (num_neg <= 1):
                return '0'
        elif (num_neg == 0):
            return '0'
        elif (num_neg == 1):
            return str(neg_panels[0])

    #  Remove one negative panel if there are an odd number
    if (num_neg % 2) != 0:
        neg_panels = sorted(neg_panels)
        neg_panels.pop(-1)

    #  Compute the product of the remaining non-zero panels
    return str(reduce((lambda x, y: x * y), pos_panels + neg_panels))


if __name__ == '__main__':
#   print(solution([2, -3, 1, 0, -5]))
#   print(solution([2, 0, 2, 2, 0]))
    print(solution([-2, -3, 4, -5]))
