data = [9,5,7,4,2,8,1,10,6,3]

for scanIndex in range(1, len(data)):
    temp = data[scanIndex] # Aqui estou guardando meu elemento atual numa variável. 

    minIndex = scanIndex

    while minIndex > 0 and temp < data[minIndex - 1]: # Enquanto a posição(miniIndex) for maior que 0 e o elemento atual for menor que a posição anterior 
        data[minIndex] = data[minIndex - 1] # Vou fazer a troca. 
        minIndex -=1

    data[minIndex] = temp
    print(data)

# Outra maneira de fazer:
n = len(data)
for i in range(1, n):
    chave = data[i]
    j = i -1 # Parcela da lista que já está ordenada
    while j >= 0 and data[j] > chave:
        data[j+1] = data[j]
        j = j-1 
        print(data)
    data[j+1] = chave
    print(data) 

'''Insertion sort funciona usando um único item como ponto de partida e adicionado itens à sua esquerda ou direita baseada em se esses itens são maiors ou menores que o selecionado. Possui O(n) no melhor caso e O(n**2) no pior caso.'''
