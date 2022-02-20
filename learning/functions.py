from subprocess import call
from unittest import result


def welcome(name, age):
    print("Hello " + name +" you are "+str(age))

welcome("Kamil", 17)


def cube(number):
    return number*number*number
result= cube(4)
print(result)