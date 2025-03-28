Pular para o conteúdo principal
Google Sala de Aula
Google Sala de Aula
2024.1 EXA854 - MI - ALGORITMOS (TP03)
Problema 3 - Entrega do código
#Autor: Maria Clara Nunes Ramos
#Componente Curricular: Algoritmos I
#Concluido em:07/07/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.


import random
#Estilização
import winsound
from tabulate import tabulate
import os
#Tratamento de arquivo
import pickle
    
# Tabela e formatação ===========================================================================

def limpa_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def dificuldade():
    limpa_terminal()
    print("=========================================")
    print("\033[1;36m           DIFICULDADE\033[0;0m")
    print("=========================================")
    print('Selecione o nível de dificuldade: ')

    #Entrada da dificuldade
    dificuldade=input("\033[32m[1]Fácil\033[0;0m\n\033[33m[2]Médio\033[0;0m\n\033[31m[3]Difícil\033[0;0m\n")
    
    #Verificação
    while dificuldade not in [1,2,3] and not dificuldade.isnumeric() or dificuldade==" ":
        limpa_terminal()
        print("=========================================")
        print("\033[1;36m           DIFICULDADE\033[0;0m")
        print("=========================================")
        print('Selecione o nível de dificuldade: ')
        dificuldade=input("\033[32m[1]Fácil\033[0;0m\n\033[33m[2]Médio\033[0;0m\n\033[31m[3]Difícil\033[0;0m\n")
    dificuldade=int(dificuldade)

    winsound.Beep(1000,350)
    limpa_terminal()
    
    #Definição da ordem da tabela com base na dificuldade
    tamanho=dificuldade+2
    return tamanho 

def tabelas(tamanho):
    #Tabela auxiliar de índices(vai de 1 a 9,serve para analisar a correspondências da casa informada com a tabela em si)
    tabela = []
    cont = 1
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(cont)
            cont += 1
        tabela.append(linha)

    #Tabela principal de strings,inicialmente preenchida com " "
    #Onde serão inseridos os números com cor,e é exibida ao usuário
    tabela_jogo = []
    for i in range(tamanho):
        lista=[]
        for j in range(tamanho):
            lista.append(" ")
        tabela_jogo.append(lista)

    #Tabela auxiliar de verificação (igual a tabela jogo,porém preenchida com 0 no lugar de " ",e só recebe números inteiros)
    #Será utilizada na verificação de sequências
    tabela_verificar = []
    for i in range(tamanho):
        lista=[]
        for j in range(tamanho):
            lista.append(0)
        tabela_verificar.append(lista)

    
    
    return tabela,tabela_jogo,tabela_verificar

# Definições prévias ================================================================================================================================================

def sorteio():# Sorteia um dos valores dentro da lista de objetivos e atrubui a variável objetivo
    objetivos = ["PARES", "ÍMPARES", "CRESCENTES", "DECRESCENTES"]
    objetivo=random.choice(objetivos)
    return objetivo

def jogadores():
    ranking = carregar_ranking()

    #Nome do jogador 1
    player1=input("\033[34m Jogador 1,digite seu nome: \033[0;0m")
    while player1.isnumeric() or player1==" ":
        player1=input("\033[34mJogador 1,digite seu nome: \033[0;0m")
    winsound.Beep(1200,350)

    #Adiciona o nome do jogador ao ranking com valor 0,após verificar se já não existe
    ranking[player1] = ranking.get(player1, 0)
    
    #Objetivo do jogador 1    
    objetivo1=sorteio()
    print("=========================================")
    print("\033[1;34m             OBJETIVOS\033[0;0m")
    print("=========================================")
    print(f"\033[34mSeu objetivo é formar uma a sequência de N números {objetivo1} em linha (diagonal, vertical ou horizontal,\ncom leitura da esquerda para a direita e de cima para baixo) \033[0;0m")


    input("Aperte ENTER para continuar")
    winsound.Beep(1000,350)
    limpa_terminal()

    #Nome do jogador 2   
    player2=input("\033[31mJogador 2,digite seu nome: \033[0;0m")
    while player2.isnumeric() or player2==" ":
        player2=input("\033[31mJogador 1,digite seu nome: \033[0;0m")
    winsound.Beep(1200,350)


    #Adiciona o nome do jogador ao ranking com valor 0,após verificar se já não existe
    ranking[player2] = ranking.get(player2, 0)
    
    #Objetivo do jogador 2
    objetivo2=sorteio()
    print("=========================================")
    print("\033[1;31m            OBJETIVOS\033[0;0m")
    print("=========================================")
    print(f"\033[31mSeu objetivo é formar uma a sequência de N números {objetivo2} em linha (diagonal, vertical ou horizontal,\ncom leitura da esquerda para a direita e de cima para baixo) \033[0;0m")

    input("Aperte ENTER para continuar")
    winsound.Beep(1000,150)
    winsound.Beep(700,200)
    winsound.Beep(1000,150)
    limpa_terminal()

    return player1,player2,objetivo1,objetivo2,ranking

