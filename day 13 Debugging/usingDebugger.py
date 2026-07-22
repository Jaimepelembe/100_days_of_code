import random
import maths


def mutate(aList):
    bList=[]
    newItem=0
    for item in aList:
        newItem=item*2
        newItem+=random.randint(1,3)
        newItem= maths.add(newItem,item)
        bList.append(newItem)
    print(bList)

mutate([1,2,3,5,8,13])