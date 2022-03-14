import os
import classe
import pandas as pd

if os.path.isdir('./dados') == False:
    os.makedirs('dados')

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        #menu
        print('[1] Cadastrar Vendedor\n[2] Cadastrar Máquinas\n[3] Cadastrar Cliente')
        print('[4] Registrar Venda\n[5] Relatório de Vendedores\n[6] Relatorio de Máquinas')
        print('[7] Relatório de Clientes\n[8] Relatório de Vendas\n[9] Relatório de Comissões\n[0] Sair')
        entrada = int(input('Opção desejada: '))
        assert 0 <= entrada <= 9

        os.system('cls' if os.name == 'nt' else 'clear')
        #seleção
        if entrada == 1:
            nome = input('Nome do Vendedor: ')
            cpf = input('CPF do Vendedor: ')

            ano = int(input('\nAno de Nascimento do Vendedor (4 Dígitos): '))
            assert ano >= 1931
            mes = int(input('Mês de Nascimento do Vendedor: '))
            dia = int(input('Dia de Nascimento do Vendedor: '))
            data = classe.Data(ano, mes, dia)
            dataV = data.formatacao()

            endereco = input('Endereço do Vendedor: ')

            vendedor = classe.Vendedor(nome, cpf, dataV, endereco)
            vendedor.registrar()

        elif entrada == 2:
            codigo = input('Código da Máquina: ')
            tipo = input('Tipo de Máquina: ').upper()
            precoUni = float(input('Preço Unitário: '))
            qtdEsto = int(input('Quantidade em Estoque: '))

            maquina = classe.Maquinas(codigo, tipo, precoUni, qtdEsto)
            maquina.registrar()

        elif entrada == 3:
            nome = input('Nome do(a) Cliente: ')
            cpf = input('CPF do(a) Cliente: ')

            ano = int(input('\nAno de Nascimento do(a) Cliente (4 Dígitos): '))
            assert ano >= 1931
            mes = int(input('Mês de Nascimento do(a) Cliente: '))
            dia = int(input('Dia de Nascimento do(a) Cliente: '))
            data = classe.Data(ano, mes, dia)
            dataC = data.formatacao()

            endereco = input('Endereço do(a) Cliente: ')

            cliente = classe.Cliente(nome, cpf, dataC, endereco)
            cliente.registrar()

        elif entrada == 4:
            codigoV = input('Código de Venda: ')
            cpfVend = input('CPF do Vendedor: ')
            cpfCliente = input('CPF do Cliente: ')

            ano = int(input('\nAno da Venda: '))
            assert ano >= 1931
            mes = int(input('Mês da Venda: '))
            dia = int(input('Dia da Venda: '))
            data = classe.Data(ano, mes, dia)
            dataVenda = data.formatacao()

            codigos = []
            unidades = []
            repeticao = int(input('\nQuantidade de Itens: '))
            for i in range(repeticao):
                codigoM = input(f'Código da {i+1}° Máquina: ')
                codigos.append(codigoM)

                unidade = int(input('Quantidade: '))
                unidades.append(unidade)

            venda = classe.Venda(codigoV, cpfVend, cpfCliente, dataVenda)
            venda.registrar(codigos, unidades)

        elif entrada == 5:
            impressaoV = pd.read_excel('./dados/Vendedores.xlsx')
            print(impressaoV)

        elif entrada == 6:
            impressaoM = pd.read_excel('./dados/Maquinas.xlsx')
            print(impressaoM)

        elif entrada == 7:
            impressaoC = pd.read_excel('./dados/Clientes.xlsx')
            print(impressaoC)

        elif entrada == 8:
            impressaoVenda = pd.read_excel('./dados/Vendas.xlsx')
            print(impressaoVenda)

        elif entrada == 9:
            impressaoComissao = pd.read_excel('./dados/Comissoes.xlsx')
            print(impressaoComissao)

        else:
            break

        input('Pressione ENTER para Continuar.')

    except AssertionError:
        input('\nInformação Inválida.\nPressione ENTER para Continuar.')