# Gameplay================================================================================================================================================

def jogada(tamanho,carregado=False, status=None):
    if not carregado:#Cria um novo status de jogo se for False e não houver status
        dados = {}
        #Armazenar jogadas
        jogadas, casas = [], []
        tabela, tabela_jogo, tabela_verificar = tabelas(tamanho)
        player1, player2, objetivo1, objetivo2, ranking = jogadores()

    else:#Carregar status de jogo passado se for True e houver status   
        dados = status
        tabela_jogo = dados["tabela_jogo"]
        tabela_verificar = dados["tabela_verificar"]
        jogadas = dados["jogadas"]
        casas = dados["casas"]
        player1 = dados["player1"]
        player2 = dados["player2"]
        objetivo1 = dados["objetivo1"]
        objetivo2 = dados["objetivo2"]
        ranking = dados["ranking"]
        tabela,_,_=tabelas(tamanho)


        print("=========================================")
        print("\033[1;36m                STATUS\033[0;0m")
        print("=========================================")
        input("Aperte enter para rever o objetivo do jogador 1")
        print(f"O objetivo de {player1} é formar uma a sequência de N números {objetivo1}" )
        
        input("Aperte enter para rever o objetivo do jogador 2")
        limpa_terminal()
        winsound.Beep(1000, 250)

        print("=========================================")
        print("\033[1;36m                STATUS\033[0;0m")
        print("=========================================")
        print(f"O objetivo de {player2} é formar uma a sequência de N números {objetivo2}" )  
        input("Aperte enter para continuar")
        limpa_terminal()
        winsound.Beep(900, 250)

        print("=========================================")
        print("\033[1;36m                STATUS\033[0;0m")
        print("=========================================")
        print("O status da partida passada é:")
        print(tabulate(tabela_jogo, tablefmt="double_grid"))
        input("Aperte enter para continuar")
        
        winsound.Beep(1000, 250)
        limpa_terminal()


    print("====================================================================")
    print("\033[1;36m                       JOGADA ESPECIAL\033[0;0m")
    print("====================================================================")
    #Entrada da escolha jogada especial
    print("-A jogada especial remove uma linha ou uma coluna de números do tabuleiro,e depois \npermite realizar jogada convencional.\n\n-Só pode ser utilizada uma vez\n\n-Para habilita-la,selecione a tecla 'E' no campo 'casa' durante seu turno\n")
    habilitado=input("Deseja habilitar modo de jogo com jogada especial?\nDigite S para sim e ENTER para não: ")
    winsound.Beep(900, 250)
    limpa_terminal()
    
    print(tabulate(tabela, tablefmt="double_grid")) #Tabela auxiliar visual
    input("Aperte enter para continuar")
    winsound.Beep(1000, 250)

    especial_p1=especial_p2=0# Auxuliar para contagem de uso de jogadas especiais

    #Jogadas alternadas
    for i in range(tamanho**2):
        #Jogador1
        if i % 2 == 0:

            #Entrada da casa
            casa_p1 = input(f"\033[34mTurno do jogador 1: Escolha uma casa entre 1 e {tamanho ** 2}: \033[0;0m")
            
            #Jogada especial
            if casa_p1 in ["E","e"] and habilitado in ["S","s"] and especial_p1==0:
                
                tabela_jogo,casas,jogadas=especial(tabela_jogo,tamanho=tamanho,jogadas=jogadas,casas=casas,tabela=tabela)
                especial_p1+=1
                
                #Nova jogada convencional,em caso da especial
                casa_p1 = input(f"\033[34mTurno do jogador 1: Escolha uma casa entre 1 e {tamanho ** 2}: \033[0;0m")
                while not casa_p1.isdigit() or int(casa_p1) not in range(1, tamanho ** 2 + 1) or casa_p1 in casas:
                    casa_p1 = input(f"\033[34mTurno do jogador 1: Escolha uma casa válida entre 1 e {tamanho ** 2}: \033[0;0m")

            #Salva as variáveis e matrizes num dicionário
            elif casa_p1 in ["S", "s"]:
                dados = {
                    "tabela_jogo": tabela_jogo,
                    "tabela_verificar": tabela_verificar,
                    "jogadas": jogadas,
                    "casas": casas,
                    "player1": player1,
                    "player2": player2,
                    "objetivo1": objetivo1,
                    "objetivo2": objetivo2,
                    "ranking": ranking,
                    "tamanho":tamanho,
                }

            #Da update do dicionário em um arquivo pickle
                save(dados)
                print("Jogo salvo com sucesso!")
                return
            
            #Verificação da entrada da casa
            while not casa_p1.isdigit() or int(casa_p1) not in range(1, tamanho ** 2 + 1) or casa_p1 in casas:
                casa_p1 = input(f"\033[34mTurno do jogador 1: Escolha uma casa válida entre 1 e {tamanho ** 2}: \033[0;0m")
            winsound.Beep(1200, 250)

            #Entrada do número
            num_p1 = input(f"\033[34mAgora escolha um número: \033[0;0m")
            while not num_p1.isdigit() or num_p1 in jogadas or int(num_p1) not in range(1, tamanho ** 2 + 1):
                num_p1 = input(f"\033[34mAgora escolha um número válido: \033[0;0m")
        
            #Armazenamento de casas ocupadas e números escolhidos
            casas.append(casa_p1) 
            jogadas.append(num_p1)

            #Diferenciação de jogador por cor e definição de valor de variável
            num_verif1=int(num_p1)
            num_p1=(f"\033[34m{num_p1}\033[0;0m")

            #Atualiza a tabela de exibição e verificação
            tabela_jogo,tabela_verificar=atualiza_tabela(tabela_jogo,tabela,tabela_verificar,tamanho,casa_p1,num_p1,num_verif1)
            winsound.Beep(1000, 250)
            
            #Verifica se já existe algum ganhador no jogo,se sim,acresce 1 vitória no valor correspondente a chave do jogador,
            if verificar_jogada(tabela_verificar, tamanho, objetivo1, player1):
                ranking[player1]+=1
                salvar_ranking(ranking)
                return

        #Jogador2
        else:

            #Entrada da casa
            casa_p2 = input(f"\033[31mTurno do jogador 1: Escolha uma casa entre 1 e {tamanho ** 2}: \033[0;0m")
            
            #Jogada especial
            if casa_p2 in ["E","e"] and habilitado in ["S","s"] and especial_p2==0:
                
                tabela_jogo,casas,jogadas=especial(tabela_jogo,tamanho=tamanho,jogadas=jogadas,casas=casas,tabela=tabela)
                especial_p2+=1
                
                #Nova jogada convencional,em caso da especial
                casa_p2 = input(f"\033[31mTurno do jogador 1: Escolha uma casa entre 1 e {tamanho ** 2}: \033[0;0m")
                while not casa_p2.isdigit() or int(casa_p2) not in range(1, tamanho ** 2 + 1) or casa_p2 in casas:
                    casa_p2 = input(f"\033[31mTurno do jogador 1: Escolha uma casa válida entre 1 e {tamanho ** 2}: \033[0;0m")

            #Salva as variáveis e matrizes num dicionário
            elif casa_p2 in ["S", "s"]:
                dados = {
                    "tabela_jogo": tabela_jogo,
                    "tabela_verificar": tabela_verificar,
                    "jogadas": jogadas,
                    "casas": casas,
                    "player1": player1,
                    "player2": player2,
                    "objetivo1": objetivo1,
                    "objetivo2": objetivo2,
                    "ranking": ranking,
                    "tamanho":tamanho,
                }
                 #Da update do dicionário em um arquivo pickle
                save(dados)
                print("Jogo salvo com sucesso!")
                return   
            
            while not casa_p2.isdigit() or int(casa_p2) not in range(1, tamanho ** 2 + 1) or casa_p2 in casas:
                casa_p2 = input(f"\033[31mTurno do jogador 1: Escolha uma casa válida entre 1 e {tamanho ** 2}: \033[0;0m")
            winsound.Beep(1200, 250)

            #Entrada do número
            num_p2 = input(f"\033[31mAgora escolha um número: \033[0;0m")
            while not num_p2.isdigit() or num_p2 in jogadas or int(num_p2) not in range(1, tamanho ** 2 + 1):
                num_p2 = input(f"\033[31m Agora escolha um número válido: \033[0;0m")            

            #Armazenamento de casas ocupadas e números escolhidos
            casas.append(casa_p2)
            jogadas.append(num_p2)           

            #Diferenciação de jogador por cor e definição de valor de variável
            num_verif2=int(num_p2)
            num_p2=(f"\033[31m{num_p2}\033[0;0m")
            
            #Atualiza a tabela de exibição e verificação
            tabela_jogo,tabela_verificar=atualiza_tabela(tabela_jogo,tabela,tabela_verificar,tamanho,casa_p2,num_p2,num_verif2)
            winsound.Beep(1000, 250)

            #Verifica se já existe algum ganhador no jogo,se sim,acresce 1 vitória no valor correspondente a chave do jogador,
            if verificar_jogada(tabela_verificar, tamanho, objetivo2,player2):
                ranking[player2]+=1
                salvar_ranking(ranking)
                return

    print("EMPATE")        
    return jogadas, casas,tabela_jogo,ranking

