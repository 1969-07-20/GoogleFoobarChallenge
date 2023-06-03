'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/kshitijjagatkar/Google-s-FooBar-Challenge-/blob/main/The%20cake%20is%20not%20a%20lie.py"


#!/usr/bin/env python
# coding: utf-8

# In[2]:


def solution(s):
    """ Very first step is 
         1.loop through the string a letter by letter.
         
         Here we are using .count() function because it provides what we actually wants that
         
         - It trace the non -repeating pattern in the string and returns it's no of occurances.
           then the logic becomes so simple we are taking one letter at a time(s[:x]) and multiplying 
           this collected string with it's occurances(.count([:x])) in the original string(==s)
           
           eg. 1st loop: a*occurances == original string? and when we hit pattern i.e. in this case: 
               ab*occurances == OG string. we will return the count.
               
         2. second if is optional step. I just wrote cause my 2,3 cases were failing. thought this might help
             :It just check the lenght of the pattern we found is equal to the the pattern at the end. it's not so
              necessary cause all work was done by the count fun. I was confused by those hidden tests
         
         3. These were the hidden test that confused me lot and then finally found it.
             1st one is empty string if they pass
             2nd one is the string which has no pattern
          
          And, here you pass the first fooBar challenge with very simple solution."""
        
    for x in range(len(s)):
        if s[:x]*s.count(s[:x])==s:
            string = s[:x]
            if s[len(s)-len(string):len(s)]==s[:x]:
                return s.count(s[:x])
    if s=='':
        return 0
    if s[:x]*s.count(s[:x])!=s:
        return 1
