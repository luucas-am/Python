import os
import datetime
import pandas as pd

class Professor:
    nome = ''
    matricula = ''
    dataNascimento = datetime

    def __init__(self, nomeP:str, matriculaP:str, dataNascimentoP:datetime):
        self.nome = nomeP
        self.matricula = matriculaP
        self.dataNascimento = dataNascimentoP

    def cadastrarP(self):
        if os.path.isfile('./dados/Professores.xlsx') == False:
            df = pd.DataFrame(columns=['Nome', 'Matrícula', 'Data de Nascimento'])
            df.to_excel('./dados/Professores.xlsx', index=False)

        excelProfessores = pd.read_excel('./dados/Professores.xlsx')
        for i in range(len(excelProfessores.values)):
            if str(excelProfessores.loc[i]['Matrícula']) == self.matricula:
                return print('\nProfessor(a) já Cadastrado(a)')

        linha = {'Nome': self.nome, 'Matrícula': self.matricula, 'Data de Nascimento': self.dataNascimento}
        excelProfessores.loc[len(excelProfessores)] = linha
        excelProfessores.to_excel('./dados/Professores.xlsx', index=False)

        return print('\nProfessor(a) Cadastrado(a) com Sucesso.')

class Aluno:
    nome = ''
    matricula = ''
    dataNascimento = datetime

    def __init__(self, nomeA:str, matriculaA:str, dataNascimentoA:datetime):
        self.nome = nomeA
        self.matricula = matriculaA
        self.dataNascimento = dataNascimentoA

    def cadastrarA(self):
        if os.path.isfile('./dados/Alunos.xlsx') == False:
            df = pd.DataFrame(columns=['Nome', 'Matrícula', 'Data de Nascimento'])
            df.to_excel('./dados/Alunos.xlsx', index=False)

        excelAlunos = pd.read_excel('./dados/Alunos.xlsx')
        for i in range(len(excelAlunos.values)):
            if self.matricula == str(excelAlunos.loc[i]['Matrícula']):
                return print('\nAluno(a) já Cadastrado(a)')

        linha = {'Nome': self.nome, 'Matrícula': self.matricula, 'Data de Nascimento': self.dataNascimento}
        excelAlunos.loc[len(excelAlunos)] = linha
        excelAlunos.to_excel('./dados/Alunos.xlsx', index=False)

        return print('\nAluno(a) Cadastrado(a) com Sucesso.')

class Disciplina:
    codigo = ''
    nome = ''
    matriculaProf = ''

    def __init__(self, codigoD:str, nomeD:str, matriculaPr:str):
        self.codigo = codigoD
        self.nome = nomeD
        self.matriculaProf = matriculaPr

    def cadastrarD(self):
        if os.path.isfile('./dados/Disciplinas.xlsx') == False:
            df = pd.DataFrame(columns=['Código', 'Nome', 'Matrícula do Professor'])
            df.to_excel('./dados/Disciplinas.xlsx', index=False)

        xlsxProf = pd.read_excel('./dados/Professores.xlsx')
        for i in range(len(xlsxProf.values)):
            if str(xlsxProf.loc[i]['Matrícula']) == self.matriculaProf:

                excelDisciplinas = pd.read_excel('./dados/Disciplinas.xlsx')
                for x in range(len(excelDisciplinas.values)):
                    if str(excelDisciplinas.loc[x]['Código']) == self.codigo:
                        return print('\nDisciplina já Cadastrada.')

                linha = {'Código': self.codigo, 'Nome': self.nome, 'Matrícula do Professor': self.matriculaProf}
                excelDisciplinas.loc[len(excelDisciplinas)] = linha
                excelDisciplinas.to_excel('./dados/Disciplinas.xlsx', index=False)

                return print('\nDisciplina Cadastrada com Sucesso.')
        
            elif i == len(xlsxProf.values)-1:
                return print('\nProfessor não Cadastrado.')

class Falta:
    codigoDisc = ''
    matriculaAluno = ''
    presenca = ''

    def __init__(self, codigoD:str, matriculaA:str, presenca:str):
        self.codigoDisc = codigoD
        self.matriculaAluno = matriculaA
        self.presenca = presenca

    def cadastrarF(self):
        if os.path.isfile(f'./dados/{self.codigoDisc}_Presença.xlsx') == False:
            df = pd.DataFrame(columns=['Disciplina', 'Professor', 'Aluno', 'Presença'])
            df.to_excel(f'./dados/{self.codigoDisc}_Presença.xlsx', index=False)

        excelFaltas = pd.read_excel(f'./dados/{self.codigoDisc}_Presença.xlsx')
        excelDisc = pd.read_excel('./dados/Disciplinas.xlsx')
        for i in range(len(excelDisc.values)):
            if str(excelDisc.loc[i]['Código']) == self.codigoDisc:
                nomeDisc = excelDisc.loc[i]['Nome']
                matriculaProf = excelDisc.loc[i]['Matrícula do Professor']
            elif i == len(excelDisc.values)-1:
                return print('\nDisciplina não Cadastrada.')

        input()
        excelProf = pd.read_excel('./dados/Professores.xlsx')
        for j in range(len(excelDisc.values)):
            if excelProf.loc[j]['Matrícula'] == matriculaProf:
                nomeProf = excelProf.loc[j]['Nome']

        excelAlunos = pd.read_excel('./dados/Alunos.xlsx')
        for k in range(len(excelAlunos.values)):
            if str(excelAlunos.loc[k]['Matrícula']) == str(self.matriculaAluno):
                nomeAluno = excelAlunos.loc[k]['Nome']
            elif i == len(excelAlunos.values)-1:
                return print('\nAluno(a) não Cadastrado(a).')

        if self.presenca == 'F':
            marca = 'X'
        else:
            marca = 'O'

        linha = {'Disciplina': nomeDisc, 'Professor': nomeProf, 'Aluno': nomeAluno, 'Presença': marca}
        excelFaltas.loc[len(excelFaltas)] = linha
        excelFaltas.to_excel(f'./dados/{self.codigoDisc}_Presença.xlsx', index=False)

        return print('\nFalta Cadastrada com Sucesso.')

class Data:
    ano = 0
    mes = 0
    dia = 0

    def __init__(self, ano, mes, dia):
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
            return