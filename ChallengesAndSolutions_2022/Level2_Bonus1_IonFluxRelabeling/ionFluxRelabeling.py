"""
The code in this file computes answers to the Ion Flux Relabeling challenge.
The function solution(h, l) is called with argument 'h' which is an integer
with the height of the binary tree and list 'l' with a list of entries for
which the function needs to find the parent.

The following observations facilitate the solution presented here.

0) Perfect binary trees of height h can be recursively constructed from two
   perfect binary sub-trees of height h-1 by taking a root node and making two
   copies of binary sub-trees of height h-1 the left and right sub-trees,
   respectively, then strategically relabeling.

   Each node in the right sub-tree is relabeled by adding the value of the
   label of the root of the left sub-tree.  The root is labeled by adding one
   to the root of the right sub-tree.

   A consequence of the recursive manner in which a perfect binary tree can be
   constructed is that most properties that apply to a binary tree apply to
   both the left and right sub-trees and vice versa.

1) The label of the root of any sub-tree is greater than the label in either
   of its sub-trees.  Moreover, all values in any right sub-tree are greater
   than the all values in the left sub-tree.

   Therefore, starting at the root of the perfect binary tree, any entry can
   be located by comparing the value we are trying to locate and the current
   node in the sub-tree.

2) For a perfect binary (sub-)tree of height h, with label n, the label of
   the right sub-tree is n-1 and the label of the left sub-tree is n-2^(h-1).

   The labels of the roots of the left and right sub-trees are trivially
   calculated, knowing only their heights.

The above properties are the foundation for the simple solution to the Ion Flux
Relabeling challenge here.  For each, entry in the list, start at the root of
the binary tree and traverse the tree until the entry in question is found.  The
parent is the previously visited node.

The above observations mean that the tree does not need to be constructed.  For
any given node, it is easy to compute the labels of its child nodes and to know
which node is next in the path to the target node.
"""

def find_parent(tree_height, tgt_entry):
    """Function find_parent() finds the parent of 'tgt_entry' in a post-order
    traversal labeled perfect binary tree if height 'tree_height'."""

    #  Initialize variables for traversing tree
    cur_entry = int((1 << tree_height) - 1)
    prv_entry = -1

    tree_level = tree_height - 1

    #  Traverse tree from root level to leaf level looking for target entry
    while 0 <= tree_level:

        #  Check if the target leaf has been found
        if cur_entry == tgt_entry:
            return prv_entry
        else:
            prv_entry = cur_entry

        #  Create power of two for this level
        power_of_two = int(1 << tree_level)

        #  Determine which branch of the tree to take
        if (cur_entry - power_of_two) >= tgt_entry:
            cur_entry = cur_entry - power_of_two
        else:
            cur_entry = cur_entry - 1

        #  Decrement level
        tree_level = tree_level - 1

    #  Arrived at leaf, return parent
    return prv_entry


def solution(tree_height, entry_list):
    """Function solution() finds solutions to the 'Ion Flux Relabeling' Google
    Foobar challenge.  For each entry in 'entry_list' it finds the parent in
    a post traversal ordered binary tree and returns the result in list
    'result'."""

    result = []

    #  Loop over entries in 'entry_list' and add their parents to list 'result'.
    for e in entry_list:
        result.append(find_parent(tree_height, e))

    return result
