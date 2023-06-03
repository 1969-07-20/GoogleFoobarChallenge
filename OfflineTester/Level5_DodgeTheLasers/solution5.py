'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://www.derekmoran.dev/software-development/google-foobar-level-5-finale"


#  Mod:
#  - force input to string to avoid code complaining about unicode input


# Author: Derek Moran, Level 5, Saboteur and Escape Artist for Bunny Planet
# With big kudos to whoever came up with this problem, THANK YOU!
# All of the problems have been fun, but this one was especially so. It was just such an absolute blast :-)
# Date: 18-DEC-2022
def solution(s):
    # Your code here
    return getTargetPositionAsString( str(s) )
# Given we have:
# - a target with an acceleration of sqrt2
# - the target velocity at each time 'timeStep' is subjected to a floor() operation
#
# Then returns the position of the target at the given timeStep
# ie: floor(sqrt2) + floor(2sqrt2) + ... + floor(timeStep*sqrt2)
#
# The input timeStepAsString must be a postive integer ( passed as string ) between 1 and 1e100 inclusive
def getTargetPositionAsString( timeStepAsString ):
    validationError = "timeStepAsString must be a postive integer ( passed as string ) between 1 and 1e100 inclusive"
    if not type(timeStepAsString) is str or not timeStepAsString.isdigit():
        raise Exception( validationError )
    timeStep = int(timeStepAsString)
    if timeStep < MIN_TIME_STEP or timeStep > MAX_TIME_STEP:
        raise Exception( validationError )
    return str( getTargetPosition( timeStep ) )
def getTargetPosition( timeStep ):
    if timeStep == 0: return 0
    # We won't have enough precision if we work in floating point
    # So we use an integer with the decimal shifted by the max possible timeStep
    # Since shifting it back cuts off the decimal portion we will end up with a precise floor( timeStep*sqrt2 )
    velocityAtTimeStep = ( timeStep * SQRT2_x_MAX_TIME_STEP ) // MAX_TIME_STEP
    # If the target had been accelerating at 1 unit/time, then it would reach the same velocity at this time step
    timeStepIfUnitAcceleration = velocityAtTimeStep
    # Since unit acceleration would result in the triangular sum we can quickly have a position for this case
    positionIfUnitAcceleration = ( timeStepIfUnitAcceleration * ( timeStepIfUnitAcceleration + 1 ) ) >> 1
    # But OUR target is accelerating faster than 1 unit/time, at sqrt2 unit/time
    # So it will have gaps any time the velocity of prior step is within ( 1 - sqrt2 ) of the next integer
    # sqrt2 is less than 2 though, and the floor will be pulling it back each step
    # So we know it will never have a gap of more than 1 unit per timeStep
    # Therefore we know how many gaps will exist as compared to our 1 unit/time acceleration case
    numGapsFromUnitAcceleration = timeStepIfUnitAcceleration - timeStep
    # Focus on where the first gap happens; when it goes from 2sqrt2 to 3sqrt2
    # We can see that 2sqrt2 will be ahead of 2 by ( 2sqrt2 - 2 ) before the floor pulls it back
    # What if a target was accelerating such that its position was this same distance behind the next?
    # Such a target must hit every gap since it will always be the same relative distance behind
    # The next is 3sqrt2, so this acceleration that would hit the gaps is 3sqrt2 - ( 2sqrt2 - 2 ) = sqrt2 + 2
    # The velocity would then be floor(timeStep*(sqrt2 + 2))
    # But floor(timeStep*(sqrt2 + 2)) = floor(timeStep*sqrt2) + 2*timeStep, since there is no decimal part to 2*timeStep
    # So our position for a target accelerating such that it hits all the gaps is then:
    # positionIfGapAcceleration
    #  = floor(sqrt2) + floor(2sqrt2) + ... + floor(numGapsFromUnitAcceleration*sqrt2)
    #   + 2*( 1 + 2 + ... + numGapsFromUnitAcceleration )
    # The first part is our original position function, but at a time step of numGapsFromUnitAcceleration
    positionIfGapAcceleration = getTargetPosition( numGapsFromUnitAcceleration )
    # And the second part is just 2 more triangular series that we can easily calculate
    positionIfGapAcceleration += numGapsFromUnitAcceleration * ( numGapsFromUnitAcceleration + 1 )
    # We know that our target position is the unit acceleration position minus any gaps
    # And we now have that position of a target that is accelerating such that it hits all the gaps
    # So, we have an answer!
    targetPosition = positionIfUnitAcceleration - positionIfGapAcceleration
    # This has reduced us from a time of 'timeStep' to a time of 'numGapsFromUnitAcceleration'
    #
    # numGapsFromUnitAcceleration
    #  = timeStepIfUnitAcceleration - timeStep
    #  = velocityAtTimeStep - timeStep
    #  = floor(timeStep*sqrt2) - timeStep
    # We know the floor will make a difference of less than 1
    # So we are roughly reducing from a time of timeStep to a time of ( timeStep*sqrt2 - timeStep )
    #
    # timeStep / ( timeStep*sqrt2 - timeStep )
    #  = 1 / ( sqrt2 - 1 )
    #  = roughly 2.4
    #
    # We know our worst case is MAX_TIME_STEP = 1e100
    # If we were reducing by factor of 2 then we would need log2(1e100)=332 reductions to get the final answer
    # 332 is less than the Python recursion limit of 1000
    # We're doing a bit better at factor of 2.4, so we know we can answer the worst case well within the limit
    return targetPosition
SQRT2_x_MAX_TIME_STEP = int(
    "1"
    "41421356237309504880"
    "16887242096980785696"
    "71875376948073176679"
    "73799073247846210703"
    "88503875343276415727"
)
MIN_TIME_STEP = 1
MAX_TIME_STEP = 10 ** 100
