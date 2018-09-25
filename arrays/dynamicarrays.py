import sys

n = 1000
data = []
for i in range(n):

    #Number of elements
    a = len(data)
    #Actual Size in Bytes
    b = sys.getsizeof(data)

    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(i)