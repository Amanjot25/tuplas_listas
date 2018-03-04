#coding: utf-8

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
  palabra=['Alberto', 'Carmen', 'Benito', 'Daniel']
  cant=int(input("Ingrese las palabras para la lista:"))
for i in range (1,cant+1):
  palabra1=input("Ingrese la palabra")
  palabra.append(palabra1)
print ("La lista creada es:",palabra)
palabra.reverse()
print ("la lista inversa es:",palabra)
