student={"name":"Salah", "age":34}
print(student["name"])
student["country"]="Egipt"
print(student)
student2=student.copy()
emptyDict={} # or dict()
student.clear() # Wipe all the items in a dictionary.
print(student)

for key in student2:
    print(key)


#Nested list in dictionary
travelLog={
    "Mozambique":["Matola","Boane","Namaacha","Mahubo"],
     "France":["Paris","Lille","Dijon"],
     "Germany":["Munich","Dortmund","Hamburg","Leverkusan"]
}

#Print Lille
print(travelLog["France"][1])

nestedList=["A","B","C",["D","E"],"G"]
nestedList[3].append("F")
print(nestedList)


travelLog2={
    "Mozambique":{"citiesVisited":["Matola","Boane","Namaacha","Mahubo"],
                  "totalVisits":10
                  }
    ,
     "France":{"citiesVisited":["Paris","Lille","Dijon"],
              "totalVisits":8
               },
    
     "Germany":{"citiesVisited":["Munich","Dortmund","Hamburg","Leverkusan"],
      "totalVisits":15
      }
}

print("Travel Log 2:")
print(travelLog2["Germany"]["citiesVisited"][2])
dict2={"a":1,"b":3,}
print(dict2)
