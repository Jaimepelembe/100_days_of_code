def inputValidation(text,tupleElements):
    while True:
        entry=input(text)
        if entry in tupleElements:
            return entry
        else:
            print(f"{entry} is an invalid option, please select one of this options {tupleElements}")


def validateInteger(text):
    number=int(input(text))
    if isinstance(number,int):
        return number


def validateFloat(text):
    number=float(input(text))
    if isinstance(number,float):
        return number

def validateIntervalOfIntegers(text,lowerLimit,upperLimit):
    """Validate if a number is in the valid interval of integers"""
    number=validateInteger(text)
    if number>=lowerLimit and number<=upperLimit:
        return number
    else:
        print(f"{number} nao esta no intervalo de {lowerLimit} a {upperLimit}. Por favor Tente novamente")
        validateIntervalOfIntegers(text,lowerLimit,upperLimit)


def validateString(text):
    string=input(text)
    if isinstance(string,str) and string!=None and string !="":
        return string
    else:
        if string == "":
            print(f"Espaco nao e uma String valida. Por favor tente de novo")

        else:
            print(f"{string} nao e uma String valida. Por favor tente de novo")

        validateString(text)
