def calcular(operacao, num1, num2):
  if operacao == "+":
    return num1 + num2
  elif operacao == "-":
    return num1 - num2
  elif operacao == "*":
    return num1 * num2
  elif operacao == "/":
    return num1 / num2
  else:
    return None

operacoes = {"+": "Soma", "-": "Subtração", "*": "Multiplicação", "/": "Divisão"}

while True:
  operacao = input("Digite a operação (+, -, *, /): ")
  if operacao not in operacoes:
    print("Operação inválida!")
    continue

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))

  resultado = calcular(operacao, num1, num2)

  if resultado is None:
    print("Divisão por zero não é permitida!")
  else:
    print(f"{operacoes[operacao]}: {num1} {operacao} {num2} = {resultado}")

  continuar = input("Deseja continuar (S/N)? ").upper()
  if continuar != "S":
    break
