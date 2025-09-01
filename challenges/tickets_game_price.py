criancas = 8
adultos = 12
idosos = 10

while True:
    entrada = input("Insira sua idade (inteiro >= 0): ").strip()

    if entrada.isdigit():  # só entra aqui se TODOS os caracteres forem dígitos
        idade = int(entrada)

        if idade < 12:
            print(f"O valor é de {criancas} reais")
        elif 12 <= idade <= 64:
            print(f"O valor é de {adultos} reais")
        else:  # idade >= 65
            print(f"O valor é de {idosos} reais")
        break  # sai do while
    else:
        print("Erro: digite apenas números inteiros positivos.")
