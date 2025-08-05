### FUNÇÕES ###

"""
# len() retorna o número de itens em uma sequência

# append() adiciona um item ao final de uma lista

# insert() e pop() adicionam e removem itens da lista em posições específicas

"""

#retona erro, não foi concatenado
#name = "Anna"
#surname = "Anderson"
#print(name surname)

#x = "robot".find("o")
#print(x)

#print("robot".find("t"))

#print("robot".find("A"))

#word = 'vehicle'
#print(word.find('r'))

#word = 'vehicle'
#print(word.find())

# filmes = ['Marvel','Batman']
# filmes.append('Thor')
# print(filmes)
# print(len(filmes))
#
# topic = ["Maths","English","Physics"]
# topic.pop(2)
# print(topic)
# print(len(topic))

# Testando remover elemento de lista como string e colcoando lower nele
films = ["Os Indomaveis", "Senhor dos aneis", "HARRY POTTER"]

# removed_item = films.pop(2)  # Remove terceiro elemento e retorna como string
# print("lista de filmes\n" + removed_item.lower())  # Aplica .lower() na string removida

# colocando em camelCase, snake_case e lower case
def to_camel_case(s):
    return ''.join(word.capitalize() for word in s.split())

def to_snake_case(s):
    return '_'.join(word.lower() for word in s.split())

def to_lower_case(s):
    return s.lower()

# Testando as funções de formatação de string
print(to_camel_case(films[0]))
print(to_snake_case(films[1]))
print(to_lower_case(films[2]))

