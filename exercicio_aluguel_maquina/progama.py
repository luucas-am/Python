import os
import funcoes as lib

MAQUINAS = ['Perfurador', 'Demolidor', 'Compactador']
while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        #menu
        print('[1] Cadastro de Cliente\n[2] Cadastro de Máquina para Aluguel\n[3] Alugar Máquina')
        print('[4] Relatório de Cliente\n[5] Relatório de Máquinas\n[6] Relatório de Alugueis\n[0] Sair')
        entrada = int(input('Opção desejada: '))
        assert 0 <= entrada <= 6

        #seleção
        os.system('cls' if os.name == 'nt' else 'clear')
        if entrada == 1:
            nome = input('Nome do Cliente: ')
            cpf = input('CPF do Cliente (Apenas Números): ')
            assert len(cpf) == 11

            lib.cadastrarC(nome, int(cpf))

        elif entrada == 2:
            codigo = int(input('Codigo de Indentificação: '))

            print('Tipo de Máquina:\n[1] Perfurador\n[2] Demolidor\n[3] Compactador')
            tipoMaquina = int(input('Tipo desejado: '))
            assert 1 <= tipoMaquina <= 3
            if tipoMaquina == 1:
                maquina = MAQUINAS[0]
            elif tipoMaquina == 2:
                maquina = MAQUINAS[1]
            else:
                maquina = MAQUINAS[2]

            marca = input('\nMarca: ')
            modelo = input('Modelo: ')

            ano = input('Ano (4 dígitos): ')
            assert len(ano) == 4

            valorAluguel = float(input('Valor do Alguel: '))

            status = input('Status (Alugada, Disponivel): ').upper()
            if status == 'DISPONÍVEL':
                status = 'DISPONIVEL'
            assert status == 'ALUGADA' or status == 'DISPONIVEL'

            lib.cadastrarM(codigo, maquina, marca, modelo, int(ano), valorAluguel, status)

        elif entrada == 3:
            cpfAluguel = input('CPF do Cliente: ')
            codigoAluguel = input('Código da Máquina: ')
            
            lib.alugarM(int(cpfAluguel), int(codigoAluguel))

        elif entrada == 4:
            lib.relatarClientes()

        elif entrada == 5:
            lib.relatarMaquinas()

        elif entrada == 6:
            print(lib.relatarAlugueis())

        else:
            break

        input('Pressione Enter Para Continuar.')

    except Exception or AssertionError:
        input('\nInformação Inválida.\nPressione Enter Para Continuar.')