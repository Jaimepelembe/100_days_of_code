fruits=["Apple","Kiwi","Orange","Avacato"]
print(fruits)
print(fruits[-3])

statesOfAmerica=["Delaware","Pennsylvania","New Jersey","Georgia","Connecticut"]
print(statesOfAmerica[4])
print(statesOfAmerica[-2])

#Add one element
statesOfAmerica.append("Massachusetts")
statesOfAmerica.append("Maryland")
statesOfAmerica.append("South Carolina")

print(statesOfAmerica)

#Add an iterable with many one or more elements.
listThreeStates=["New Hampshire","Virginia","New York"]
statesOfAmerica.extend(listThreeStates)
print(statesOfAmerica)