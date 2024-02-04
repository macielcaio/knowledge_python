###  CLASSEs  ###

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("branco", 4)
rover = Cat("caramelo", 4)
stumpy = Cat("marrom", 3)

print("A cor do gato Felix é? " + felix.color)
print("Qual número de patas do gato Felix? " + str(felix.legs))

