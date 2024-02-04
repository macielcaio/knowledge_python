###  RECURSÃO  ###


def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)
    
print(factorial(5))

def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
print(fib(4))

def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))


def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)

print(power(2, 3))

a = (lambda x: x*(x+1)) (6)
print(a)

nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x%2==0, nums))
print(res)

def func(**kwargs):
    print(kwargs["zero"])
func(a = 0, zero = 8)