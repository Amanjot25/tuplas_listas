#coding: utf-8

numero = int(input("Dime cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
  palabra=['Carmen', 'Alberto', 'Benito', 'Carmen']
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


numero1 = int(input("Dime cuántas palabras tiene la lista: "))

if numero1 < 1:
    print("¡Imposible!")
else:
  palabra1=['Benito', 'Juan', 'Carmen']
  cant=int(input("Ingrese las palabras para la lista: "))
for i in range (numero1):
      print("Díme la palabra")
      palabra2=input()
      palabra1 += [palabra2]
print ('La lista es:', palabra)

for i in range(len(palabra1)-1, -1, -1):
      if palabra1[i] in palabra1[:i]:            
           del(palabra1[i])
print('La lista sin repetir es:', palabra1)

iguales = []
        
for i in palabra:
            if i in palabra1:
                iguales += [i]
print("Palabras que salen en las dos listas:", iguales)

primeraPalabra = []
        
for i in palabra:
            if i not in palabra1:
                primeraPalabra += [i]
print("Palabras que solo salgan en la primera lista:", primeraPalabra)

segundaPalabra = []

for i in palabra1:
            if i not in palabra:
                segundaPalabra += [i]
print("Palabras que solo salgan en la segunda lista:", segundaPalabra)

total = iguales + primeraPalabra + segundaPalabra

print("Total de palabrasen la lista:", total)



