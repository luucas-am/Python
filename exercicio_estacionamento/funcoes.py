def criarMatriz():
    DIMENSAO = [6, 10]
    matriz = []

    open('vagas_ocupadas.txt', 'a')
    open('relatorio_vagas_livres.txt', 'w')

    for x in range(DIMENSAO[0]):
        linha = []
        for y in range(DIMENSAO[1]):
            with open('vagas_ocupadas.txt') as vagasO:
                if f'[{x},{y}]' in vagasO.read():
                    linha.append('O')
                else:
                    linha.append('X')
                    with open('relatorio_vagas_livres.txt', 'a') as vagasL:
                        vagasL.write(f'[{x + 1},{y + 1}]')
                        if y == 9:
                            vagasL.write('\n')
        matriz.append(linha)

    return matriz

def cadastro(nome:str, cpf:str):
    cliente = open(f'{cpf}.txt', 'w')
    cliente.write(f'Nome: {nome}\nCPF: {cpf}\n')

def consulta(cpf:str):
    with open(f'{cpf}.txt', 'r') as arqConsulta:
        x = arqConsulta.read()
    return x

def reserva(matriz:list ,fila:int, vaga:int, cpf:str):
    open('relatorio_reservas.txt', 'a')

    #verificar se espaço foi ocupado
    if matriz[fila - 1][vaga - 1] == 'O':
        return False

    #marcar espaço ocupado e escrever nos arquivos
    else:
        matriz[fila - 1][vaga - 1] = 'O'
        with open('vagas_ocupadas.txt', 'a') as vagasOcupadas:
            vagasOcupadas.write(f"[{fila - 1},{vaga - 1}]\n")

        with open(f'{cpf}.txt', 'a') as arqReserva:
            arqReserva.write("Vaga do estacionamento: [{0},{1}]".format(fila, vaga))

        with open(f'{cpf}.txt', 'r') as leituraR:
            linha = leituraR.readlines()
            for i in linha:
                if i == linha[0]:
                    nome = i[6:99999].strip('\n')

        with open('relatorio_reservas.txt', 'a') as escritaR:
            escritaR.write(f"Vaga [{fila},{vaga}] - Reservada para {nome}\n")

        return True

def cancelamento(cpf:str):
    #leitura do arquivo para poder remover a linha do estacionamento
    with open(f'{cpf}.txt', 'r') as arqLeitura:
        linha = arqLeitura.readlines()
    
    #remoção da linha do arquivo
    with open(f'{cpf}.txt', 'w') as arqCancela:
        for i in linha:
            if i == linha[0]:
                nome = i[6:99999].strip('\n')
            if i == linha[2]:
                filaVaga = [int(i[25]) - 1, int(i[27:29].strip(']')) - 1]
            else:
                arqCancela.write(i)

    #leitura do arquivo para desocupar o lugar
    with open('vagas_ocupadas.txt', 'r') as arqVagaL:
        linha = arqVagaL.readlines()

    #remoção da vaga ocupada
    conteudoV = (f"[{filaVaga[0]},{filaVaga[1]}]")
    with open('vagas_ocupadas.txt', 'w') as arqVagaC:
        for x in linha:
            if x.strip('\n') != conteudoV:
                arqVagaC.write(x)

    #escrever que vaga foi cancelada
    with open('relatorio_cancelamento.txt', 'a') as relCan:
        relCan.write(f"Vaga [{filaVaga[0] + 1},{filaVaga[1] + 1}] - Reserva Cancelada\n")

def relReservas():
    with open('relatorio_reservas.txt', 'r') as relatorioR:
        return relatorioR.read()

def relVagasL():
    with open('relatorio_vagas_livres.txt', 'r') as relatorioVL:
        return relatorioVL.read()

def relCancelamento():
    with open('relatorio_cancelamento.txt', 'r') as relatorioC:
        return relatorioC.read()