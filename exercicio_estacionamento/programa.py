import funcoes as lib
import os

#IDE UTILIZADA -- VISUAL CODE STUDIO
while True:
    try:

        estacionamento = lib.criarMatriz()
        print("IDE ULTILIZADA -- VISUAL CODE STUDIO")
        entrada = input("Deseja Prosseguir ao Menu? (S/N): ").upper()
        assert entrada == 'S' or entrada == 'N'
        if entrada == 'N':
            break

        os.system('cls' if os.name == 'nt' else 'clear')

        for i in range(6):
            print(estacionamento[i])

        #menu
        print("\n1 - Cadastro do Cliente\n2 - Consulta de Clientes\n3 - Reserva de Vaga")
        print("4 - Cancelamento de Reserva de Vaga\n5 - Relatório de Reservas")
        print("6 - Relatório de Vagas Livres\n7 - Relatório de Cancelamento de Reservas de Vagas")
        entrada = int(input("Opção desejada: "))
        assert 1 <= entrada <= 7

        #seleção
        os.system('cls' if os.name == 'nt' else 'clear')
        if entrada == 1:
            nome = input("Nome do Cliente: ")
            cpf = input("CPF do Cliente (123.456.789-10): ")
            lib.cadastro(nome, cpf)
            print("\nCadastro Feito com Sucesso.")

        elif entrada == 2:
            cpfConsulta = input("CPF para consulta: ")
            print(f'\n{lib.consulta(cpfConsulta)}')

        elif entrada == 3:
            fila = int(input("Fila: "))
            vaga = int(input("Vaga: "))
            cpfReserva = input("CPF do Cliente para Reserva: ")

            if lib.reserva(estacionamento, fila, vaga, cpfReserva) == True:
                print(f"\nVaga [{fila},{vaga}] Reservada.")
            else:
                print(f"\nVaga [{fila},{vaga}] Indisponível")

        elif entrada == 4:
            cpf = input("CPF do Cliente para Cancelamento: ")
            lib.cancelamento(cpf)

            print("\nCancelamento Feito com Sucesso.")

        elif entrada == 5:
            print(lib.relReservas())

        elif entrada == 6:
            print(lib.relVagasL())
        
        else:
            print(lib.relCancelamento())

    except Exception or AssertionError:
        input("\nInformação Inválida.\nPressione Enter Para Continuar.")