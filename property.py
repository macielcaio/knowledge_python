### PROPERTY ###

# A função setter define o valor da propriedade correspondente.
# A função getter obtém o valor.
# Para definir um setter, você precisa usar um decorador com o mesmo nome da propriedade, seguido por um ponto e a palavra-chave setter.
# O mesmo se aplica para definir funções getter .


class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    
  @property
  def pineapple_allowed(self):
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True


## setter e getter

# class Pizza:
#   def __init__(self, toppings):
#     self.toppings = toppings
#     self._pineapple_allowed = False

#   @property
#   def pineapple_allowed(self):
#     return self._pineapple_allowed

#   @pineapple_allowed.setter
#   def pineapple_allowed(self, value):
#     if value:
#       password = input("Enter the password: ")
#       if password == "Sw0rdf1sh!":
#         self._pineapple_allowed = value
#       else:
#         raise ValueError("Alert! Intruder!")
      
# pizza = Pizza(["cheese", "tomato"])  # create a Pizza instance
# print(pizza.pineapple_allowed)  # print the value of pizza._pineapple_allowed
# pizza.pineapple_allowed = True  # set the value of pizza._pineapple_allowed, this will ask for a password
# print(pizza.pineapple_allowed)  # we entered the password, so pizza._pineapple_allowed has been set to True