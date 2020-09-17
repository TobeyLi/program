def quickSort(array, low, high):
    """
    recursion version
    :param array:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        keyIndex = partion(array, low, high)
        quickSort(array, low, keyIndex - 1)
        quickSort(array, keyIndex + 1, high)


def quickSortNonRecursion(array, low, high):
    """
    non recursion version
    :param array:
    :param low:
    :param high:
    :return:
    """
    stack = []
    if low < high:
        mid = partion(array, low, high)
        if low < mid - 1:
            stack.append(low)
            stack.append(mid - 1)
        if mid + 1 < high:
            stack.append(mid + 1)
            stack.append(high)
        while len(stack) != 0:
            q = stack[-1]
            stack.pop(-1)
            p = stack[-1]
            stack.pop(-1)
            mid = partion(array, p, q)
            if p < mid - 1:
                stack.append(p)
                stack.append(mid - 1)
            if mid + 1 < q:
                stack.append(mid + 1)
                stack.append(q)


def partion(array, low, high):
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
    nums = [4, 2, 5, 7, 3, 4]
    quickSortNonRecursion(nums, 0, len(nums) - 1)
    print(nums)
