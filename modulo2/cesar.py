
texto = input('ingrese su texto a cifrar: ')

if texto == texto.upper(): 
    tex = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
else:
    tex = 'abcdefghijklmnopqrstuvwxyz'

valor = int (input('Ingrese el valor de desplazamiento: '))

textocifrado = ''

for i in texto:
    if i in tex:
        textocifrado += tex[(tex.index(i)+valor )%len(tex)]
    else:
        textocifrado += i 

print ('El texto cifrado es: ',textocifrado)