def atualiza_tabela(tabela_jogo,tabela,tabela_verificar,tamanho,casa,num,num_verif):   
    for i in range(tamanho):
        for j in range(tamanho):                      #Percorre a tabela
            if tabela[i][j] == int(casa) and num !=0: #Verifica a casa escolhida
                tabela_jogo[i][j] = num               #Adiciona o número (str) na casa da tabela visual
                tabela_verificar[i][j]=num_verif      #Adiciona o mesmo número (int) na mesma casa da tabela de verificação
                
            
    print(tabulate(tabela_jogo, tablefmt="double_grid"))
    return tabela_jogo,tabela_verificar

def verificar_jogada(tabela_verificar, tamanho, objetivo, jogador):
    sequencias=[]   #Lista para armazenar sequencias
    
    for linha in tabela_verificar:    #Percorre as linhas da tabela verificar
        if 0 not in linha:            #Verifica se a sequencia está completa
            sequencias.append(linha)  #Adiciona á lista de sequencias
          
    #Colunas
    for j in range(tamanho):
        coluna=[]
        for i in range(tamanho):
            coluna.append(tabela_verificar[i][j]) #Percorre as colunas da tabela verificar                                         
        if 0 not in coluna:                       #Verifica se a sequencia está completa
            sequencias.append(coluna)             #Adiciona á lista de sequencias
                  
    #Diagonal 1
    diagonal1 = []
    for i in range(len(tabela_verificar)):
        diagonal1.append(tabela_verificar[i][i])  #Percorre a diagonal principal da tabela verificar
    if 0 not in diagonal1:                        #Verifica se a sequencia está completa
        sequencias.append(diagonal1)              #Adiciona á lista de sequencias

    #Diagonal 2
    diagonal2 = []
    for i in range(len(tabela_verificar)):
        diagonal2.append(tabela_verificar[i][len(tabela_verificar)-1-i])    #Percorre a diagonal secundária da tabela verifica
    if 0 not in diagonal2:                                                  #Verifica se a sequencia está completa
        sequencias.append(diagonal2)                                        #Adiciona á lista de sequencias

    
    for sequencia in sequencias: #Percorre as sequencias   
        if verificar_objetivo(sequencia, objetivo): #Verifica se alguma delas se encaixa no objetivo
            print(f"O jogador {jogador} ganhou! Formando a sequência {sequencia} cumprindo o objetivo de formar números {objetivo}")
            return True 
        else: 
            return False

