'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/oneshan/foobar/blob/master/ion_flux_relabeling/solution.py"


def answer(h, q):
    ans = [-1] * len(q)
    max_v = (1 << h) - 1

    def getPid(h, target, bias):
        max_v = (1 << h) - 1
        max_hv = max_v // 2
        # target == left node
        if target == max_hv + bias:
            return max_v + bias
        # target == right node
        elif target == (max_hv << 1) + bias:
            return max_v + bias
        # target in left subtree
        elif target < max_hv + bias:
            return getPid(h - 1, target, bias)
        # target in right subtree
        else:
            return getPid(h - 1, target, bias + max_hv)

    for idx, elem in enumerate(q):
        if elem < max_v:
            ans[idx] = getPid(h, elem, 0)

    return ans
