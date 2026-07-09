def formatName(firstName,lastName):
    """"Take a first and last name and format it to return the title case version of te complete name."""
    if firstName =="" or lastName=="":
        return "You did not provide valid inputs."
    firstName=firstName.title()
    lastName=lastName.title()
    return f"{firstName} {lastName}"

print(formatName("JaImE","mAtOlA"))
print(formatName("JaImE",""))

#Multiple return values
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(print(f"Resultado: {result}"))

#Store a function in a variable
myCompleteName=formatName
comple