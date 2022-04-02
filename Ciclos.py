
##################### Ciclo While
contador=1
while contador<=5:
        print("El valor de contador es: "+ str(contador))
        contador+=1

#Omitiendo el valor 3
contador=0
while contador<=5:
    contador += 1
    if contador== 3:
        continue
    print("El valor de contador es: "+ str(contador))

###################### Ciclo For

arreglo=['platano','melon','sandia','pera']

for fruta in arreglo:
    if fruta.endswith('a'):
        print("La fruta es: " + fruta)

print('segundo ejemplo')

for fruta in arreglo:
    if fruta== 'sandia':
        break
    print("La fruta es: " + fruta)

#Comandos para agregar o eliminar elementos dentro de un arreglo
print('Append')
arreglo.append("mango")
print(arreglo)
print('Remove')
arreglo.remove("sandia")
print(arreglo)

#Ejemplo del manejo de posiciones en For en Python
texto='Hola Mundo'
for letra in texto:
    print("Letra: "+ letra)

#Ejemplo de como siempre se empieza desde la posicion 0
for numero in range(7):
    print(numero)