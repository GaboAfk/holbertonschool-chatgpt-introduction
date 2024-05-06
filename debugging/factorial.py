#!/usr/bin/python3
import sys

def factorial(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1  # Se debe decrementar n en cada iteración para evitar un bucle infinito
	return result

if len(sys.argv) != 2:
	print("Usage: python script_name.py <number>")
	sys.exit(1)

try:
	f = factorial(int(sys.argv[1]))
	print(f)
except ValueError:
	print("Please enter a valid integer.")
