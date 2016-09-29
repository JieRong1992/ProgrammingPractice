def binarysearch(list, target):
    if list is None or len(list) == 0:
        return False
    start = 0
    end = len(list)-1
    mid = start+(end-start)//2
    while start+1 < end:
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            end = mid
        elif list[mid] < target:
            start = mid
        mid = start + (end - start) // 2
    if list[start] == target:
        return start
    elif list[end] == target:
        return end
    else:
        return False
