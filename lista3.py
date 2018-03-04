#coding: utf-8

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
  lista=[]
cant=int(input("Ingrese la cantidad de palabras para la lista:"))
for i in range (1,cant+1):
  palabra1=input("Ingrese la palabra")
  lista.append(palabra1)
print (lista)
 
busr= input("Sustituir la palabra: ")
sust = input("por la palabra: ")
for i in range(len(lista)):
  if lista[i] == busr:
    lista[i] = sust
print("La lista es ahora:",lista)
