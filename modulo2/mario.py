
while True:
    altura = input('Ingrese la altura de la pirámide: ')

    if altura.isalpha:
        print('Escriba un número')
        continue
    elif int(altura) <=0:
        print('Número inválido, se permite desde el 1 al 8')
        continue
    elif int(altura) > 8: 
        print('Número inválido, se permite desde el 1 al 8')
        continue
    else:
        altura = int(altura)
        for i in range(1,altura+1):
            print(' '*(altura-i),'#'*i)
        break