def verificar_objetivo(sequencia, objetivo): 
    if objetivo == "PARES":                                 #Caso o objetivo seja par
        for i in range(len(sequencia)):                     #Percorre a sequencia pelo índice
            if sequencia[0] % 2 == 0 :                      #Verifica se o primeiro elemento é par
                primeiro_valor=sequencia[0]                 
                for j in range(1,len(sequencia)):           #Percorre o índice a partir do j
                    if sequencia[j]!= primeiro_valor+2*j :  #Verifica se a sequencia toda é realmente de pares e consecutiva,tomando como base o primeiro elemento
                        break  
                else:
                    return sequencia              
            
    elif objetivo == "ÍMPARES":                             #Caso o objetivo seja ímpar
        for i in range(len(sequencia)):                     #Percorre a sequencia pelo índice
            if sequencia[0] % 2 != 0 :                      #Verifica se o primeiro elemento é ímpar
                primeiro_valor=sequencia[0]                 
                for j in range(1,len(sequencia)):           #Percorre o índice a partir do j
                    if sequencia[j]!= primeiro_valor+2*j:   #Verifica se a sehquencia toda é realmente de ímpares e consecutiva,tomando como base o primeiro elemento
                        break                               #Se sim,ignora
                else:
                    return sequencia
                             
    elif objetivo == "CRESCENTES":                          #Caso o objetivo seja crescente
        primeiro_valor=sequencia[0]                     
        for j in range(1,len(sequencia)):                   #Percorre a sequencia pelo índice
            if sequencia[j]!= primeiro_valor+j:             #Verifica se os termos posteriores são diferente do primeiro valor+o seu índice 
                break                                       #Se sim,ignora
        else:
            return sequencia
                
    elif objetivo == "DECRESCENTES":                        #Caso o objetivo seja decrescente
        primeiro_valor=sequencia[0]                     
        for j in range(1,len(sequencia)):                   #Percorre a sequencia pelo índice
            if sequencia[j]!= primeiro_valor-j:             #Verifica se os termos posteriores são diferente do primeiro valor+o seu índice
                break                                       #Se sim,ignora
        else:
            return sequencia
    
    return False                                            #Se não retornar nenhuma sequencia,continua

