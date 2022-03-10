import os

def cadastrarVet(cfmv:str, nome:str, cpf:int, genero:str, status:str):
    open('cfmv_veterinarios.txt', 'a')
    if os.path.isfile(f'./{cfmv}.txt') == True:
        return print('\nVeterinário já Cadastrado.')

    else:
        arquivo = open(f'{cfmv}.txt', 'w')
        arquivo.write(f'CFMV: {cfmv}\nNome: {nome}\nCPF: {cpf}\n'
            f'Genero: {genero}\nStatus: {status}')

        with open('cfmv_veterinarios.txt', 'a') as arqCfmv:
            arqCfmv.write(f'{cfmv}\n')

        return print('\nVeterinário Cadastrado com Sucesso.')

def inativarVet(cfmv:str):
    if os.path.isfile(f'./{cfmv}.txt') == False:
        return print('\nVeterinário Não Cadastrado')

    else:
        with open(f'{cfmv}.txt', 'r') as arqInativoL:
            linhas = arqInativoL.readlines()

        with open(f'{cfmv}.txt', 'w') as arqInativoE:
            for i in linhas:
                if i == linhas[4]:
                    status = i[8:999999].strip('\n')
                    if status == 'INATIVO':
                        arqInativoE.write(i)
                        return print('\nCadastro já Inativo.')
                    else:
                        arqInativoE.write('Status: INATIVO')
                        return print('\nCadastro Inativado.')
                else:
                    arqInativoE.write(i)

def cadastrarPet(codigo:int, nome:str, especie:str, valor:float):
    open('codigo_pets.txt', 'a')
    if os.path.isfile(f'./{codigo}.txt') == True:
        return print('\nPet já Cadastrado.')

    else:
        arquivo = open(f'{codigo}.txt', 'w')
        arquivo.write(f'Codigo Registro: {codigo}\nNome: {nome}\n'
            f'Especie: {especie}\nValor de Consulta: R${valor}')

        with open('codigo_pets.txt', 'a') as arqCodigo:
            arqCodigo.write(f'{codigo}\n')

        return print('\nPet Cadastrado com Sucesso.')

def registrarCons(data:str, cfmv:str, codigo:int):
    if checarData(data) == AssertionError: return int('error')

    dataformatada = f'{data[0:2]}-{data[2:4]}-{data[4:8]}'
    arquivoData = open(f'{dataformatada}.txt', 'a')

    if os.path.isfile(f'./{cfmv}.txt') == False or os.path.isfile(f'./{codigo}.txt') == False:
        return print('\nCFMV ou Pet não Registrados.')
    
    else:
        if os.path.isfile(f'./{codigo}{cfmv}-{data}.txt') == True:
            return print('\nConsulta já foi Marcada.')
        else:
            open(f'{codigo}{cfmv}-{data}.txt', 'w')
            arquivoData.write(f'{codigo}{cfmv}-{data}\n')

        with open(f'{cfmv}.txt', 'r') as leituraVet:
            linhasVet = leituraVet.readlines()
            for linha in linhasVet:
                if linha == linhasVet[1]:
                    nomeVet = linha[6:9999].strip('\n')
                elif linha == linhasVet[4]:
                    status = linha[8:99999].strip('\n')

        with open(f'{codigo}.txt', 'r') as leituraPet:
            linhasPet = leituraPet.readlines()
            for linha in linhasPet:
                if linha == linhasPet[1]:
                    nomePet = linha[6:99999].strip('\n')
                elif linha == linhasPet[3]:
                    valor = linha[21:999999].strip('\n')

        if status == 'ATIVO':
            with open(f'{codigo}{cfmv}-{data}.txt', 'w') as arqConsulta:
                arqConsulta.write(f'Data da Consulta: {dataformatada}\n\nCFMV do Veterinario: {cfmv}\n'
                f'Nome do Veterinario: {nomeVet}\n\nCodigo de Registro do Pet: {codigo}\nNome do Pet: {nomePet}\n'
                f'\nStatus da Consulta: ATIVA\nValor da Consulta: R${valor}')
            return print('\nConsulta Marcada com Sucesso.')

        else:
            return print('\nNão Foi Possível Marcar Consulta: Cadastro de Veterinário Inativado.')

def cancelarCons(data:str, cfmv:str, codigo:int):
    if checarData(data) == AssertionError: return int('error')

    if os.path.isfile(f'./{codigo}{cfmv}-{data}.txt') == False:
        return print('\nConsulta não Registrada.')

    else:
        with open(f'{codigo}{cfmv}-{data}.txt', 'r') as arqConsultaL:
            linhas = arqConsultaL.readlines()

        with open(f'{codigo}{cfmv}-{data}.txt', 'w') as arqConsultaE:
            for i in linhas:
                if i == linhas[8]:
                    status = i[20:9999999].strip('\n')
                    if status == 'INATIVA':
                        arqConsultaE.write(i)
                        cancelamento = False
                    else:
                        arqConsultaE.write('Status da Consulta: INATIVA\n')
                        cancelamento = True
                elif i == linhas[9] and cancelamento == True:
                    arqConsultaE.write('Valor da Consulta: R$0.0')
                else:
                    arqConsultaE.write(i)
        return cancelamento
        
def relatarPets():
    with open('codigo_pets.txt', 'r') as arquivo:
        codigos = arquivo.readlines()

    for i in codigos:
        codigo = i.strip('\n')
        with open(f'{codigo}.txt', 'r') as arqLeitura:
            print(arqLeitura.read())
            print('\n')

def relatarVetsA():
    with open('cfmv_veterinarios.txt', 'r') as arquivo:
        cfmvs = arquivo.readlines()

    for i in cfmvs:
        cfmv = i.strip('\n')
        with open(f'{cfmv}.txt', 'r') as arqLeitura:
            if 'Status: ATIVO' in arqLeitura.read():
                arquivo = open(f'{cfmv}.txt', 'r')
                print(arquivo.read())
                print('\n')

def relatarCons(data:str):
    if checarData(data) == AssertionError: return int('error')

    if os.path.isfile(f'./{data[0:2]}-{data[2:4]}-{data[4:8]}.txt') == False:
        return print('\nNenhuma Consulta Marcada para essa Data.')

    with open(f'{data[0:2]}-{data[2:4]}-{data[4:8]}.txt', 'r') as arquivo:
        consultas = arquivo.readlines()

    totalArrecadado = 0
    for i in consultas:
        consulta = i.strip('\n')
        with open(f'{consulta}.txt', 'r') as arqLeitura:
            linhas = arqLeitura.readlines()
            if linhas[9].startswith('V'):
                totalArrecadado += float(linhas[9][21:99999])
            arquivo = open(f'{consulta}.txt', 'r')
            print(arquivo.read())
            print('\n')

    print(f'Valor Total Arrecadado no dia: {totalArrecadado}')

def checarData(data:str):
    dia = int(data[0:2])
    mes = int(data[2:4])
    ano = int(data[4:8])

    mesesTU = [1, 3, 5, 7, 8, 10, 12]
    mesesT = [4, 6, 9, 11]

    if dia < 1 or dia > 31:
        return AssertionError

    if mes in mesesT and dia > 30:
        return AssertionError
    elif mes in mesesTU and dia > 31:
        return AssertionError
    elif mes == 2 and dia > 29:
        return AssertionError
    elif mes == 2 and dia > 28 and ano % 4 != 0:
        return AssertionError
    else:
        return