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
    
    ''' 
    # Greedy solution
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
            
            numEggs = dp_make_weight(egg_weights, target_weight - nextEgg, memo) + 1
            
            memo[(egg_weights, target_weight)] = numEggs
    return numEggs
    # not optimal when for example egg_weights = (1, 9, 90, 91) and target_weight = 99
    '''
    # dynamic programming, bottom up
    dp = [0 for i in range(target_weight + 1)]
    for i in range(1, target_weight + 1):
        dp[i] = 1 + min([dp[i-weight] for weight in egg_weights if weight <= i])
    
    return dp[target_weight]


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    print('---Test 1---')
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    
    print('---Test 2---')
    egg_weights = (1, 9, 90, 91)
    n = 99
    print("Egg weights = (1, 9, 90, 91)")
    print("n = 99")
    print("Expected ouput:29 (1*90 + 1*9 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    