def especial(tabela_jogo,tamanho,casas,jogadas,tabela):
    casas = [int(elemento) for elemento in casas]
    jogadas = [int(elemento) for elemento in jogadas]

    tipo=input("Deseja apagar:\n1-Linha\n2-Coluna\n3-Diagonal\n")
    while int(tipo) not in [1,2,3]:
        tipo = input("Deseja apagar:\n1-Linha\n2-Coluna\n3-Diagonal\n")
    winsound.Beep(1200, 250)
    limpa_terminal()
    
    #Apagar linha(OBS:Os comentários ao lado de apagar linha 1 valem para as outras estruturas de linhas,colunas e diagonais.A diferenciação está comentada na linha em que essa descrição não se encaixa,em cada bloco )
    if int(tipo)==1:

        #Pergunta qual linha
        tipo2=input("Deseja apagar:\n1-Linha 1 \n2-Linha 2\n3-Linha 3\n4-Linha 4 \n5-Linha 5\n")
        while int(tipo2) not in [1,2,3]:
            tipo2 = input("Deseja apagar:\n1-Linha 1 \n2-Linha 2\n3-Linha 3\n4-Linha 4 \n5-Linha 5\n")
            winsound.Beep(1000, 250)
            limpa_terminal()

        for i in range(tamanho):    
            for j in range(tamanho):                        #Percorre a matriz
                    for c in range(len(casas)):             #Percorre a lista de casas ocupadas
                        for jog in range (len(jogadas)):    #Percorre a lista números jogados
                            
                            if int(tipo2) ==1:                          #Se for a primeira linha
                                if i==0 and tabela_jogo[i][j]!=" ":     #Verifica na tabela princial se a linha é a primeira e se a sequencia está completa
                                    if tabela[i][j] == casas[c]:        #Verifica quais as casas da sequencia
                                        casas.pop(c)                    #Apaga as casas da lista de já ocupadas
                                        jogadas.pop(jog)                #Apaga os números da lista de já jogados
                                    tabela_jogo[i][j]=" "               #"Apaga" o número da tabela de exibição

                            elif int(tipo2) ==2:                         
                                if i==1 and tabela_jogo[i][j]!=" ":
                                    if tabela[i][j] == casas[c]:
                                        casas.pop(c)
                                        jogadas.pop(jog)
                                    tabela_jogo[i][j]=" "

                            elif int(tipo2) ==3:                        
                                if i==2 and tabela_jogo[i][j]!=" ":
                                    if tabela[i][j] == casas[c]:
                                        casas.pop(c)
                                        jogadas.pop(jog)
                                    tabela_jogo[i][j]=" "       

                            elif int(tipo2) ==4:                         
                                if i==3 and tabela_jogo[i][j]!=" ":
                                    if tabela[i][j] == casas[c]:
                                        casas.pop(c)
                                        jogadas.pop(jog)
                                    tabela_jogo[i][j]=" " 

                            elif int(tipo2) ==5:                         
                                if i==4 and tabela_jogo[i][j]!=" ":
                                    if tabela[i][j] == casas[c]:
                                        casas.pop(c)
                                        jogadas.pop(jog)
                                    tabela_jogo[i][j]=" "                
    
    #Apagar coluna
    elif int(tipo)==2:
        #Pergunta qual coluna
        tipo2=input("Deseja apagar:\n1-Coluna1 \n2-Coluna2\n3-Coluna3\n4-Coluna4 \n5-Coluna5\n")
        while int(tipo2) not in [1,2,3]:
            tipo2 = input("Deseja apagar:\n1-Coluna1 \n2-Coluna2\n3-Coluna3\n4-Coluna4 \n5-Coluna5\n")
        winsound.Beep(1000, 250)

        for i in range(tamanho):
            for j in range(tamanho):
                for c in range(len(casas)): 
                    for jog in range (len(jogadas)):
                        
                        if int(tipo2) ==1:
                            if j==0 and tabela_jogo[i][j]!=" ":      
                                if tabela[i][j] == casas[c]:
                                    casas.pop(c)
                                    jogadas.pop(jog)
                                tabela_jogo[i][j]=" "
                                
                        elif int(tipo2) ==2:
                            if j==1 and tabela_jogo[i][j]!=" ":
                                if tabela[i][j] == casas[c]:
                                    casas.pop(c)
                                    jogadas.pop(jog)
                                tabela_jogo[i][j]=" "

                        elif int(tipo2) ==3:
                            if i==2 and tabela_jogo[i][j]!=" ":
                                if tabela[i][j] == casas[c]:
                                    casas.pop(c)
                                    jogadas.pop(jog)
                                tabela_jogo[i][j]=" "

                        elif int(tipo2) ==4:
                            if j==3 and tabela_jogo[i][j]!=" ":
                                if tabela[i][j] == casas[c]:
                                    casas.pop(c)
                                    jogadas.pop(jog)
                                tabela_jogo[i][j]=" "

                        elif int(tipo2) ==5:
                            if j==4 and tabela_jogo[i][j]!=" ":
                                if tabela[i][j] == casas[c]:
                                    casas.pop(c)
                                    jogadas.pop(jog)
                                tabela_jogo[i][j]=" "

    #Apagar diagonal
    elif int(tipo)==3:
        
        #Pergunta qual diagonal
        tipo2=input("Deseja apagar:\n1-Diagonal principal \n2-Diagonal secundária\n")
        while int(tipo2) not in [1,2,3]:
            tipo2 = input("Deseja apagar:\n1-Diagonal principal \n2-Diagonal secundária\n")
        winsound.Beep(1000, 250)
        
        for i in range(tamanho):
            for j in range(tamanho):
                for c in range(len(casas)): 
                    for jog in range (len(jogadas)):  
                        if int(tipo2) ==1:
                            if i==j and tabela_jogo[i][j]!=" ":      #Verifica na tabela princial se a linha igual a coluna e se a sequencia está completa
                                if tabela[i][j] == casas[c]:
                                    casas.pop(c)
                                    jogadas.pop(jog)
                                tabela_jogo[i][j]=" "

                        elif int(tipo2) ==2:
                            if i==1 and j==1 and tabela_jogo[i][j]!=" " and i==j-2 and j==i-2: #Verifica na tabela princial se a linha é a primeira e se a sequencia está completa
                                if tabela[i][j] == casas[c]:
                                    casas.pop(c)
                                    jogadas.pop(jog)
                                tabela_jogo[i][j]=" "


    winsound.Beep(300, 250)
    winsound.Beep(400, 250)
    limpa_terminal()
    print(tabulate(tabela_jogo, tablefmt="double_grid"))
    return tabela_jogo,casas,jogadas

