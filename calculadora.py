def suma(a,b):
  return a+b

def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial
