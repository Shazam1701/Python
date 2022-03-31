print('Hello world')

# Creacion de variables
nombre = "Marco"

# Concatenation
print('Hola mundo, mi nombre es ' + nombre)

# Tambien lo podemos guardar como una variable
texto = ('Hola mundo, mi nombre es ' + nombre)

print(texto)

# Ejemplo de Edades
edad = 20
if edad >= 18:
    print("Es mayor de edad ")
else:
    print("Es menor de edad ")

# Ejemplo dinamico
nombre2 = input('¿Como te llamas? ')
edad2 = int(input('¿Cuantos años tienes? '))

if edad2 >= 18:
    print(nombre2 + " es mayor de edad ")
else:
    print(nombre2 + "es menor de edad ")

# Mas condiciones

edad3 = int(input('¿Cuantos años tienes? '))
MayorEdad = edad3 >= 18
privilegio = input('¿Eres socio del club? ')
res_privilegio = privilegio == 'si'

acceso= MayorEdad or res_privilegio

if acceso:
    print('Bienvenido, usted puede pasar')
else:
    print('Lo sentimos, usted no tiene acceso')