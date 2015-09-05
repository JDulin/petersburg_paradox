"""
John Dulin
September 4, 2015
St. Petersburg Paradox 

A simulation of the coin game used to postulate 
the St. Petersburg Paradox - A game of chance 
where the player earns 2^k dollars where 
k is the first flip in a series which lands 
tails.

In theory, this has an infinite expectation value.
"""

import random

def test(cost, times):
        """ 
        Play the game a certain number of times, at a constant cost per game. 
        Return the money made (positive) or lost (negative).
        """
        ### TODO: To what extent can we solve for the # of occurances of each k?
        winnings = []
        for i in xrange(times):
                winnings.append(play(1))

        return sum(winnings) - (times*cost)

def play(i):
        """ Play the game.  Return the money won. """
        if flip():
                return play(i+1)
        else:
                return 2**i

def flip():
        """ Flip the coin. Assume Heads = True, Tails = False  """
        return bool(random.getrandbits(1))

def experiment():
        """ 
        Run several tests to determine expectation values, 
        Optimal cost to iteration ratio, etc.
        """


if __name__ == '__main__':
        print test(10, 100)
