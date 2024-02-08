###  EXCEPTIONS  ###

# ImportError: uma importação falha;
# IndexError: uma lista é indexada com um número fora do intervalo;
# NameError: uma variável desconhecida é usada;
# SyntaxError: o código não pode ser analisado corretamente;
# TypeError: uma função é chamada em um valor de um tipo inadequado;
# ValueError: uma função é chamada em um valor do tipo correto, mas com um valor inadequado.

# try:
#    num1 = 7
#    num2 = 0
#    print (num1 / num2)
#    print("Done calculation")
# except ZeroDivisionError:
#    print("An error occurred")
#    print("due to zero division")


# try:
#     variable = 10
#     print (10 / 2)
# except ZeroDivisionError:
#     print("Erro")
#     print("Terminado")

# try:
#    variable = 10
#    print(variable + "hello")
#    print(variable / 2)
# except ZeroDivisionError:
#    print("Divided by zero")
# except (ValueError, TypeError):
#    print("Error occurred")

# try:
#     meaning = 42
#     print(meaning / 0)
#     print("o sentido da vida")
# except (ValueError, TypeError):
#     print("Ocorreu um ValueError ou TypeError")
# except ZeroDivisionError:
#     print("Dividido por zero")

# num = 102
# if num > 100:
#   raise ValueError

# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     raise ValueError

# ## ERRO CASO A ENTRADA SEJA NEGATIVO
# num = -1
# if float(num) < 0:  
#     raise
#     ValueError("Negative!")

# x = 3
# try:
#   x+="2"
# except:
#   x+=2
# else:
#   x+=4
# finally:
#   print(x)


x = 0
try:
  x+=1
  raise ValueError
except NameError:
  x+=1
except ValueError:
  x+=1
else:
  x+=1
finally:
  x+=1
  print(x)