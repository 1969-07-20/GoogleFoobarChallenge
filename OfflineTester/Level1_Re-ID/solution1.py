'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/1969-07-20/GoogleFoobarChallenge/blob/master/ChallengesAndSolutions/Level1_Re-ID/re-ID.py"


#  Determining the specified ID is predicated upon finding the first N primes
#  where is the number of primes required to create the first i+5 characters
#  of the string from which the ID is extracted.  If these primes are known
#  constructing the string and extracting the 5 characters making up the ID
#  is trivial.  Therefore, the bulk of the logic of this program is concerned
#  with finding these primes.

#  This program uses a modified version of the Sieve of Eratosthenes to find
#  primes.  The modifications are intended to both reduce the memory and time
#  complexity of the traditional Sieve of Eratosthenes. This program maintains
#  a sorted list of the next multiples of all primes identified so far.  Primes
#  are identified when there is a gap between the largest multiple processed so
#  far and the smallest unprocessed multiple.

#  When a prime is identified, it is added to the list of primes and twice of
#  the prime is appended to the end of multiples.  Since the new prime is the
#  largest prime identified so far, twice the value of the new prime is
#  guaranteed to be the largest unprocessed multiple.

#  Multiples are processed by removing the smallest unprocessed multiple from
#  the list of multiples.  Since the list is always sorted, the smallest
#  unprocessed multiple will always be the first element in the list.
#  Processing a multiple consists of finding the next multiple of every prime
#  which divides into that multiple.  If that multiple does not already have
#  a corresponding entry in the list of multiple, a new entry in the list of
#  multiples is created at the appropriate location in the list.  If, the
#  list of multiples already has an entry the next multiple of the prime being
#  processed, the prime being processed is added to the list primes which
#  evenly divide that multiple.

#  The time complexity of the Sieve of Eratosthenes can be minimized by
#  at the expense of high space complexity by maintaining a list of candidate
#  primes and marking multiples of known primes.  The space complexity of the
#  algorithm can be minimized at the expense of high time complexity by
#  dividing candidate primes by all primes smaller than it.

#  This program is economical in both time and space complexity.  At any given
#  time there will be one, and only one, multiple of each prime pending
#  processing.  Because of this, the list of multiples will be at most as long
#  as the list of primes, economizing space complexity.  The time complexity is
#  reduced by avoiding unproductive calculations for each multiple.  Inserting
#  multiples into the list of multiples is a major portion of the processing of
#  multiples.  Most multiples will be associated with the smallest few primes.
#  The position of these multiples will found relatively quickly because they
#  will be positioned in the first few positions of the list of multiples.


def solution(i):

    #  Initialize for first prime
    prime_state = []
    next_multiples = []

    last_prime = 2
    id_string = str(last_prime)
    prime ={'value': last_prime, 'next_multiple': last_prime + last_prime}
    prime_state.append(prime)

    next_multiples.append({'value': prime['next_multiple'], 'primes': [prime]})

    last_multiple = prime['value']

    #  Find primes until the id string is at least (i+5) characters long
    while len(id_string) < (i + 5):

        #  If the next number is not the smallest value in the list of multiples, it is prime
        if (last_multiple+1) < next_multiples[0]['value']:

            #  Create a new entry in the list of primes
            last_prime = last_multiple + 1
            id_string += str(last_prime)
            prime = {'value': last_prime, 'next_multiple': last_prime + last_prime}
            prime_state.append(prime)

            #  Add twice the value of the new prime to the list of multiples
            next_multiples.append({'value': prime['next_multiple'], 'primes': [prime]})

            #  The times the new prime is the last multiple seen
            last_multiple = last_prime
        else:

            #  Pop smallest entry off the list of multiples to begin processing it
            multiple = next_multiples.pop(0)

            #  Process all primes which divide the current multiple
            for prime in multiple['primes']:

                #  Find next multiple of the current prime being processed
                prime['next_multiple'] += prime['value']

                #  Search for next multiple of this prime in the current list of multiples
                idx = 0
                while prime['next_multiple'] > next_multiples[idx]['value']:
                    idx += 1

                    if idx == len(next_multiples):
                        break

                #  If the next multiple of current prime is already in list of multiples add prime to list of primes
                #  which evenly divide that multiple
                if idx < len(next_multiples):
                    if prime['next_multiple'] == next_multiples[idx]['value']:
                        next_multiples[idx]['primes'].append(prime)
                    else:
                        next_multiples.insert(idx, {'value': prime['next_multiple'], 'primes': [prime]})
                else:
                    next_multiples.append({'value': prime['next_multiple'], 'primes': [prime]})

            last_multiple = multiple['value']

    #  Extract the ID and return it
    return id_string[i:i+5]
