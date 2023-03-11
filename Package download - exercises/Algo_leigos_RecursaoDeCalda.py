# https://blog.moertel.com/posts/2013-05-14-recursive-to-iterative-2.html

# função binomial recursiva (seria essa parte aqui: 'binomial(n - 1, k - 1)')
def binomial(n, k):
    if k == 0:
        return 1
    return n * binomial(n - 1, k - 1) // k 

# Outra versão recursiva:
def binomial(n, k):
    """Compute binomial coefficient C(n, k) = n! / (k! * (n-k)!)."""
    if k == 0:
        return 1
    return n * binomial(n - 1, k - 1) // k

# Chamada iterativa, onde lmul= leftMultiplication and rdiv=rightDivision
def binomial_iter(n, k):
    """Compute binomial coefficient C(n, k) = n! / (k! * (n-k)!)."""
    lmul = rdiv = 1
    while k > 0:
        (n, k, lmul, rdiv) = (n - 1, k - 1, lmul * n, k * rdiv)
    return lmul // rdiv

print (binomial(39, 9))
print (binomial_iter(39, 9))

# Função fatorial que usa iteração no lugar da recursão:
def fatorial(n):
    print('Factorial called with n = ', str(n))
    result = 1
    while n>1:
        result = result * n
        n = n-1
        print('Current value of n is ', str(n))
    print('Ending condition met!')
    return result

print(fatorial(5))