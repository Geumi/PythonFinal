
print ('Ingrese el número de tarjeta junto y sin guiones')
tarjeta =input ('ingrese un número de tarjeta de crédito: ')

listarj = list(tarjeta)

listarjnum = []
for i in listarj:
    listarjnum.append(int(i))

#print(listarjnum) #comprobación
n = len(listarjnum)
por2 = []

#numeros multiplicados por 2
for j in range(-2,-n-1,-2):        
    por2.append(listarjnum[j]*2)
#print(por2) #comprobación

strpor2 = ''.join(map(str,por2)) #juntar los numeros para tener los digitos por separado
#print(strpor2) #comprobación

listforsum = []
for t in strpor2:
    listforsum.append(int(t))
#print(listforsum) #comprobación

#suma de los multiplicados por 2
#print(sum(listforsum)) #comprobación

#lista de los num restantes
listno2 = []
for x in range(-1,-n-1,-2):        
    listno2.append(listarjnum[x])
#print(listno2) #comprobación

sumatotal = sum(listforsum)+sum(listno2)
#print(sumatotal) #comprobación

strsumtotal = str(sumatotal)
listsumatotal = list(strsumtotal)
#print(listsumatotal) #comprobación


if listsumatotal[-1] == '0':
    
    if listarjnum[0] ==3 and listarjnum[1] ==4:
        print('Tarjeta American Express válida')
    elif listarjnum[0] ==3 and listarjnum[1] ==7:
        print('Tarjeta American Express válida')
    elif listarjnum[0] ==5 and listarjnum[1] ==1:
        print('Tarjeta Mastercard válida')
    elif listarjnum[0] ==5 and listarjnum[1] ==2:
        print('Tarjeta Mastercard válida')
    elif listarjnum[0] ==5 and listarjnum[1] ==3:
        print('Tarjeta Mastercard válida')
    elif listarjnum[0] ==5 and listarjnum[1] ==4:
        print('Tarjeta Mastercard válida')
    elif listarjnum[0] ==5 and listarjnum[1] ==5:
        print('Tarjeta Mastercard válida')
    elif listarjnum[0] ==4 : 
        print('Tarjeta Visa válida')
    else:
        print ('otro tipo de tarjeta válida')
else: 
    print('Tarjeta inválida')





   