myString= "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
###############################################################

firstString= "water"
secondString= "fall"
thirdString= firstString + secondString
print(thirdString)
###############################################################

name = input("What is your name? ")
print(name)
color =  input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))
###############################################################

num1 = float(input("Ingresa un número entero: "))
num2 = float(input("Ingresa otro número entero: "))
num3 = int(input("Ingresa una opción: "))
print("Pero ojo no se puede dividir por 0 !")
res = 0
if num3 == 1:
    res= num1+num2
elif num3 == 2:
    res= num1-num2
elif num3 == 3:
    res= num1*num2
try:
    if num3 == 4:
        res = num1/num2
except ZeroDivisionError:
    print("Error no puede dividir por cero!")
else:
    print("El resultado de los dos números es: {}".format(res))