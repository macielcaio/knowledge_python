def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))

def my_func(f, arg):
  return f(arg)
print(
  my_func(lambda x: 2*x*x, 5)
    )

a = (lambda x: x*x ) (8)
print(a)

def add_five(x):
  return x + 5

# MAPEANDO ITENS DE LISTA E ADICIONANDO 5 EM CADA ITEM
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

# USANDO FILTER DENTRO DE UMA LISTA
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

#USANDO GERADORES YIELD JUNTO COM FOR 
def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1
    
for i in countdown():
  print(i)

def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))


def make_word():
    word = ""
    for ch in "spam":
        word +=ch
        yield word

print(list(make_word()))