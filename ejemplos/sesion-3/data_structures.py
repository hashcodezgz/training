"""Ejercicios sobre estructuras de datos"""

import gc
import sys
import math
from timeit import timeit

# En Python nos encontramos con 4 estrcturas de datos básicas:
# Listas, Tuplas, Diccionarios y Sets

type([])
type({})
type({'key':'value'})
type({1})
type(())
type(0)

# No están tipadas
LISTA = [1, "hola", 3.4]
print(LISTA[1])
print(LISTA[:2])
print(LISTA[1:])
print(LISTA[1:2])
print(LISTA[-1])
print(LISTA[:-1])
print(LISTA[3])

C, D, E = LISTA

BASE = [1, 3, 2, 4]

print([[BASE[:y] for y in BASE[:x] if y % 3 != 0]  for x in BASE])

del LISTA[1]
print(LISTA)

print(sys.getsizeof([1, "hola", 3.4]))

timeit("[]")
timeit("list()")
timeit("{}")
timeit("dict()")
timeit("[1,2,3]")
timeit("list((1,2,3))")
timeit("list(foo)", setup="foo=(1,2,3)")
timeit("{'a':1, 'b':2, 'c':3}")
timeit("dict(bar)", setup="bar=[('a', 1), ('b', 2), ('c', 3)]")

def funct_append():
    """Incrementar añadiendo"""
    lista = []
    for i in range(1000000):
        lista.append(i)

def funct_prealloc():
    """Prealocación"""
    lista = [None]*1000000
    for i in range(1000000):
        lista[i] = i

def array_1():
    """Utilizando arrays"""
    from array import array
    lista = array('i', [0]*1000000)
    for i in range(1000000):
        lista[i] = i

def array_2():
    """Utilizando arrays"""
    from array import array
    lista = array('i', [0])*1000000
    for i in range(1000000):
        lista[i] = i

def numpyzero():
    """Utilizando numpy"""
    from numpy import zeros
    lista = zeros(1000000, dtype='i')
    for i in range(1000000):
        lista[i] = i

gc.collect()
print(timeit(funct_append, number=10))
gc.collect()
print(timeit(funct_prealloc, number=10))
gc.collect()
print(timeit(array_1, number=10))
gc.collect()
print(timeit(array_2, number=10))
gc.collect()
print(timeit(numpyzero, number=10))

print([x for x in range(1, 10)])

def yieldlist(lista):
    """Ejemplo de generador"""
    print("inicio")
    for valor in lista:
        print("inner inicio")
        yield valor
        print("inner final")
    print("final")


YIELD_LIST = yieldlist(range(1, 10))
print(YIELD_LIST)
print(next(YIELD_LIST))

def is_prime(number):
    """Comprueba si number es primo"""
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_primes(number, maximo=1000):
    """Generador de números primos"""
    while number < maximo:
        if is_prime(number):
            yield number
        number += 1

print(get_primes(1))

print([(x, y) for x in range(0, 3) for y in range(0, 3) if x + y > 2])

print([next(get_primes(1)) for x in range(1, 100)])

print([c for c in get_primes(1) if c < 100])
