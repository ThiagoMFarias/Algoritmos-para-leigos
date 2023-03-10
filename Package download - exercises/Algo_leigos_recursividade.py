# Um dos exeplos mais comuns de recursão para todas as linguagens de programação é o cálculo de fatorial:

def factorial (n):
    print('factorial called with n = ', str(n))
    if n == 1 or n == 0:
        print ('Ending codition met.')
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Outra forma de chamar o fatorial com menos linhas

def fatorial (a):
    print('factorial called with n = ', str(a))
    if a>1:
        return a * fatorial(a-1)
    print('Ending condition met.')
    return 1
print(fatorial(10))