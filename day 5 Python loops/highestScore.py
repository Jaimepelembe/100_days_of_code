studentScores=[150,142,185,120,171,184,149,24,59,68,199,78,65,89,86,55,91,64,89]
totalScore=sum(studentScores)
print(totalScore)

#Creating the sum using for loop
total=0
for score in studentScores:
    total+=score

print(total)


#Finding the max value

##Using Max function
print(f"The maximum score is {max(studentScores)}\n")

## Using for loop
actualMax=studentScores[0]
for score in studentScores:
    if actualMax < score:
        actualMax=score

print(f"The maximum score is {actualMax}")