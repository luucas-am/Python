import os
import datetime
import pandas as pd

class Vendedor:
    nome = ''
    cpf = ''
    data = datetime
    endereco = ''

    def __init__(self, nome:str, cpf:str, data:datetime, endereco:str):
        self.nome = nome
        self.cpf = cpf
        self.data = data
        self.endereco = endereco
        
    def registrar(self):
        if os.path.isfile('./dados/Vendedores.xlsx') == False:
            df = pd.DataFrame(columns=['Nome', 'CPF', 'Data de Nascimento', 'Endereço'])
            df.to_excel('./dados/Vendedores.xlsx', index=False)

        vendedores = pd.read_excel('./dados/Vendedores.xlsx')
        for i in range(len(vendedores.values)):
            if str(vendedores.loc[i]['CPF']) == self.cpf:
                return print('\nVendedor(a) já Registrado(a).')

        linha = {'Nome': self.nome, 'CPF': self.cpf, 'Data de Nascimento': self.data, 'Endereço': self.endereco}
        vendedores.loc[len(vendedores)] = linha
        vendedores.to_excel('./dados/Vendedores.xlsx', index=False)

        return print('\nVendedor(a) Registrado(a) com Sucesso.')

class Maquinas:
    codigo = ''
    tipo = ''
    precoUni = 0.0
    qtdEsto = 0

    def __init__(self, codigo:str, tipo:str, precoUni:float, qtdEsto:int):
        self.codigo = codigo
        self.tipo = tipo
        self.precoUni = precoUni
        self.qtdEsto = qtdEsto

    def registrar(self):
        if os.path.isfile('./dados/Maquinas.xlsx') == False:
            df = pd.DataFrame(columns=['Código', 'Tipo', 'Preço por Unidade', 'Quantidade em Estoque'])
            df.to_excel('./dados/Maquinas.xlsx', index=False)

        maquinas = pd.read_excel('./dados/Maquinas.xlsx')
        for i in range(len(maquinas.values)):
            if str(maquinas.loc[i]['Código']) == self.codigo:
                return print('\nMáquina já Registrada.')

        linha = {'Código': self.codigo, 'Tipo': self.tipo, 'Preço por Unidade': self.precoUni, 'Quantidade em Estoque': self.qtdEsto}
        maquinas.loc[len(maquinas)] = linha
        maquinas.to_excel('./dados/Maquinas.xlsx', index=False)

        return print('\nMáquina Registrada com Sucesso.')

class Cliente:
    nome = ''
    cpf = ''
    data = datetime
    endereco = ''

    def __init__(self, nome:str, cpf:str, data:datetime, endereco:str):
        self.nome = nome
        self.cpf = cpf
        self.data = data
        self.endereco = endereco
        
    def registrar(self):
        if os.path.isfile('./dados/Clientes.xlsx') == False:
            df = pd.DataFrame(columns=['Nome', 'CPF', 'Data de Nascimento', 'Endereço'])
            df.to_excel('./dados/Clientes.xlsx', index=False)

        clientes = pd.read_excel('./dados/Clientes.xlsx')
        for i in range(len(clientes.values)):
            if str(clientes.loc[i]['CPF']) == self.cpf:
                return print('\nCliente já Cadastrado(a).')

        linha = {'Nome': self.nome, 'CPF': self.cpf, 'Data de Nascimento': self.data, 'Endereço': self.endereco}
        clientes.loc[len(clientes)] = linha
        clientes.to_excel('./dados/Clientes.xlsx', index=False)

        return print('\nCliente Cadastrado(a) com Sucesso.')

