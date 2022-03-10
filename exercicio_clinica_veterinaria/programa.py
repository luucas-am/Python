import os
import funcoes as lib

VALOR_CONSULTA = [100.0, 120.0, 150.0]
TIPOS_PETS = ['Cachorro', 'Gato', 'Passaro']
while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        #menu
        print('[1] Cadastro de Veterinário\n[2] Inativação do Cadastro do Veterinário\n[3] Cadastro de Pet')
        print('[4] Registrar Consulta\n[5] Cancelar Consulta\n[6] Relatório de Pets')
        print('[7] Relatório de Veterinários Ativos\n[8] Relatório de Consultas por Data\n[0] Sair')
        entrada = int(input('Opção desejada: '))
        assert 0 <= entrada <= 8

        #seleção
        os.system('cls' if os.name == 'nt' else 'clear')
        if entrada == 1:
            cfmv = input('CFMV: ')
            nome = input('Nome: ')

            cpf = input('CPF (Apenas Números): ')
            assert len(cpf) == 11

            genero = input('Gênero (F/M): ').upper()
            status = input('Status (Ativo/Inativo): ').upper()
            assert genero == 'F' or genero == 'M' and status == 'ATIVO' or status == 'INATIVO'

            lib.cadastrarVet(cfmv, nome, int(cpf), genero, status)

        elif entrada == 2:
            cfmvInativar = input('CFMV do Veterinário para Inativação: ')
            lib.inativarVet(cfmvInativar)

        elif entrada == 3:
            codigo = input('Código Registro do Pet: ')
            nomePet = input('Nome do Pet: ')

            print('Espécie:\n[1] Cachorro\n[2] Gato\n[3] Pássaro')
            especies = int(input('Tipo desejado: '))
            assert 1 <= especies <= 3
            if especies == 1:
                especiePet = TIPOS_PETS[0]
                valor = VALOR_CONSULTA[0]
            elif especies == 2:
                especiePet = TIPOS_PETS[1]
                valor = VALOR_CONSULTA[1]
            else:
                especiePet = TIPOS_PETS[2]
                valor = VALOR_CONSULTA[2]

            lib.cadastrarPet(int(codigo), nomePet, especiePet, valor)

        elif entrada == 4:
            data = input('Data de Consulta (DDMMAAAA): ')
            assert len(data) == 8 and int(data)

            cfmv = input('CFMV do Veterinário: ')
            codigo = input('Codigo de Registro do Pet: ')
            lib.registrarCons(data, cfmv, int(codigo))

        elif entrada == 5:
            dataCons = input('Data de Consulta (DDMMAAAA): ')
            assert len(dataCons) == 8 and int(dataCons)

            cfmvVet = input('CFMV do Veterinário: ')
            codigoPet = input('Codigo de Registro do Pet: ')

            cancelamento = lib.cancelarCons(dataCons, cfmvVet, int(codigoPet))
            if cancelamento == True:
                print('\nCancelamento Feito com Sucesso.')
            elif cancelamento == False:
                print('Consulta já foi Cancelada.')

        elif entrada == 6:
            lib.relatarPets()

        elif entrada == 7:
            lib.relatarVetsA()

        elif entrada == 8:
            dataRel = input('Data do Relatorio de Consultas (DDMMAAAA): ')
            assert len(dataRel) == 8 and int(dataRel)
            lib.relatarCons(dataRel)

        else:
            break

        input('Pressione Enter Para Continuar.')

    except Exception or AssertionError:
        input('\nInformação Inválida.\nPressione Enter Para Continuar.')