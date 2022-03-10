import os

def cadastrarC(nome:str, cpf:int):
    open('cpf_clientes.txt', 'a')
    if os.path.isfile(f'./{cpf}.txt') == True:
        return print('\nCliente já cadastrado.')

    else:
        arquivo = open(f'{cpf}.txt', 'w')
        arquivo.write(f'Nome: {nome}\nCPF: {cpf}\n')

        with open('cpf_clientes.txt', 'a') as arqCpf:
            arqCpf.write(f'{cpf}\n')

        return print('\nCliente cadastrado com sucesso.')

def cadastrarM(codigo:int, maquina:str, marca:str, modelo:str, ano:int, valor:float, status:str):
    open('codigo_maquinas.txt', 'a')
    if os.path.isfile(f'./{codigo}.txt') == True:
        return print('\nMáquina já cadastrada.')

    else:
        arquivo = open(f'{codigo}.txt', 'w')
        arquivo.write(f'Codigo: {codigo}\nMaquina: {maquina}\nMarca: {marca}\nModelo e Ano: {modelo}/{ano}\nValor: R${valor}\nStatus: {status}')

        with open('codigo_maquinas.txt', 'a') as arqCodigo:
            arqCodigo.write(f'{codigo}\n')

        return print('\nMáquina cadastrada com sucesso.')

def alugarM(cpf:int, codigo:int):
    open('relatorio_aluguel.txt', 'a')
    if os.path.isfile(f'./{cpf}.txt') == False or os.path.isfile(f'./{codigo}.txt') == False:
        return print('\nCliente ou Máquina não registados.')

    else:
        with open(f'{codigo}.txt', 'r') as arqMaquinaL:
            linhaMaquina = arqMaquinaL.readlines()
            for i in linhaMaquina:
                if i == linhaMaquina[1]:
                    tipoMaquina = i[9:999999].strip('\n')
                elif i == linhaMaquina[4]:
                    valor = i[7:999999].strip('\n')

        with open(f'{codigo}.txt', 'w') as arqMaquinaE:
            for i in linhaMaquina:
                if i == linhaMaquina[5]:
                    status = i[8:9999999].strip('\n')
                    if status == 'ALUGADA':
                        arqMaquinaE.write(i)
                        return print('\nMáquina Indisponível.')
                    else:
                        arqMaquinaE.write('Status: ALUGADA')
                        print('\nAluguel realizado com sucesso.')
                else:
                    arqMaquinaE.write(i)

        with open(f'{cpf}.txt', 'r') as arqClienteL:
            linhaCliente = arqClienteL.readlines()
            for i in linhaCliente:
                if i == linhaCliente[0]:
                    nome = i[6:99999].strip('\n')

        with open(f'{cpf}.txt', 'a') as arqClienteE:
            arqClienteE.write(f'Maquina Alugada: {codigo}\n')

        with open('relatorio_aluguel.txt', 'a') as relatorio:
            relatorio.write(f'Cliente: {nome}\nMaquina: {tipoMaquina} - Codigo: {codigo} - Valor: R${valor}\n\n')

def relatarClientes():
    with open('cpf_clientes.txt', 'r') as arquivo:
        cpfs = arquivo.readlines()

    for i in cpfs:
        cpf = i.strip('\n')
        with open(f'{cpf}.txt', 'r') as arqLeitura:
            print(arqLeitura.read())
            print('\n')

def relatarMaquinas():
    with open('codigo_maquinas.txt', 'r') as arquivo:
        codigos = arquivo.readlines()

    for i in codigos:
        codigo = i.strip('\n')
        with open(f'{codigo}.txt', 'r') as arqLeitura:
            print(arqLeitura.read())
            print('\n')

def relatarAlugueis():
    with open('relatorio_aluguel.txt', 'r') as relatorioA:
        return relatorioA.read()