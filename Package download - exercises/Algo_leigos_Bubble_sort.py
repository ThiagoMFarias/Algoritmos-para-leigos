vet = [21,9,1,45,11,90,132,87,3]

for a in range(0, len(vet)):
    print(vet[a])

for i in range(0, len(vet)):
    for x in range(0, len(vet)-1):  # antes estava assim: range(0,4)
        if vet[x] > vet[x+1]:
            aux = vet[x]
            vet[x] = vet[x+1]
            vet[x+1] = aux
            print(vet)

print('Vetor Ordenado')
for a in range(0, len(vet)):
    print(vet[a])

"""Vamos para as explicações:

1- se eu quiser que o código não imprima os vetores antes de estarem ordenados, basta eu retirar a linha 12;
2- na linha 7, se eu colocar range(0, len(vet)) ele irá dar erro em virtude de não existir o vetor 5, logo tive que restringir até o 4º vetor;
3- aqui eu optei por selecionar o maior item e colocá-lo na fim da lista, porém tem a possibilidade de escolher o menor item e colocá-lo no início da lista, bastando trocar o sinal de > por < na linha 8;"""

