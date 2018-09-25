def add_one(input_array):
    cary = 1
    result = [0]*len(input_array)
    iter_t = len(input_array)-1
    while iter_t >= 0:
        total = input_array[iter_t] + cary
        if total == 10:
            cary =1
        else:
            cary = 0
        result[iter_t] = total%10
        iter_t -= 1
    if cary == 1:
        result.insert(0, cary)
    print(result)

if __name__ == "__main__":
    add_one([1,2,3,4,5,6])
    add_one([1,2,3,9])
    add_one([9,9,9,9])