class Venda:
    codigo = ''
    cpfV = ''
    cpfC = ''
    data = datetime

    def __init__(self, codigo:str, cpfV:str, cpfC:str, data:datetime):
        self.codigo = codigo
        self.cpfV = cpfV
        self.cpfC = cpfC
        self.data = data

    def registrar(self, codigosM:list, unidades:list):
        if os.path.isfile('./dados/Vendas.xlsx') == False:
            df = pd.DataFrame(columns=['Informações', 'Tipo de Máquina', 'Quantidade Vendida', 'Preço por Unidade', 'Valor Total do Item'])
            df.to_excel('./dados/Vendas.xlsx', index=False)

            dfC = pd.DataFrame(columns=['Código da Venda', 'Nome do Vendedor', 'Valor Total da Venda', 'Valor da Comissão'])
            dfC.to_excel('./dados/Comissoes.xlsx', index=False)

        planilhaV = pd.read_excel('./dados/Vendedores.xlsx')
        for i in range(len(planilhaV.values)):
            if str(planilhaV.loc[i]['CPF']) == self.cpfV:
                nomeV = str(planilhaV.loc[i]['Nome'])
            elif i == len(planilhaV.values) - 1:
                return print('\nVendedor(a) não Registrado(a).')
            
        planilhaC = pd.read_excel('./dados/Clientes.xlsx')
        for x in range(len(planilhaC.values)):
            if str(planilhaC.loc[x]['CPF']) == self.cpfC:
                nomeC = str(planilhaC.loc[x]['Nome'])
            elif x == len(planilhaC.values) - 1:
                return print('\nCliente não Registrado(a).')

        planilhaCom = pd.read_excel('./dados/Comissoes.xlsx')
        for j in range(len(planilhaCom.values)):
            if str(planilhaCom.loc[j]['Código da Venda']) == self.codigo:
                return print('\nCódigo de Venda já Cadastrado.')

        tipos = []
        precos = []
        valorTotalItem = []
        planilhaM = pd.read_excel('./dados/Maquinas.xlsx')
        repetir = 0
        for codigo in codigosM:
            for y in range(len(planilhaM.values)):
                if str(planilhaM.loc[y]['Código']) == codigo:
                    if unidades[repetir] > int(planilhaM.loc[y]['Quantidade em Estoque']):
                        return print('\nQuantidade em Estoque de Máquina Insuficiente.')

                    tipos.append(str(planilhaM.loc[y]['Tipo']))
                    precos.append(float(planilhaM.loc[y]['Preço por Unidade']))
                    valorTotalItem.append(precos[repetir] * unidades[repetir])
                    
                    quantidadeRestante = int(planilhaM.loc[y]['Quantidade em Estoque']) - unidades[repetir]

                    for t in range(1):
                        linhaM = {'Código': codigosM[repetir], 'Tipo': tipos[repetir], 'Preço por Unidade': precos[repetir], 'Quantidade em Estoque': quantidadeRestante}
                        planilhaM.loc[len(planilhaM)] = linhaM
                        planilhaM.drop(index=[y], inplace=True)

                    planilhaM.to_excel('./dados/Maquinas.xlsx', index=False)

                    y = 0
                    repetir+=1
                break
            if repetir != len(codigosM) and codigo == codigosM[len(codigosM)-1]:
                return print('\nMáquina não Registrada.')

        valorTotalVenda = 0
        for k in valorTotalItem:
            valorTotalVenda += k

        tipoLinha = ' '.join(str(t) for t in tipos)
        precoLinha = ' '.join(str(i) for i in precos)
        unidade = ' '.join(str(k) for k in unidades)    
        linhaVI = ' '.join(str(j) for j in valorTotalItem)
        
        info = f'Código da Venda: {self.codigo}\nData da Venda: {self.data}\nNome do Vendedor: {nomeV}\nNome do Cliente: {nomeC}\nValor Total da Venda: {valorTotalVenda}'

        vendas = pd.read_excel('./dados/Vendas.xlsx')
        linha = {'Informações': info, 'Tipo de Máquina': tipoLinha.replace(' ', '\n'), 'Quantidade Vendida': unidade.replace(' ', '\n'), 
                'Preço por Unidade': precoLinha.replace(' ', '\n'), 'Valor Total do Item': linhaVI.replace(' ', '\n')}
        vendas.loc[len(vendas)] = linha
        vendas.to_excel('./dados/Vendas.xlsx', index=False)

        valorComissao = valorTotalVenda * 0.1
        
        comissoes = pd.read_excel('./dados/Comissoes.xlsx')
        linhaC = {'Código da Venda': self.codigo, 'Nome do Vendedor': nomeV, 'Valor Total da Venda': valorTotalVenda, 'Valor da Comissão': valorComissao}
        comissoes.loc[len(comissoes)] = linhaC
        comissoes.to_excel('./dados/Comissoes.xlsx', index=False)

        return print('\nVenda Registrada com Sucesso.')

class Data:
    ano = 0
    mes = 0
    dia = 0

    def __init__(self, ano:int, mes:int, dia:int):
        self.ano = ano
        self.mes = mes
        self.dia = dia

    def formatacao(self):
        mesesTU = [1, 3, 5, 7, 8, 10, 12]
        mesesT = [4, 6, 9, 11]

        if self.dia < 1 or self.dia > 31:
            return AssertionError

        if self.mes in mesesT and self.dia > 30:
            return AssertionError
        elif self.mes in mesesTU and self.dia > 31:
            return AssertionError
        elif self.mes == 2 and self.dia > 29:
            return AssertionError
        elif self.mes == 2 and self.dia > 28 and self.ano % 4 != 0:
            return AssertionError
        else:
            return datetime.date(self.ano, self.mes, self.dia)