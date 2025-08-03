### LISTAS ###

last_calls = ["Mom", "Dave", "Lawyer"]
# print(last_calls[0])
# print(last_calls[1])

#define os valores dentro da lista
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# cria um for, declarando cada elemento da lista representado por "n"
# insere condicional que apenas irá trazer os elementos "n",
# que são divisiveis por 2 ou seja numeros pares
test_list = [n for n in numbers if n % 2 == 0]

# imprime na tela os valores dentro de test_list
print (test_list)
