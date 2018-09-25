"""
without recursion
"""
def binary_search(arr, item):
    found = False
    first = 0
    last = len(arr) -1
    mid = (first+last)//2

    while first <= last and not found:
        if arr[mid] == item:
            found = True
        else:
            if item < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def binary_search_recursive(arr, item):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if arr[mid] == item:
            return True
        else:
            if item < arr[mid]:
                return binary_search_recursive(arr[:mid-1], item)
            else:
                return binary_search_recursive(arr[mid+1:], item)