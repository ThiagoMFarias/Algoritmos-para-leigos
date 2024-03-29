data = [9,5,7,4,2,8,1,10,6,3]

def mergeSort(list):
    # Determine whether the list is broken into in individual pieces.
    if len(list) < 2:
        return list
    
    # Find the middle of the list.
    middle = len(list)//2

    # Break the list into tow pieces.
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])

    # Merge the tow sorted pieces into a large piece.
    print('Left side: ', left)
    print('Right side: ', right)
    merged = merge(left, right)
    print('Merged ', merged)
    return merged

def merge(left, right):
    # When the last side or the right side is empty, ir means that this is an individual item and is an individual item and is already sorted.
    if not len(left):
        return left
    if not len(right):
        return right
    
    # Define variables used to merge the tow pieces.
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    # keep working until all of the items are merged.
    while (len(result) < totalLen):

        # Perform the required comparisons and merge the pieces according to value.
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
        
        # When the left side or the right side is longer, add the remaining elements to the result.
        if leftIndex == len(left) or rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])
            break
    return result

mergeSort(data)