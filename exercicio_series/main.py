contador = 1
soma = 0
fracoes = []
texto = ''
linha = ''

n = int(input())

if n > 0:
    while contador <= n:

        s = (contador)/(contador*3)

        soma += s
        if contador == n:
            texto += f'{contador}/{contador*3}'
            linha += '%d/%d' %(contador, contador*3)
            fracoes.append(f'{contador}/{contador*3}')
        else:
            texto += f'{contador}/{contador*3} + '
            linha += '%d/%d + ' %(contador, contador*3)
            fracoes.append(f'{contador}/{contador*3} + ')

        contador += 1

    for fracao in fracoes:
        print(fracao, end='')
    
    print('\n' + texto)
    print(linha)
    print('%.2f' %soma)

else:
    print('%.2f' %soma)