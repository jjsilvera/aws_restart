myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
milista = [1,2,3,4,5,6]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item))) # item se se pasa desde el for es cada elemento de la lista
    for k in milista:
        
        print("Elementos de mis lista: {}".format(k))
    