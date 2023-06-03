'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/narickamez/ion-flux-relabeling/blob/main/flux.py"


# This function recursively calculates the label of a node in a binary tree
# given the label of its parent node, the desired label, and the size of the
# subtree rooted at the parent node.
def cal(head, target, under):
    under = under >> 1 # Divide the size of the subtree by 2
    right = head - 1 # Label of the right child node
    left = head - 1 - under # Label of the left child node
    under -= 1 # Decrease the size of the subtree by 1 (to exclude the parent node)
    if right == target or left == target: # If the target label is a child node, return the parent node's label
        return head
    else: # If the target label is not a child node, recursively search the left or right subtree
        if target <= left:
            return cal(left, target, under)
        else:
            return cal(right, target, under)

# This function solves the ion flux relabeling problem for a binary tree of height h
# and a list of target node labels q.
def solution(h, q):
    head = (1 << h) - 1 # Label of the root node
    result = []
    for i in q: # Iterate over the target node labels
        if head > i >= 1: # Check if the target label is within the binary tree
            result.append(cal(head, i, head - 1)) # Calculate the label of the target node and add it to the result list
        else:
            result.append(-1) # If the target label is outside the binary tree, add -1 to the result list
    return result
