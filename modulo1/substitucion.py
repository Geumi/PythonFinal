
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#NQXPOMAFTRHLZGECYJIUWSKDVB #prueba
#YTNSHKVEFXRBAUQZCLWDMIPGJO #prueba

key = input('Escriba la línea de comando: ').lower()

cipherTexto = str 

for i in key:
    if key.count(i) != 1:
        print ('hay caracteres que se repiten')
        print('ciphertexto = 1')
        break
    
if len(key)!= 26:
    print('cantidad incorrecta de caracteres')
    print('ciphertexto = 1')
    

elif key.isalpha() is False:
    print('Existe dígitos que no son letras')
    print('ciphertexto = 1')
    
else:
    cipherTexto == key
    plaintexto = input('escriba su mensaje: ')
    for m in cipherTexto:
        for t in range(0,len(key)):
            key[t] == m
            plaintexto += cipherTexto
 
print (cipherTexto)


    
            



   

