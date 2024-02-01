###  FUNÇÕES PERSONALIZADAS  ###

# DEFININDO FUNÇÕES COM ARGUMENTOS #

#🌟 def define uma nova função

#🌟 O corpo da função contém o código que é executado quando a função é chamada

#🌟 return envia valores de volta para que possam ser armazenados e usados no programa

#def personal_greet(name): 
#  print("Hello", name)
#  print("Have a great day")

#personal_greet("James")

#def bmi(weight, height):
#    index = weight / (height * height)
#    return index
#p6 = bmi(79, 1.73)
#print(p6 < 18.5)

#def rect(length, width):
#  area = length * width
#  perimeter = 2 * length + 2 * width
#  return area, perimeter
#print(rect(10, 20))

def rect(d1, d2):
  area = 0
  return area
  area = d1 * d2
print(rect(1,2))

def greet(name="Guest"):
  print("Welcome", name)
greet()

def greet(name="Guest"):
  print("Welcome", name)
greet("Anna")