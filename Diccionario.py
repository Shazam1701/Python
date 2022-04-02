#Diccionario

diccionario={
    "Programar": "Programar es crear todo lo que te puedas imaginar",
    "POO": "Programacion Orientada a Objetos",
    "Rstudio": "El mejor IDE que existe"
}

print(diccionario["POO"])

# Ejercicio de numeros

dic_num={
    "1": "Uno",
    "2": "Dos",
    "3": "Tres",
    "4": "Cuatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Siete",
    "8": "Ocho",
    "9": "Nueve",
    "0": "Cero"
}

num=input("Escribe un numero entero ")

for cont in num:
    print(dic_num[cont])

