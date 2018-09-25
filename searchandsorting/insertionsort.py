def insertion_sort(arr):
    for i in range(1, len(arr)):
        currentvalue = arr[i]
        position = i
        while position > 0 and arr[position -1] > currentvalue:
            arr[position] = arr[position-1]
            position = position-1
        arr[position] = currentvalue
    print(arr)

if __name__ == "__main__":
    insertion_sort([3,5,4,6,8,1,2,12,41,25])