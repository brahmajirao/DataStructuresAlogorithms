"""
Given an integer, create a function which returns the sum of all the individual
digits in that integer. For example: if n = 4321, return 4+3+2+1

"""

def sum_digits(n):
    if int(n/10) <= 1:
        return n
    else:
        return (n%10) + sum_digits(int(n/10))


if __name__ == "__main__":
    print(sum_digits(4567892))