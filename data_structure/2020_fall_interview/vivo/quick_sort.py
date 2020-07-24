

def quick_sort(array,low,high):
    if low < high:
        key_index = partion(array,low,high)
        quick_sort(array,low,key_index-1)
        quick_sort(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        array[high] = array[low]

    array[low] = key
    return low

if __name__ == '__main__':
    nums=[4,2,5,7,3,4]
    quick_sort(nums,0,len(nums)-1)
    print(nums)