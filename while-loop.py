print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and yuo will try to guess it.")
print("=============================================================================")

import random
number = random.randint(1,10)
suma = 0
isGuessRight = False # Se inicializa en False para que el bucle sea continuo 
# El bucle while repetirá el código dentro del bucle hasta que se adivine el número correcto,
# lo que está representado por la condición isGuessRight != True
while isGuessRight != True: 
    guess = int(input("Guess a number between 1 and 10: "))
    suma += guess
    if int(guess) == number:
        print("You guessed {}. That is correct! You win, the number's sum is: {}".format(guess, suma))
        isGuessRight = True # se cambia a True para finalizar el ciclo
    else:
        print("You guessed {}. Sorry that isn't it. Try again.".format(guess))