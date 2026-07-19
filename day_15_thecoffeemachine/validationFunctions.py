def inputValidation(text,listElements):
    """Returns a valid element typed by the user."""
    try:
        entry=input(text).lower()
        lowerList=list(map(str.lower,listElements)) #Transform the list elements in lower case
    except Exception as e:
        print (e)

    else:

        if entry in lowerList:
            return entry
        elif entry == "":
            print(f"Space is an invalid option, please select one of this options {listElements}")
        else:
            print(f"{entry} is an invalid option, please select one of this options {listElements}")
        inputValidation(text,listElements)

def validateInteger(text):
    """"Validate if a String typed is a integer."""
    try:
        number=int(text)
    except ValueError as vex:
        if text== "" or text ==" ":
            print("Error: Space is not a valid number.")
        else:
            print(f"Error: {text} is not a valid number.")

    except Exception as e:
        print(f"Error: {e}")
    
    else:
        if isinstance(number,int):
            return number


def inputInteger(text):
    """"Validate if an input typed is an integer and return a number."""
    while True:
        try:
            entry=input(text)
            number=validateInteger(entry)
    
        except Exception as e:
            print(f"Error: {e}")
        
        else:
            if isinstance(number,int):
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
