#coding: utf-8

numero = int(input("Dime cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
  palabra=['Alberto', 'Carmen', 'Benito', 'Carmen']
  cant=int(input("Ingrese las palabras para la lista: "))
for i in range (numero):
      print("Díme la palabra")
      palabra1=input()
      palabra += [palabra1]
print ('La lista es:', palabra)

for i in range(len(palabra)-1, -1, -1):
      if palabra[i] in palabra[:i]:            
           del(palabra[i])
print('La lista sin repetir es:', palabra)


