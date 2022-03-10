import os
import classe
import datetime
import pandas as pd

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        #Menu
        print('[1] Cadastrar Professores\n[2] Cadastrar Aluno')
        print('[3] Cadastrar Disciplina\n[4] Cadastrar Falta')
        print('[5] Relatorio de Faltas\n[0] Sair')
        entrada = int(input('Opção desejada: '))
        assert 0 <= entrada <= 5

        os.system('cls' if os.name == 'nt' else 'clear')
        #seleção
        if entrada == 1:
            nomeProf = input('Nome do Professor: ')
            matriculaProf = input('Matrícula do Professor: ')
            
            anoProf = input('\nAno de Nascimento do Professor (4 Dígitos): ')
            assert len(anoProf) == 4
            mesProf = int(input('Mês de Nascimento do Professor: '))
            diaProf = int(input('Dia de Nascimento do Professor: '))

            data = classe.Data(anoProf, mesProf, diaProf)
            data.formatacao()

            dataProf = datetime.datetime(int(anoProf), mesProf, diaProf)

            professor = classe.Professor(nomeProf, matriculaProf, dataProf)
            professor.cadastrarP()
        
        elif entrada == 2:
            nomeAluno = input('Nome do Aluno: ')
            matriculaAluno = input('Matrícula do Aluno: ')
            
            anoAluno = input('\nAno de Nascimento do Aluno (4 Dígitos): ')
            assert len(anoAluno) == 4
            mesAluno = int(input('Mês de Nascimento do Aluno: '))
            diaAluno = int(input('Dia de Nascimento do Aluno: '))
            
            data = classe.Data(anoAluno, mesAluno, diaAluno)
            data.formatacao()

            dataAluno = datetime.datetime(int(anoAluno), mesAluno, diaAluno)

            aluno = classe.Aluno(nomeAluno, matriculaAluno, str(dataAluno))
            aluno.cadastrarA()

        elif entrada == 3:
            codigo = input('Código da Disciplina: ')
            nomeDisc = input('Nome da Disciplina: ')
            matriculaP = input('Matrícula do Professor da Disciplina: ')

            disciplina = classe.Disciplina(codigo, nomeDisc, matriculaP)
            disciplina.cadastrarD()

        elif entrada == 4:
            codigoDisc = input('Código da Disciplina: ')
            matriculaA = input('Matrícula do Aluno: ')
            presenca = input('Presença [T/F]: ').upper()
            assert presenca == 'T' or presenca == 'F'

            falta = classe.Falta(codigoDisc, matriculaA, presenca)
            falta.cadastrarF()

        elif entrada == 5:
            codigoDF = input('Código da Disciplina: ')
            print(pd.read_excel(f'./dados/{codigoDF}_Presença.xlsx'))
            input('\nPressione ENTER para Continuar')

        else:
            break

        input('Pressione ENTER para Continuar.')
    
    except AssertionError:
        input('\nInformação Inválida.\nPressione ENTER para Continuar.')