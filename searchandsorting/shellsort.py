def shell_sort(arr):
    sublistcount = len(arr)//2
    while sublistcount > 0:
        print("Sublistcount:", sublistcount)
        for start in range(sublistcount):
            gap_insertion_sort(arr, start, sublistcount)

        sublistcount = sublistcount//2

def gap_insertion_sort(arr, start, gap):
    print("start plus gap:", start+gap)
    print([range(start + gap, len(arr), gap)])
    for i in range(start + gap, len(arr), gap):
        currentvalue = arr[i]
        position = i

        while position >= gap and arr[position-gap] > currentvalue:
            arr[position] = arr[position -  gap]
            position = position-gap

        arr[position] = currentvalue

if __name__ =="__main__":
    arr = [45, 67, 23, 45, 21, 24, 7, 2, 6, 4, 90]
    shell_sort(arr)
    print(arr)