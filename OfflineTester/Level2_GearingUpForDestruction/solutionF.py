'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/40465866/google-foobar-gearing-up-for-destruction/45626410#45626410 (Nader)"


def solutionNader(pegs):
    
    """
        returns the radius of cog i
        ri = Xi -/+ r0
        also sets the ans for the fractional requirement.
    """
    def helper(X,i):
        if i == len(pegs)-1: # last cog, we need to make sure its half of r0
            X = 2*(pegs[i]-pegs[i-1]-X)
            if i%2:
                ans[0],ans[1] = [X,3] if (X)%3 else [X/3,1]
                return X/6.0
            else:
                ans[0],ans[1] = [-X,1]
                return -X/2
        #recursively calculate the radius of next cog
        r_next = helper(pegs[i]-pegs[i-1]-X,i+1) if i>0 else helper(0,1)

        #radius of r = gap bitween the pegs - r of next cog        
        r = pegs[i+1]-pegs[i]-r_next 

        if r < 1: 
            ans[0],ans[1] = [-1,-1]
            raise Exception('Invalid Cog')
        return r

    try:
        ans = [-1,-1]
        helper(0,0)
    finally:
        return ans
