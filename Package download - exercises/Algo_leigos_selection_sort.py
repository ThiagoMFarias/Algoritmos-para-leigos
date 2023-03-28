data = [9,5,7,4,2,8,1,10,6,3]

for scanIndex in range(0, len(data)):
    minIndex = scanIndex

    for compIndex in range(scanIndex + 1, len(data)):
        if data[compIndex] < data[minIndex]:
            minIndex = compIndex
            print(compIndex)

    if minIndex != scanIndex:
        data[scanIndex], data[minIndex] = \
            data[minIndex], data[scanIndex]
        print(data)

# Numa lista você troca o primeiro menor valor por quem estiver na primeira posição da lista