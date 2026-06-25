def inputValidation(text,tupleElements):
    while True:
        entry=input(text)
        if entry in tupleElements:
            return entry
        else:
            print(f"{entry} is an invalid option, please select one of this options {tupleElements}")