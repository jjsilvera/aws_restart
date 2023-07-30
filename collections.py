##### Listas #####
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print((type(myFruitList)))
###########################################

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
###########################################

myFruitList[2] = "orange"
print(myFruitList)

#### Tuplas ####
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

############# Diccionario #################
myFavoriteFruitDictionary = {
    "Akua": "apple",
    'Saanvi': 'banana',
    'Paulo': 'pineapple',
    "Danny": "grape",
    "Maria": "orange",
    "Scarlet": "watermelon"
    }
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

############################################
print("La fruta favorita de Paulo es: ", myFavoriteFruitDictionary["Paulo"] + "\n" + "La primera posición de la lista es: ", myFruitList[0])
print("Esta es una llave del diccionario: ",[k for k in  myFavoriteFruitDictionary.keys()][5])
