"""
Question
Find the squareroot of a given number rounded down to the nearest integer,
without using the sqrt function. For example, squareroot of a number between [9, 15]
should return 3, and [16, 24] should be 4.

Solution
The squareroot of a (non-negative) number N always lies between 0 and N/2.
The straightforward way to solve this problem would be to check every number k between 0 and N/2,
until the square of k becomes greater than or rqual to N. If k^2 becomes equal to N,
then we return k. Otherwise, we return k-1 because we're rounding down. Here's the code:
"""
def solution(num):
    if num<0:
        raise ValueError
    if num == 1:
        return 1
    for k in range(1+(num//2)):
        if k**2 == num:
            return k
        elif k**2 > num:
            return k-1
    return k

def better_solution(num):
    if num < 0:
        raise ValueError
    if num == 1:
        return 1
    low = 0
    high = 1+ (num//2)

    while low + 1 < high:
        mid = low + (high-low)//2
        square = mid ** 2
        if square == num:
            return mid
        elif square<num:
            low = mid
        else:
            high = mid
    return low

if __name__ == "__main__":
    print(solution(14))
    print(better_solution(14))