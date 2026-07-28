""""
As Higher-Order Functions (HOFs) são funções que trabalham com outras funções. Em programação, uma função é considerada de ordem superior quando ela faz pelo menos uma destas duas coisas:

Recebe outra função como argumento.
Retorna outra função como resultado.
"""


# 1.Recebe outra função como argumento. 
def soma(a,b):
    return a+b

def multiplicacao(a,b):
    return a*b

def calcular(operacao,a,b): 

    return operacao(a,b)

print(calcular(soma,2,5))
print(calcular(multiplicacao,2,5))


# 2.Retorna outra função como resultado.
print("------------------")

def criarMultiplicador(n):
    def multiplicar(x):
        return x*n
    
    return multiplicar

dobro=criarMultiplicador(2)
#print(criarMultiplicador(5)(9))
triplo=criarMultiplicador(3)

print(dobro(10))
print(triplo(10))


print("----------------")

def criarPotencias(expoente):
    def potencia(base):
        return base**expoente

    return potencia

quadrado=criarPotencias(2)
cubo=criarPotencias(3)
print(quadrado(5))
print(cubo(5))