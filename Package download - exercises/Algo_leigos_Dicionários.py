colors = {'Sam': 'Blue', 'Amy': 'Red', 'Sarah': 'Yellow'}
print(colors['Sarah'])
print(colors.keys())

for Item in colors:
    print('{0} likes the color {1}'.format (Item, colors[Item]))

colors['Sarah'] = 'Purple'
colors.update({'Harry': 'Orange'})  # não usei a função 'append' pois é usada apenas em listas e aqui temos um dict. Logo a função update substitui ou inclui novas entradas ao dict.
del colors['Sam']

print(colors)

# Como vemos, um dict sempre tem um par de chave-valor separados um do outro por dois pontos(:).