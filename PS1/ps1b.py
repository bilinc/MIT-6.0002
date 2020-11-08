###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Bilin Chen
# Collaborators: None
# Time: 2020-11-08
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
	# TODO: Your code here
    eggs = [0, 0, 0, 0]
    if memo == None:
        memo = {}

    if (egg_weights, target_weight) in memo:
        # numEggs = result
        numEggs = memo[(egg_weights, target_weight)]
	
    elif target_weight == 0  or egg_weights == ():
        numEggs = 0
    
    else:
        nextEgg = max(egg_weights)
        if nextEgg > target_weight:
            numEggs = dp_make_weight(egg_weights[:-1], target_weight, memo)
            
        else:
            # Add an egg to the taken list
            eggs[egg_weights.index(nextEgg)] += 1
            
            numEggs = dp_make_weight(egg_weights, target_weight - nextEgg, memo) + 1
            
            memo[(egg_weights, target_weight)] = numEggs
            
    return numEggs
            
        # take the maximum weight egg, if it excedes the current limit, take the next heaviest, and so on...
#        while target_weight != 0:
#            if egg_weights[3] < target_weight:
#                pass
#            elif egg_weights[2] < target_weight:
#                pass
#            elif egg_weights[1] < target_weight:
#                pass
#            elif egg_weights[0] < target_weight:
#                pass
        
    
    # dict, key = egg_weight, value = nr of eggs
#    numEggs = result
#    return result

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    
    
    
    