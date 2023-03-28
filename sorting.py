def selection_sort(lista):
    for j in range(len(lista)-1):
        min_index = j # O valor mínimo seria quem está na posição 0 da lista;
        for i in range(j, len(lista)): # Eu vou andar pelos índices da lista de 0 até o tamanho da lista -1;
            if lista[i] < lista[min_index]: # Verifico se o valor que eu estou olhando no momento é menor do que algum valor que eu conheço por mínimo.
                min_index = i
        j = 0
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
        
