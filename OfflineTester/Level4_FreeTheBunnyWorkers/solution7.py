'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://www.derekmoran.dev/software-development/google-foobar-level-4b"


# Author: Derek Moran, Level 4, Bunny Planet Rescue Service
# With my thanks to Amazon Software Engineer ShuXiang Gao
# While this solution is my own, I gained valuable insights from Gao's blog detailing his own experience with this problem
# Date: 12-DEC-2022
def solution(num_buns, num_required):
    # Your code here
    return getKeyDistribution( num_buns, num_required )
# Given a total number of bunnies numTotalBunnies ( integer between 1 and 9 inclusive )
# And given total number of locks per room numberOfLocksPerRoom ( integer between 0 and 9 inclusive )
# Then returns a specification for the key distribution such that:
# - any set of bunnies of size ( numberOfLocksPerRoom ) can open the locks ( i.e. all the keys they require must be within their set )
# - any set of bunnies of size ( numberOfLocksPerRoom - 1 ) cannot open the locks ( i.e. their set must lack a key )
# The specification will take the form of a matrix where each row contains the keys held by the bunny whose index matches that row
# Keys will be ordered such that first bunny will have keys sequentially starting from 0
def getKeyDistribution( numTotalBunnies, numberOfLocksPerRoom ):
    if not type(numTotalBunnies) is int or numTotalBunnies < 1 or numTotalBunnies > 9:
        raise Exception( "numTotalBunnies must be an integer between 1 and 9 inclusive" )
    if not type(numberOfLocksPerRoom) is int or numberOfLocksPerRoom < 0 or numberOfLocksPerRoom > 9:
        raise Exception( "numberOfLocksPerRoom must be an integer between 0 and 9 inclusive" )
    keyDistributionMatrix = [[] for _ in range(numTotalBunnies)]
    # If we can already tell that no keys are necessary, then let's bail early to avoid the unnecessary processing
    if numberOfLocksPerRoom == 0 or numberOfLocksPerRoom > numTotalBunnies: return keyDistributionMatrix
    # Any set of bunnies of size ( numberOfLocksPerRoom - 1 ) should NOT be able to open the set of locks
    # This implies that any set of bunnies of size ( numberOfLocksPerRoom - 1 ) is lacking one key
    # Yet any set of bunnies of size ( numberOfLocksPerRoom ) SHOULD be able to open the set of locks
    # This implies that adding any remaining bunny to our set of bunnies of size ( numberOfLocksPerRoom - 1 ) gives us that missing key
    # Therefore each lock must have ( numTotalBunnies - ( numberOfLocksPerRoom - 1 ) ) == ( 1 + numTotalBunnies - numberOfLocksPerRoom ) keys
    numberOfKeysPerLock = 1 + numTotalBunnies - numberOfLocksPerRoom
    # We know that each lock has numberOfKeysPerLock keys
    # So let's visit every possible distinct set of bunnies of size numberOfKeysPerLock
    # We'll give the first set of bunnies the full set of keys for the first lock
    #  -> this implies that the set of remaining bunnies will lack the first key
    # Then we'll give the second set of bunnies the full set of keys for the second lock
    #  -> this implies that the set of remaining bunnies will lack the second key
    # Continue this for all the sets we have
    # Now given any set of bunnies of size ( numberOfLocksPerRoom - 1 )
    #  -> the set will always lack one of the keys, and each of the remaining bunnies are the ones that have this key
    #  -> the other possible sets of bunnies of size ( numberOfLocksPerRoom ) will all have at least one of these bunnies in them,
    #     and since we've given one of the other keys to each of those sets, our bunnies must already have the remaining keys
    # Note that we will visit in ascending order of bunnyId and keyId to ensure the ordering requirement
    #
    # Example: numTotalBunnies == 5, numberOfLocksPerRoom == 3
    # Any 2 bunnies must lack a key, so any of the 3 remaining must always have that missing key -> there must be 3 keys per lock
    # So visit every set of 3 bunnies we can make from the 5 and give them a full set of keys:
    #  [0,1,2] -> Give them all key0 ( [3,4] would then lack key0 )
    #  [0,1,3] -> Give them all key1 ( [2,4] would then lack key1 )
    #  [0,1,4] -> Give them all key2 ( [2,3] would then lack key2 )
    #  [0,2,3] -> Give them all key3 ( [1,4] would then lack key3 )
    #  [0,2,4] -> Give them all key4 ( [1,3] would then lack key4 )
    #  [0,3,4] -> Give them all key5 ( [1,2] would then lack key5 )
    #  [1,2,3] -> Give them all key6 ( [0,4] would then lack key6 )
    #  [1,2,4] -> Give them all key7 ( [0,3] would then lack key7 )
    #  [1,3,4] -> Give them all key8 ( [0,2] would then lack key8 )
    #  [2,3,4] -> Give them all key9 ( [0,1] would then lack key9 )
    # Now pick any set of 2 bunnies and it must lack one of the keys; the remaining bunnies are the ones that do have this key
    # Any other set of 3 bunnies must have at least one of these 2 bunnies in it, so our 2 must already have all of the other keys
    bunniesInSet = []
    # Python 2.7.13 does not support assignment to nonlocal int; using this list of size 1 as a workaround to get similar functionality
    lockNumber = [0]
    def distributeKeys( nextBunnyInSet ):
        if len(bunniesInSet) == numberOfKeysPerLock:
            for bunny in bunniesInSet:
                keyDistributionMatrix[bunny].append( lockNumber[0] )
            lockNumber[0] += 1
            return
        for bunny in range( nextBunnyInSet, numTotalBunnies ):
            bunniesInSet.append(bunny)
            distributeKeys( nextBunnyInSet = bunny + 1 )
            bunniesInSet.pop()
    distributeKeys( nextBunnyInSet = 0 )
    return keyDistributionMatrix
