arr = [9,5,7,4,2,8,1,10,6,3]
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr
merge_sort(arr)



# Chamada inicial da função merge_sort com arr = [9,5,7,4,2,8,1,10,6,3]
# O tamanho de arr é maior que 1, então a função executa a primeira recursão
# Criando left_half com [9,5,7,4,2] e right_half com [8,1,10,6,3]
# left_half precisa ser ordenado, então a função é chamada recursivamente com left_half
# arr = [9,5,7,4,2]
# mid = 2
# left_half = [9,5]
# right_half = [7,4,2]
# merge_sort(left_half)
# left_half precisa ser ordenado, então a função é chamada recursivamente com left_half
# arr = [9,5]
# mid = 1
# left_half = [9]
# right_half = [5]
# merge_sort(left_half)
# left_half é um array de tamanho 1, então não é necessária mais nenhuma chamada recursiva
# retorna [9]
# merge_sort(right_half)
# right_half é um array de tamanho 1, então não é necessária mais nenhuma chamada recursiva
# retorna [5]
# Na função merge_sort, left_half é [9] e right_half é [5]
# left_half e right_half são ordenados no while loop abaixo:
# arr = [9,5,7,4,2]
# i = 0, j = 0, k = 0
# arr[k] = 5
# j += 1
# k += 1
# arr[k] = 9
# i += 1
# k += 1
# Agora, i == len(left_half), então o while loop termina e o restante do array left_half é adicionado a arr:
# arr = [5,9,7,4,2]
# i = 1, k = 2
# arr[k] = 7
# i += 1
# k += 1
# ...
# arr = [2,4,5,7,9]
# O array left_half foi ordenado, então a segunda chamada recursiva para merge_sort com left_half terminou
# agora, right_half precisa ser ordenado, então a função é chamada recursivamente com right_half
# arr = [8,1,10,6,3]
# mid = 2
# left_half = [8,1]
# right_half = [10,6,3]
# merge_sort(left_half)
# left_half precisa ser ordenado, então a função é chamada recursivamente com left_half
# arr = [8,1]
# mid = 1
# left_half = [8]
# right_half = [1]
# merge_sort(left_half)
# left_half é um array de tamanho 1, então não é necessária mais nenhuma chamada recursiva
# retorna [8]
# merge_sort(right_half)
# right_half é um array de tamanho 1, então não é necessária mais nenhuma chamada recursiva
# retorna [1]
# Na função merge_sort, left_half é [8] e right_half é [1]
# left_half e right_half são ordenados no while loop abaixo:
# arr = [8
