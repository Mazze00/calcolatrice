#!/usr/bin/env python3

num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))

scelta = input("Scegli l'operazione (+, -, *, /): ")

if scelta == '+':
    risultato = num1 + num2
elif scelta == '-':
    risultato = num1 - num2
elif scelta == '*':
    risultato = num1 * num2
elif scelta == '/':
    if num2 == 0:
        risultato = "Impossibile dividere per zero"
    else:
        risultato = num1 / num2
else:
    risultato = "Operazione non valida"

print("Risultato:", risultato)