#RANKING E SAVE ================================================================================================================================================
def save(dados):
    with open('savegame.pkl', 'wb') as arquivo: #Cria o arquivo de save
        pickle.dump(dados, arquivo)             #Aloca os dados(dicionário) para o arquivo 

def load():
    if os.path.exists('savegame.pkl'):               #Verifica se o save existe
        with open('savegame.pkl', 'rb') as arquivo:  #Abre o arquivo no modo leitura
            return pickle.load(arquivo)              #Carrega os dados salvos no arquivo
    return None

def salvar_ranking(ranking):
    with open('ranking.pickle', 'wb') as rank:       #Cria o arquivo de ranking
        pickle.dump(ranking, rank)                   #Aloca o ranking(dicionário) para o arquivo 

def carregar_ranking():
    try:
        with open('ranking.pickle', 'rb') as rank:  #Lê o arquivo ranking
            return pickle.load(rank)                #Carrega os dados do arquivo ranking
    except FileNotFoundError:                       #Caso não encontrado
        return {}                                   #Cria o ranking(dicionário)
    
def mostrar_ranking():
    ranking = carregar_ranking()                   #Carrega os dados do arquivo ranking 
    for player, score in sorted(ranking.items()):  #Percorre o arquivo ranking,ordena por valor mais alto
        print(f"{player}: {score} vitórias")       #Exibe a chave seguido do valor 

