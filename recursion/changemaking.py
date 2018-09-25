"""
Coin Change Problem
Note: This problem has multiple solutions and is a classic problem in showing issues with
basic recursion. There are better solutions involving memoization and simple iterative solutions.
If you are having trouble with this problem (or it seems to be taking a long time to run
in some cases) check out the Solution Notebook and fully read the conclusion link for a
detailed description of the various ways to solve this problem!

This problem is common enough that is actually has its own Wikipedia Entry!
Let's check the problem statement again:

This is a classic recursion problem: Given a target amount n and a list (array) of
distinct coin values, what's the fewest coins needed to make the change amount.

For example:

If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

1+1+1+1+1+1+1+1+1+1

5 + 1+1+1+1+1

5+5

10

With 1 coin being the minimum amount.

Solution
This is a classic problem to show the value of dynamic programming.
We'll show a basic recursive example and show why it's actually not the best
way to solve this problem.

Make sure to read the comments in the code below to fully understand the basic logic!
"""
def rec_coin(target, coins):

    #Default value set to target
    min_coins = target

    #check to see target in coins
    if target in coins:
        return 1
    else:
        #For every coin value that is less than or equal to my target value
        for i in [c for c in coins if c <= target]:
            #Add coin count + recursive call
            num_coins = 1 + rec_coin(target -i, coins)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


"""
Dynamic Programming Solution
This is the key to reducing the work time for the function. 
The better solution is to remember past results, that way before computing a new minimum 
we can check to see if we already know a result.

Let's implement this:
"""
def rec_coin_dynam(target, coins, known_results):
    '''
        INPUT: This funciton takes in a target amount and a list of possible coins to use.
        It also takes a third parameter, known_results, indicating previously calculated results.
        The known_results parameter shoud be started with [0] * (target+1)

        OUTPUT: Minimum number of coins needed to make the target.
        '''
    min_coins = target

    #Base Case
    if target in coins:
        known_results[target] = 1
        return 1
    #Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        for i in [c for c in coins if c<= target]:
            num_coins = 1+ rec_coin_dynam(target - i, coins, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[target] = min_coins
    print(known_results)
    return min_coins



if __name__ == "__main__":
    target = 85
    coins =[1,5, 10, 20, 50]
    known_results = [0]*(target+1)
    print(known_results)
    print(rec_coin_dynam(target,coins,known_results))