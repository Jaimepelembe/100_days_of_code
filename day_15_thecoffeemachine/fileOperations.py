def readFile(fileName):
    """ Read a whole file"""

    try:
        file=open(fileName,"r")
        content=file.read()

    except FileNotFoundError:
        print("Error: The file was not founded.")
        #Create the file
        with open(fileName, "w") as fileText:
            fileText.write("0")
            return "0"
    except PermissionError:
        print("Error: Permission denied to read this file.")
    except IsADirectoryError:
        print("Error: The specified path is a folder, not a file.")
            
    except Exception as ex:
        print(f"Error: {ex}")
    else:
        if content=="":
            content="0"
        return content



def writeFile(fileName,value):
    """Write in a file"""

    try:
        file=open(fileName,"w")
        file.write(value)

    except FileNotFoundError:
        print("Error: The file was not founded.")
        #Create the file
        with open(fileName, "w") as fileText:
            fileText.write("")
    except PermissionError:
        print("Error: Permission denied to read this file.")
    except IsADirectoryError:
        print("Error: The specified path is a folder, not a file.")
            
    except Exception as ex:
        print(ex)
    else:
        print("File saved sucessfuly.")

    finally:
        if 'file' in locals() or not file.closed(): # locals() Verify the locals variables
            file.close()


def writeObjectInJson(fileName,object):
    import json
    try:
        with open(fileName,"w", encoding="utf-8") as file:
            json.dump(object,fileName,ident=4, ensure_ascii=False)
    
    except TypeError as e:
        print(f"Error: There are data that can't be converted to JSON.\n{e}") 
    
    except PermissionError:
        print("Error: Permission denied to write this file.")
    
    except OSError as e:
        print(f"Error in the file system: {e}")
    else:
        print("File saved sucessfuly.")



def readJsonFile(fileName):
    import json

    try:
        with open(fileName,"r", encoding="utf-8") as file:
            data=json.load(file)
    
    except FileNotFoundError:
        print("Error: The file was not founded.")
        #Create the file
        with open(fileName,"w", encoding="utf-8") as file:
            json.dump("[0]",fileName,ident=4, ensure_ascii=False) # Create a file with a empty space.
    
    except PermissionError:
        print("Error: Permission denied to write this file.")
    
    except OSError as e:
        print(f"Error in the file system: {e}")
    
    else:
        return data
