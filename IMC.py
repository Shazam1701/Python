# Calculadora de IMC
# IMC = Peso/ (Altura)^2
# <19: Delgado
# Entre 20 y 25: normal
# Entre 26 y 30: Obesidad

peso= float(input('Ingrese su peso en kg: '))
altura= int(input('Ingrese su altura en cm: '))
altura= altura/100

IMC = peso/(altura)**2

if IMC<20:
    print("Su IMC es " + str(IMC) + "usted es una persona delgada")
if IMC>=20 and IMC<=26:
    print("Su IMC es " + str(IMC) + "usted es una persona normal")
if IMC>=30:
    print("Su IMC es " + str(IMC)  + "usted es una persona obesa")

### Usar una funcion

def calculoIMC(peso,altura):
    altura = altura / 100
    IMC = peso / (altura) ** 2
    return IMC

calculoIMC(75,175)