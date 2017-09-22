def bsearch(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if target==data[mid]:
            return mid
        elif target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid + 1
        else:
            return mid
    return None
 
if __name__ == '__main__':
    array = [1,2,3,4,5]
    result = bsearch(array,4)
    print(result)
