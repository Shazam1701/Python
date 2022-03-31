chatting=True
while chatting:
    texto = input('>')
    if texto=='salir':
        chatting = False
    texto=texto.replace(':)','💀')
    texto=texto.replace('8)','😎')
    texto=texto.replace(':.)','🥸')
    texto=texto.replace(':*','😘')
    texto=texto.replace(':D','😁')

    print(texto)