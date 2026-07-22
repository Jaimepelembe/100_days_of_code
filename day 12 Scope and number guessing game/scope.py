apples=1
def increaseApples():
    apples=2
    print(f"Apples inside the function: {apples}")


increaseApples()

print(f"Apples outside the function: {apples}")

#Local Scope
# Variaveis declaradas dentro de funcoes tem escopo local. Elas sao vistas apenas por outro codigo que esteja dentro do escopo da funcao

def drinkPotion():
    potionStrenght=2
    print(potionStrenght)

drinkPotion()
#print(posionStrenght) This will cause a NameError because the postionStrenght variable is not declared as a global scope.


#Global scope

pontos = 0
print("Variaveis globais")
def ganhar_ponto():
    #pontos = pontos + 1   # ❌ UnboundLocalError, a variavel ainda nao foi definida localmente
    print(pontos)

ganhar_ponto()

#Para modificar uma variavel global dentro de uma funcao usa-se a palavra chave "global" antes do nome da variavel
def ganhar_ponto2():
    global pontos 
    pontos = pontos + 1   # ❌ UnboundLocalError, a variavel ainda nao foi definida localmente
    print(pontos)

ganhar_ponto2()
ganhar_ponto2()


# Block scope
#   Python does not have block scope.
print("Block Scope:")
listEnemies=["Skeleton","Zombie","Alien"]
gameLevel=3

def createEnemy():
    newEnemy=""
    if gameLevel <5:
        newEnemy=listEnemies[0]
    print(newEnemy)

createEnemy()