#iterator way
def fib_iter(n):
    a, b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a

def fib_recursive(n):
    #base condition
    if n==0 or n==1:
        return n
    else:
        return fib_iter(n-1) + fib_iter(n-2)

n =10
cache = [None]*(n+1)
def fib_memoization(n):
    #base condition
    if n==0 or n==1:
        return n
    #check cache
    if cache[n] != None:
        return cache[n]
    cache[n] = fib_memoization(n-1) + fib_memoization(n-2)
    return cache[n]

if __name__ == "__main__":
    print(fib_iter(10))
    print(fib_recursive(10))
    print(fib_memoization(10))
