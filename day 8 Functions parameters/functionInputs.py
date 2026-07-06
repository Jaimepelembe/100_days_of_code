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


def apresentar(nome, idade):
    print(f"{nome} tem {idade} anos")

apresentar("Ana Maria",22)
apresentar(idade=25,nome="Jeremias")

def life_in_weeks(age):
    weeksPerYear=int(365/7)
    yearsLeft=90-age
    weeksLeftUntil90=yearsLeft*weeksPerYear
    
    return f"You have {weeksLeftUntil90} weeks left."

print(life_in_weeks(30))