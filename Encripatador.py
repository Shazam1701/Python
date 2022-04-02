# Encriptar y Desencripat archivos

#archivo = open('texto.txt','a')
#archivo.write('Prueba de guardado en el archivo')
#archivo.close()

#archivo=open('texto.txt','r')
#print(archivo.read())

#Encripatdor

def encriptar(texto):
    textofinal=''
    for letra in texto:
            textofinal += letra + 'x'
    return  textofinal

def desencriptar(texto):
    print('El texto a desencriptar es: ' + texto)
    textofinal = ''
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textofinal += letra
        contador += 1
    return  textofinal


#encriptar('Prueba de Texto')

#desencriptar('Prueba de Texto')

### funcion mas complicada

def encriptarArchivo():
    archivo = open('texto.txt', 'r')
    texto=archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open('texto.txt', 'w')
    archivo.write(textoEncriptado)
    archivo.close()


def desencriptarArchivo():
    archivo = open('texto.txt', 'r')
    texto=archivo.read()
    archivo.close()
    textoDesncriptado = desencriptar(texto)

    archivo = open('texto.txt', 'w')
    archivo.write(textoDesncriptado)
    archivo.close()


#Quitrar el comentario para realizar la accion que se desea

#encriptarArchivo()
#desencriptarArchivo()


##
respuesta= input('Presione la letra "E" para encriptar, o "D" para desencriptar' )
rutaArchivo = input('Ingrese la ruta del archivo')

