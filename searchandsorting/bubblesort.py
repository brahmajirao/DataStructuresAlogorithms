"""
Implementation of a Bubble Sort
The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.

Resources for Review
Check out the resources below for a review of Bubble sort!

Wikipedia: https://en.wikipedia.org/wiki/Bubble_sort
Visual Algo: https://visualgo.net/sorting.html
"""
def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k+1]:
                tmp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = tmp
    return arr

if __name__ == "__main__":
    print(bubble_sort([5,4,7,3,8]))