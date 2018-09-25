def merge_sort(arr):
    length = len(arr)
    if length > 1:
        mid = length//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        while i<len(lefthalf):
            arr[k] = lefthalf[i]
            i+=1
            k += 1

        while j<len(righthalf):
            arr[k] = righthalf[j]
            j+=1
            k+=1
        #print("Merging", arr)

if __name__ =="__main__":
    arr = [45, 67, 23, 45, 21, 24, 7, 2, 6, 4, 90]
    merge_sort(arr)
    print(arr)