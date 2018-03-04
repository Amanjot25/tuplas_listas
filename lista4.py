#coding: utf-8

lista=[]
cant=int(input("Ingrese la cantidad de palabras para la lista:"))
for i in range (1,cant+1):
  palabra=input("Ingrese la palabra")
  lista.append(palabra)
print (lista)
 
elim= input("eliminar la palabra: ")
for i in range(len(lista)-1,-1,-1):
    if lista[i] == elim:
         del(lista[i])
print("La lista es ahora:",lista)
