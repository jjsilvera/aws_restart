print("Count to 10!")
lista = ["Primer número impar: ", "Segundo número impar: ", "Tercer número impar: ", "Cuarto número impar: ", "Quinto número impar: "]
lista2 = []
for x in range(0,10):
    if x % 2 != 0:
        #print(x)
        lista2.append(x)
        print(lista2)
        print(f'"Primer número impar: {x}", "Segundo número impar: {x}", "Tercer número impar: {x}", "Cuarto número impar: {x}", "Quinto número impar: {x}"') 
        



"""num_list = [1, 2, 3, 4, 5]
print(f'Current Numbers List {num_list}')
num = int(input("Please enter a number to add to list:\n"))
index = int(input(f'Please enter the index between 0 and {len(num_list) - 1} to add the number:\n'))
num_list.insert(index, num)
print(f'Updated Numbers List {num_list}')"""