# Main================================================================================================================================================

def main():
    Menu_principal=0
    while Menu_principal!=4: 
        print("=========================================")
        print("\033[1;36m Bem-vind@ ao Jogo da Sequência Numérica!\033[0;0m")
        print("=========================================")
        print("Selecione uma opção:")
        Menu_principal = input("\033[30m[1]Continuar🕹️\033[0;0m\n\033[35m[2]Novo Jogo👾\033[0;0m\n\033[33m[3]Ranking👑\033[0;0m\n\033[31m[4]Sair❌\033[0;0m\nOpção: ")
        
        # Verificar se a opção é um número e está dentro do intervalo válido
        while not Menu_principal.isdigit() or int(Menu_principal) < 1 or int(Menu_principal) > 4:
            Menu_principal = input("\033[30m[1]Continuar🕹️\033[0;0m\n\033[35m[2]Novo Jogo👾\033[0;0m\n\033[33m[3]Ranking👑\033[0;0m\n\033[31m[4]Sair❌\033[0;0m\nOpção: ")
        Menu_principal = int(Menu_principal)
        winsound.Beep(1000,350)
        limpa_terminal()

        #Continuar
        if Menu_principal==1:
            print("=========================================")
            print("\033[1;30mJogo da Sequência Numérica\033[0;0m")
            print("=========================================")
            status = load()         #Veirifica o status do jogo
            if status:              #Se houver carregado,pega os dados do save
                limpa_terminal()
                tamanho = status["tamanho"]     #Inicia jogo conforme tamanho definido em dados
                jogada(tamanho, carregado=True, status=status)     #Inicia jogada conforme dados carregados
            else:
                print("Nenhum jogo salvo encontrado.")
                input("Aperte ENTER para voltar ao menu principal.")
                limpa_terminal()                

        #Novo jogo        
        elif Menu_principal==2:
            tamanho=dificuldade()   #Pergunta a dificuldade
            winsound.Beep(700,200)
            print("=========================================================================================================================================")
            print("\033[1;36m                                                              REGRAS\033[0;0m")
            print("=========================================================================================================================================")
            print("-Cada jogador, em sua vez e de forma alternada, pode selecionar um número dentre os números disponíveis\ne posicionar este número em uma das casas.\n\n-Ganha o jogador que fizer a sequência de N números em linha (diagonal, vertical ou horizontal, com leitura da esquerda para a direita e de cima para baixo) que atende ao seu objetivo.\n\n -O jogo termina em empate se todas as casas do tabuleiro forem marcadas sem que nenhum jogador tenha completado uma sequência de objetivos.\n\n-Para salvar o jogo aperte 'S' no campo 'casa'\n")
            input("Aperte ENTER para continuar")
            winsound.Beep(700,200)
            winsound.Beep(1000,350)
            limpa_terminal()
            jogada(tamanho=tamanho) #Inicia o jogo

        #Mostrar ranking
        elif Menu_principal==3:
            print("=========================================")
            print("\033[1;33m             RANKING👑\033[0;0m")
            print("=========================================")
            mostrar_ranking()

    print("Encerrando jogo...")

if __name__ == "__main__":
    main()
