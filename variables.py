_cars = [0,10,20,30]
# cars = 24
# This is a module-level variable
def get_cars():
    return _cars[1]
print(get_cars())


def nome_baby():
    a = str(input("insira um nome: "))
    b = str(input("insira um sobrenome: "))
    print(f"o nome escolhido é: {a} {b}")
nome_baby()