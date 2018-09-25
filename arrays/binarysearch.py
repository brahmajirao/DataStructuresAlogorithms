def binary_search(input_array, value):
    """Your code goes here."""
    min = 0
    max = len(input_array) - 1
    while True:
        if min > max:
            return -1
        mid = int((min+max)//2)
        print("Mid number:{}, mid value:{}".format(mid, input_array[mid]))
        if input_array[mid]< value:
            min = mid + 1
        elif input_array[mid]>value:
            max = mid-1
        else:
            return mid


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))