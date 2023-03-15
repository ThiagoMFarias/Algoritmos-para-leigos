def search(searchList, key):
    mid = int(len(searchList)/2)
    print('searching midpoint at ', str(searchList[mid]))

    if mid == 0:
        print('Key not found!')
        return key
    elif key == searchList[mid]:
        print('Key found!')
        return searchList[mid]
    
    elif key > searchList[mid]:
        print('SearchList now contains ', searchList[mid:len(searchList)])
        search(searchList[mid:len(searchList)], key)

    else:
        print('SearchList now contains ', searchList[0:mid])
        search(searchList[0:mid], key)

aList = list(range(1,21))
search(aList,5)

# Explicação página 112 do livro!