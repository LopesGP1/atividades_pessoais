

import time

def gerenciador_taf ():
    time.sleep(0.5) 
    print ("\n=== Gerenciador de Tarefas ===")
    time.sleep(0.5) 
    print ( "1. Adicionar Tarefa ")
    time.sleep(0.5) 
    print ("2. Listar Tarefas ")
    time.sleep(0.5) 
    print ("3. Remover Tarefa ")
    time.sleep(0.5) 
    print ("4. Sair ")

def ver_list (lista):
    if len(lista) == 0:
        print("Nenhuma tarefa na lista.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}. {tarefa}")

def adcionar_list (lista):
    tarefa = input("Digite uma tarefa: ")
    lista.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def remover_tarefa(lista):
    ver_list(lista)  # Mostrar as tarefas antes de remover
    if len(lista) > 0:
        try:
            indice = int(input("Digite o número da tarefa a remover: ")) - 1
            if 0 <= indice < len(lista):
                removida = lista.pop(indice)
                print(f"Tarefa '{removida}' removida com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

lista_Tarefas = [] 

# lOOP PRICIPAL 
while True: 
    gerenciador_taf()
    time.sleep(0.5) 
    opcao = int(input ("Escolha uma opação: "))

    if opcao == 1:
        print("Você escolheu a opção 1.")
        adcionar_list (lista_Tarefas)
    elif opcao == 2: 
        print("Você escolheu a opção 2.")
        ver_list(lista_Tarefas)
    elif opcao == 3 :
        print("Você escolheu a opção 3.")
        remover_tarefa(lista_Tarefas)
    elif opcao == 4:
        print ("Até mais !!!")
        break
    else:
        print ("Opção inexistente ")



    


    

