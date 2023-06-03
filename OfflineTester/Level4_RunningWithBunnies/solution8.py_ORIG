'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://www.derekmoran.dev/software-development/google-foobar-level-4a"


# Author: Derek Moran, Level 4, Bunny Planet Rescue Service
# With big thanks and kudos to Google software engineer William Fiset; his video series on graph algorithms was invaluable for this solution
# Date: 08-DEC-2022

def solution(times,times_limit):
    # Your code here
    return getMaxBunniesWeCanRescueWithinTimeLimit( times, times_limit )

# When given an adjacencyMatrix:
# - such that each column will indicate the time it takes to get to the start, first bunny, second bunny, ..., last bunny, and the bulkhead in that order
# - the order of the rows follows the same pattern (start, each bunny, bulkhead)
# - we can escape only through the bulkhead, and only when there is 0 or more time units remaining
# - times must be integers, note they can be positive OR negative ( bulkhead opens again if a negative route puts it back to 0 )
# - Infinite can also be used if a particular route is not possible
# - there can be at most 5 bunny rows
#
# And given a timeLimit that is a non-negative integer that is at most 999 time units
#
# Then this will return a list containing the maximum number of bunnies that can be visited prior to escaping, sorted by lowest bunny workerId
# The bunny workerIds start at 0 ( i.e. are their row index - 1 )
# If multiple sets of the same size are possible, the result will favour the one starting with lowest workerIds
def getMaxBunniesWeCanRescueWithinTimeLimit( adjacencyMatrix, timeLimit ):

    validateInputs( adjacencyMatrix, timeLimit )

    bulkheadIndex = len(adjacencyMatrix) - 1
    numBunnies = bulkheadIndex - 1

    # We can tell how many bunnies we have from the original matrix, so let's bail early if we have the chance!
    if numBunnies == 0: return []

    # We don't need the original matrix any more, so will just convert it in place to avoid additional memory complexity
    convertAdjacencyMatrixToAllPairsShortestPaths( adjacencyMatrix )

    startIndex = 0
    # If we can't reach the bulkhead from the start then no point going further
    if adjacencyMatrix[startIndex][bulkheadIndex] > timeLimit: return []

    rangeOfBunnyIndexes = range( startIndex + 1, bulkheadIndex )

    # Using dictionary entry allBunniesSaved[1] as a workaround to get similar functionality to a nonlocal bool
    # ( Python 2.7.13 does not support assignment to a bool with a nonlocal closure )
    allBunniesSaved = {}

    def getMaxBunniesWeCanRescueWithinTimeLimit( currentNode, timeTakenSoFar, bunniesVisitedSoFar, bunniesSavedSoFar ):

        if 1 in allBunniesSaved: return bunniesSavedSoFar
        elif len(bunniesSavedSoFar) == numBunnies:
            allBunniesSaved[1] = True
            return bunniesSavedSoFar

        maxBunniesSavedTotal = list(bunniesSavedSoFar)

        for nextBunnyIndex in rangeOfBunnyIndexes:
            if nextBunnyIndex in bunniesVisitedSoFar: continue

            nextBunniesVisitedSoFar = bunniesVisitedSoFar.copy()
            nextBunniesVisitedSoFar.add(nextBunnyIndex)

            timeToReachNextBunny = adjacencyMatrix[currentNode][nextBunnyIndex]
            timeToEscapeWithNextBunny = adjacencyMatrix[nextBunnyIndex][bulkheadIndex]

            if timeTakenSoFar + timeToReachNextBunny + timeToEscapeWithNextBunny > timeLimit: continue

            nextBunniesSaved = list(bunniesSavedSoFar)
            nextBunniesSaved.append(nextBunnyIndex-1)

            maxBunniesIfWeSaveNextBunny = getMaxBunniesWeCanRescueWithinTimeLimit(
                currentNode = nextBunnyIndex,
                timeTakenSoFar = timeTakenSoFar + timeToReachNextBunny,
                bunniesVisitedSoFar = nextBunniesVisitedSoFar,
                bunniesSavedSoFar = nextBunniesSaved
            )

            # Note that since we are trying bunnies with lowest id first, we will get the set we want even if others with the same size exist
            if len(maxBunniesIfWeSaveNextBunny) > len(maxBunniesSavedTotal): maxBunniesSavedTotal = maxBunniesIfWeSaveNextBunny

        return maxBunniesSavedTotal

    maxBunniesWeCanRescueWithinTimeLimit = getMaxBunniesWeCanRescueWithinTimeLimit(
        currentNode = startIndex,
        timeTakenSoFar = 0,
        bunniesVisitedSoFar = set(),
        bunniesSavedSoFar = []
    )

    maxBunniesWeCanRescueWithinTimeLimit.sort()
    return maxBunniesWeCanRescueWithinTimeLimit

Infinite = float('inf')
NegativeInfinite = float('-inf')

# Transforms the given adjacencyMatrix into one that gives all-pairs-shortest-paths
# Use Infinite to represent an edge that cannot be crossed
# NegativeInfinite will be used to represent edges caught in a negative cycle
#
# This is a version of the Floyd-Warshall algorithm - one explained in fantastic detail in a video series by Google software engineer William Fiset
def convertAdjacencyMatrixToAllPairsShortestPaths( adjacencyMatrix ):

    # Let intermediateNode be a potential node in the shortest path from sourceNode to destinationNode
    # If the path through intermediateNode turns out to be shorter, then update to that shorter path
    # Do this times the number of nodes to ensure any path size reductions propagate through
    # At this point we'll do a second pass. If a path through intermediateNode turns out to still be shorter, then we must have a negative cycle
    # If we do have a negative cycle, then update that path to NegativeInfinite to represent this case
    # Do this times the number of nodes to ensure any negative cycles propagate through
    rangeOfNodes = range( len(adjacencyMatrix) )
    for reductionPass in [1, 2]:
        for intermediateNodeIndex in rangeOfNodes:
            for row in rangeOfNodes:
                for col in rangeOfNodes:
                    pathLengthViaIntermediateNode = adjacencyMatrix[row][intermediateNodeIndex] + adjacencyMatrix[intermediateNodeIndex][col]
                    if pathLengthViaIntermediateNode < adjacencyMatrix[row][col]:
                        adjacencyMatrix[row][col] = pathLengthViaIntermediateNode if reductionPass == 1 else NegativeInfinite

def validateInputs( adjacencyMatrix, timeLimit ):
    if not type(timeLimit) is int or timeLimit < 0 or timeLimit > 999:
        raise Exception( "timeLimit must be a non-negative integer that is at most 999" )

    adjacencyMatrixExceptionMessage = "The adjacencyMatrix must be a square matrix of integers ( or Infinite if an edge is disconnected ); "\
        "the size must be at least 2 ( ie there must be at least a starting point and the bulkhead ) and no more than 7 ( ie 0-5 optional bunnies )"
    numMatrixRows = len(adjacencyMatrix)
    if numMatrixRows < 2 or numMatrixRows > 7:
        raise Exception( adjacencyMatrixExceptionMessage )

    for row in range(numMatrixRows):
        col = adjacencyMatrix[row]
        colLength = len(col)
        if colLength != numMatrixRows: raise Exception( adjacencyMatrixExceptionMessage )
        for col in range(colLength):
            colValue = adjacencyMatrix[row][col]
            if not type(colValue) is int and not ( type(colValue) is float and colValue in [Infinite, NegativeInfinite] ):
                raise Exception( adjacencyMatrixExceptionMessage )
