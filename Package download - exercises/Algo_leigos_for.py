def DisplayMulti(*Varargs):
    for Arg in Varargs:
        if Arg.upper() == 'CONT':
            continue #Perceba que com o continue o print abaixo dele deixa de ser necessário e o loop é interrompido passando para o próximo índice. 
            print('Continue Argument: ' + Arg)
        elif Arg.upper() == 'BREAK':
            break #O mesmo comentário do continue!
            print('Break Argument: ' + Arg)
        print('Good argument: ' + Arg)

DisplayMulti('Hello', 'Goodbye', 'First')
DisplayMulti('Hello', 'Cont', 'Goodbye', 'Break', 'Last')

# Aqui, o *VarArgs permite que você passe qualquer número de argumentos posicionais, que serão empacotados como uma tupla: