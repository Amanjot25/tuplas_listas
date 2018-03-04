#coding: utf-8

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
  palabra=['Carmen', 'Alberto', 'Benito', 'Carmen']
  cant=int(input("Ingrese las palabras para la lista:"))
for i in range (1,cant+1):
  palabra1=input("Ingrese la palabra")
  palabra.append(palabra1)
print ("La lista creada es:",palabra)
print("Digame cuantas palabras tiene la lista:",len(palabra))
buscar=input("palabra a buscar:")
contador=0
for i in palabra:
  if i==buscar:
    contador+=1
print("la palabra ",buscar,"aparece",contador,"veces en la lista")
if contador==0:
  print("la palabra", buscar,"no aparece en la lista")
