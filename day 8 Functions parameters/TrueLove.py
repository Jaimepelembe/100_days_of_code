def calculate_love_score(name1,name2):
    totalTrue=0
    totalLove=0
    listWords=["true","love"]
    listNames=[name1,name2] 
    listTrue=list((0,0,0,0))
    listLove=list((0,0,0,0))
 
  
    #name1=name1.lower()

    for i,word in enumerate(listWords): #Pega a primeira palavra
        #name=listNames[i].lower()
        for name in listNames: #Pega o primeiro nome
            name=name.lower()
            for  j,wordLetter in enumerate(word):
                if wordLetter in name: 
                    
                    for nameLetter in name:
                      
                        if wordLetter == nameLetter:   
                            if i==0:    
                                listTrue[j]+=1
                            else:
                                listLove[j]+=1
       
       
   
    for i,word in enumerate(listWords):
        for j,wordLetter in enumerate(word):
            if i ==0:
                print(f"{wordLetter} occurs {listTrue[j]} times")
                totalTrue+=listTrue[j]
            else:
                print(f"{wordLetter} occurs {listLove[j]} times")
                totalLove+=listLove[j]        
    
    return f"{totalTrue}{totalLove}"
"""
    print("------------------")
    print(f"Lista True: {listTrue}")
    print(f"Lista Love: {listLove}")
    print("------------------")
    print(totalTrue)
    print(totalLove)
"""
    
#calculate_love_score("TRUEvava","TubaruufoVVv")
#print()
print(calculate_love_score("Angela Yu","Jack Bauer"))

  # Para "True" name1= "True" , name2="Tubaruufo" 2T, 2R,4U, 1E 
    # Para "Love" name1= "True" , name2="Tubaruufo" 0L, 1 O,0V, 1E 