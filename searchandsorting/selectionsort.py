#Max element sorts first
def selection_sort(arr):

    for fillspot in range(len(arr)-1, 0, -1):
        maxPosition = 0
        for minlocation in range(1, fillspot+1):
            if arr[minlocation] > arr[maxPosition]:
                maxPosition = minlocation
        tmp = arr[fillspot]
        arr[fillspot] = arr[maxPosition]
        arr[maxPosition] = tmp
    print(arr)



def selection_sort_minfirst(arr):
    for fillspot in range(0, len(arr) -1):
        minposition = fillspot
        for i in range(fillspot+1, len(arr)):
            if arr[i]<arr[minposition]:
                minposition = i
        tmp = arr[fillspot]
        arr[fillspot] = arr[minposition]
        arr[minposition] = tmp
    print(arr)

if __name__ == "__main__":
    selection_sort_minfirst([8,9,4,6,3, 89,91,5,7,11])