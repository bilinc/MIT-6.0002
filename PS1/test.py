def dp_make_weight(egg_weights, target_weight, memo = {}):

    new_eggs = egg_weights
    
    if target_weight in memo:
        return memo[target_weight]
    elif len(new_eggs) == 1:     
        result = target_weight
    elif new_eggs[-1] > target_weight:      
        result = dp_make_weight(new_eggs[:-1], target_weight, memo)
    else:
        nextItem = new_eggs[-1]
        Withvalue = dp_make_weight(new_eggs, target_weight - nextItem, memo)
        Withvalue += 1
        
        WithoutValue = dp_make_weight(new_eggs[:-1], target_weight, memo)
        
        if Withvalue > WithoutValue:
            result = WithoutValue
        else:
            result = Withvalue
    memo[target_weight] = result
    return result
                
        
# bottom up approach        
def dp_make_weight2(egg_weights, target_weight, memo = {}):
    assert 1 in egg_weights
    assert all(x<y for x, y in zip(egg_weights, egg_weights[1:]))
    
    # creates a list of zeros
    dp = [0 for i in range(target_weight+1)]
    
    for i in range(1, target_weight+1):
        dp[i] = 1 + min([dp[i-weight] for weight in egg_weights if weight<=i])
    print(dp)
    return dp[target_weight]

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight2(egg_weights, n))
    print()
    

