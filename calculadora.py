#!/usr/bin/python3
# Ejercicio 13.6
# Celia Martin

import sys

if len(sys.argv) != 4:
    sys.exit("usage:ejercicio13_6.py operacion num1 num2")

_, operacion, num1, num2 = sys.argv

num1 = float(num1)
num2 = float(num2)

if operacion == "suma":
    print(num1 + num2)
elif operacion == "division":
    try:
        print (num1 / num2)
    except ZeroDivisionError:
        print("no dividas entre cero")
elif operacion == "resta":
    print(num1 - num2)
elif operacion == "multiplicacion":
    print(num1 * num2)
