import random
from sorting import selection_sort

any_numbers = random.sample(range(1, 100), 42)

already_sorted = [1, 2, 3, 4, 5, 9, 20, 22, 23, 28, 32, 34, 76, 39, 40, 42, 87, 99, 112]

inversed = [200, 198, 150, 132, 115, 100, 80, 53, 31, 29, 17, 5, 1]

repeated = [7, 7, 7, 7, 8, 8, 5, 5, 10, 10, 13, 13, 0, 1, 7, 5, 8]

if __name__ == '__main__':
    lista = repeated
    print(lista)
    selection_sort(lista)
    print('\n Ordenado' )
    print(lista)