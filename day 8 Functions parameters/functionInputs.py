def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")

#greet()
print()

def greetWithName(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")


#greetWithName("Angela")
#greetWithName("Maria")


def apresentar(nome,idade,cidade):
    print(f"{nome} tem {idade} anos e mora em {cidade}")

#apresentar("Ana Maria",22,"Matola")
#apresentar(idade=25,nome="Jeremias",cidade="Maputo")

def life_in_weeks(age):
    weeksPerYear=int(365/7)
    yearsLeft=90-age
    weeksLeftUntil90=yearsLeft*weeksPerYear
    
    return f"You have {weeksLeftUntil90} weeks left."

#print(life_in_weeks(30))

#Functions with more than 1 input

#1. Positional argument
#Argumentos posicionais
    #São passados na mesma ordem em que os parâmetros foram definidos na função. A posição é o que determina qual valor vai para qual parâmetro.
def greetWithLocation(name,location):
    print(f"Hello {name}, you are in {location}")

greetWithLocation("Carla","Angoche") 

#2. Argumentos nomeados (keyword arguments)
    # Você pode ignorar a posição e especificar diretamente qual valor vai para qual parâmetro, usando nome_do_parametro=valor: 
greetWithLocation(location="Balama",name="Angoche")


#3. Misturando os dois
    # Os posicionais devem vir primeiro:

apresentar("Zebito",idade=45,cidade="Gaza")
apresentar("Zebito",65,cidade="Gaza")

# 4. Parâmetros com valores padrão (default)
    # Devem vir depois dos que não têm:
def apresentar2(nome, idade=18, cidade="Maputo"):
    print(f"{nome} tem {idade} anos e mora em {cidade}")

apresentar2("Tekkan") # Usa valores padrão de idade e cidade.
apresentar2("Fabrizio Romano",idade=25)