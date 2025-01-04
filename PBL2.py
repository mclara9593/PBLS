#Autor: Maria Clara Nunes Ramos
#Componente Curricular: Algoritmos I
#Concluido em:01/06/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

import csv
import os
from datetime import datetime, timedelta
#bibliotecas importadas

#================================================SEÇÃO DE FORMATAÇÃO===================================================

def limpa_terminal():
    os.system('cls') or None


#Lê o arquivo csv e importa como lista
def boletim(nome_arquivo):
    lista_csv=[]

    with open(nome_arquivo, "r",) as arquivo_csv:
            leitor_csv=csv.reader(arquivo_csv,delimiter=",")
            lista_csv=[]
            for linha in leitor_csv:
                lista_csv.append(linha)
            lista_csv.pop(0)
    return lista_csv

#Cria um arquivo csv com cabeçalho e o importa como lista
def formatar_boletim(nome_arquivo):
    lista_csv = []
    with open(nome_arquivo,'w') as csvfile:
        criar_csv=csv.writer(csvfile, delimiter=',').writerow(['Data','Bairros','Habitantes','Casos Suspeitos'',Casos Negativos','Casos Confirmados'])
        for linha in criar_csv:
            lista_csv.append(linha)
        lista_csv.pop(0) # Remove cabeçalho
    return lista_csv

#Exibe a tabela completa
def ler_total(lista_csv):
    print('{:^15}|{:^20}|{:^15}|{:^15}|{:^15}|{:^15}'.format(
        "DATA","BAIRRO","HABITANTES","SUSPEITOS","NEGADOS","CONFIRMADOS"))
    for linha in lista_csv:
        print('{:^15}|{:^20}|{:^15}|{:^15}|{:^15}|{:^15}'.format(
            linha[0], 
            linha[1],
            linha[2], 
            linha[3], 
            linha[4],
            linha[5]))

#Acrescenta datas na matriz,a partir da última,utilizando datetime para converter de string para formato 'time'
def acrescentar_datas(lista_csv):
    data = lista_csv[-1][0]  
    ultima_data = datetime.strptime(data, "%d/%m/%Y")
    proxima_data = ultima_data + timedelta(days=1)
    nova_linha = [proxima_data.strftime("%d/%m/%Y"), '', '', 0, 0, 0]
    lista_csv.append(nova_linha)
    print("Nova data adicionada:", proxima_data.strftime("%d/%m/%Y"))

#Filtra a partir da última data,valores das outras colunas(exeto bairro) e converte para inteiro
def converter(lista_csv):
        for linha in lista_csv:
            if linha[0] == lista_csv[-1][0]:
                hab=int(linha[2])
                casos_sus=int(linha[3])
                casos_neg =int(linha[4])
                casos_pos=int(linha[5])
        return hab,casos_sus,casos_neg,casos_pos


#===============================================SEÇÃO DE PESQUISA=============================================================

# Exibe dados da mattriz referentes á data informada pelo usuário
def busca_data(lista_csv):
    data=input("Por favor,informe a data deseja verificar:\n")
    print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(
    "BAIRRO","HABITANTES","SUSPEITOS","NEGADOS","CONFIRMADOS"))
    for linha in lista_csv:
        if linha[0] == data:
            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(
     linha[1], 
     linha[2], 
     linha[3], 
     linha[4], 
     linha[5]))

#Exibe dados da matriz referentes ao bairro informada pelo usuário
def busca_bairro(lista_csv):
    bairro=input("Por favor,informe o bairro que deseja verificar:\n")
    for linha in lista_csv:
        if linha[1] == bairro:
            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(
    "DATA","HABITANTES","SUSPEITOS","NEGADOS","CONFIRMADOS"))
            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(
     linha[0], 
     linha[2], 
     linha[3], 
     linha[4], 
     linha[5])) 

#Exibe dados da matriz referentes ao intervalo de datas informado,bem como diferença bruta e percentual entre os casos
def busca_intervalo(lista_csv):
    
    data1_str = input("Digite a primeira data (formato DD/MM/AAAA):\n")
    while data1_str not in lista_csv[0]:
        data1_str=input("Por favor,informe uma data válida:\n")
    data2_str = input("Digite a segunda data (formato DD/MM/AAAA):\n")

# Conversão das datas para formato time
    data1 = datetime.strptime(data1_str, "%d/%m/%Y")
    data2 = datetime.strptime(data2_str, "%d/%m/%Y")

#Filtro do intervalo   
    for linha in lista_csv:
        data_atual = datetime.strptime(linha[0], "%d/%m/%Y")
        if data1 <= data_atual <= data2:
            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format("BAIRRO","HABITANTES","SUSPEITOS","NEGADOS","CONFIRMADOS"))
            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(
                linha[1], 
                linha[2], 
                linha[3], 
                linha[4], 
                linha[5])) 
            
# Guarda negativos e positivos das datas em variáveis manipuláveis,pelo índice da lista
        if linha[0]==data1_str:
            negData1=int(linha[4])
            posData1=int(linha[5])
        if linha[0]==data2_str:
                negData2=int(linha[4]) 
                posData2=int(linha[5]) 

                diferença_pos=0
                diferença_neg=0
                diferença_pos=posData2-posData1
                diferença_neg=negData2-negData1

                porcentagem_negs=diferença_neg*(100/negData1)
                porcentagem_pos=diferença_pos*(100/posData1)

    print(f'Indicadores de prevalência entre as datas {data1_str} e {data2_str}')
    print(f'Diferença entre casos positivos: {"%.1f" % diferença_pos}, Diferença entre casos negativos: {"%.1f" % diferença_neg}')
    print(f'Diferença entre casos positivos(percentual): {"%.1f" % porcentagem_pos}%, Diferença entre casos negativos(percentual): {"%.1f" % porcentagem_negs}%')


#Exibe a porcentagem de casos suspeitos,positivos e negativos em relação ao total
def porcentagem_geral(lista_csv):
    hab,casos_sus,casos_neg,casos_pos=converter(lista_csv)

    total=casos_sus+casos_neg+casos_pos

    porcentagem_suspeito=casos_sus*(100/total)
    porcentagem_positivos=casos_pos*(100/total)
    porcentagem_negativos=casos_neg*(100/total)

    print('|------------------INDICADORES DE PREVALÊNCIA------------------|')
    print(f'Casos positivos: {"%.1f" % porcentagem_positivos}%, Casos negativos: {"%.1f" % porcentagem_negativos}%')
    print(f'Casos suspeitos: {"%.1f" % porcentagem_suspeito}%')


# Exibe a porcentagem de casos suspeitos,positivos e negativos em relação ao bairro informado
def porcentagem_bairro(lista_csv):
    bairro = input("Aperte a tecla ENTER para verificar a porcentagem\n")
    hab,casos_neg,casos_pos,casos_sus = converter(lista_csv)

    porcentagem_positivos=casos_pos*(100/hab)
    porcentagem_negativos=casos_neg*(100/hab)

    print('|------------------INDICADORES DE PREVALÊNCIA------------------|')
    print(f'Casos positivos: {"%.1f" % porcentagem_positivos}%, Casos negativos: {"%.1f" % porcentagem_negativos}%')

#===============================================SEÇÃO DE EDIÇÃO======================================================================

# Permite atualização de dados referentes aos casos suspeitos a partir do bairro
def alterar_suspeitos(lista_csv):
    bairro=input("Os dados a serem alterados são referentes a qual localidade? \n(OBS:Informar com base no endereço)").strip().title()
    suspeitos_atualizados=int(input("Informe a quantidade de suspeitos:"))
    
    print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(
        "DATA","BAIRRO","HABITANTES","SUSPEITOS","NEGADOS","CONFIRMADOS"))
    hab,casos_sus,casos_neg,casos_pos=converter(lista_csv)
    
    for linha in lista_csv:
        if linha[1] == bairro and linha[0] == lista_csv[-1][0]:  
            casos_sus += suspeitos_atualizados
            linha[3]=casos_sus
            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(   
            linha[0], 
            linha[1], 
            linha[2], 
            linha[3], 
            linha[4],
            linha[5])) 

    modificar_arquivo(lista_csv)
               
# Permite atualização de dados referentes aos casos negativos a partir do bairro
def alterar_negativados(lista_csv):
    bairro=input("Os dados a serem alterados são referentes a qual localidade? \n(OBS:Informar com base no endereço)").strip().title()
    negativados_atualizados=int(input("Informe a quantidade de negativados: "))
    
    print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(
        "DATA","BAIRRO","HABITANTES","SUSPEITOS","NEGADOS","CONFIRMADOS"))
    
    hab,casos_sus,casos_neg,casos_pos=converter(lista_csv)
    for linha in lista_csv:
        if linha[1] == bairro and linha[0] == lista_csv[-1][0]:
            casos_neg += negativados_atualizados 
            casos_sus -= negativados_atualizados
            linha[3]=casos_sus
            linha[4]=casos_neg

            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(   
            linha[0], 
            linha[1], 
            linha[2], 
            linha[3], 
            linha[4],
            linha[5])) 
    
    modificar_arquivo(lista_csv)
        
# Permite atualização de dados referentes aos casos positivos a partir do bairro
def alterar_positivados(lista_csv):
    bairro=input("Os dados a serem alterados são referentes a qual localidade? \n(OBS:Informar com base no endereço)").strip().title()
    positivos_atualizados=int(input("Informe a quantidade de confirmados: "))
    print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(
        "DATA","BAIRRO","HABITANTES","SUSPEITOS","NEGADOS","CONFIRMADOS"))
    
    hab,casos_sus,casos_neg,casos_pos=converter(lista_csv)

    for linha in lista_csv:
        if linha[1] == bairro and linha[0] == lista_csv[-1][0]:
            casos_pos += positivos_atualizados  
            casos_sus -= positivos_atualizados
            linha[3]=casos_sus
            linha[5]=casos_pos

            print('{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}'.format(   
            linha[0], 
            linha[1], 
            linha[2], 
            linha[3], 
            linha[4],
            linha[5])) 

    modificar_arquivo(lista_csv)


#===============================================SEÇÃO PRINCIPAL=============================================================

#Passa as informações da lista para o csv
def modificar_arquivo(lista_csv):
    with open("DadosDengue.csv", "w", newline='') as arquivo:
        writer = csv.writer(arquivo)
        for registro in lista_csv:
            writer.writerow(registro)    

#Menu Principal
def main():

    #Trata o erro caso o arquivo não seja encontrado
    nome_arquivo = input('Digite o nome do documento que deseja abrir,".",formato (exemplo:DadosDengue.csv): ')
    try:
        lista_csv=boletim(nome_arquivo)
    except FileNotFoundError:
        lista_csv = formatar_boletim(nome_arquivo)

    # Menu principal
    Menu_principal=0
    while Menu_principal!=3: 
        print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------------LEITURA-------------------------------------------------------------|\n")
        Menu_principal=int(input("[1]Informações sobre a dengue\n[2]Cadastro\n[3]Sair\nOpção:"))
        limpa_terminal()
        if Menu_principal==1:
            print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------------LEITURA-------------------------------------------------------------|\n")
            Menu_Secundário_busca=int(input("[1]Dados por data específica\n\n[2]Dados por bairro\n\n[3]Dados por intervalo de data\n\n[4]Boletim completo\n\nOpção:"))
            limpa_terminal()

            if Menu_Secundário_busca==1:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------------LEITURA-------------------------------------------------------------|\n")
                busca_data(lista_csv)
                
            
            elif Menu_Secundário_busca==2:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------------LEITURA-------------------------------------------------------------|\n")
                busca_bairro(lista_csv)
                porcentagem_bairro(lista_csv)

            elif Menu_Secundário_busca==3:
                print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------LEITURA-E-CADASTRAMENTO---------------------------------------------------------|\n")
                busca_intervalo(lista_csv)

            elif Menu_Secundário_busca==4:
                ler_total(lista_csv)
                porcentagem_geral(lista_csv)

        elif Menu_principal==2:
            print("|------------------------------------------------------------DENGUE-FREE-FEIRA------------------------------------------------------------|\n|---------------------------------------------------------CADASTRAMENTO---------------------------------------------------------|\n")
            Menu_secundário_edição=int(input("Alterar número de:\n[1]Suspeitos de dengue \n\n[2]Casos positivos\n\n[3]Casos negativos\n\n"))
            limpa_terminal()

            if Menu_secundário_edição==1:
                alterar_suspeitos(lista_csv)

            elif Menu_secundário_edição==2:
                alterar_positivados(lista_csv)

            elif Menu_secundário_edição==3:
                alterar_negativados(lista_csv)

    print('Fechando programa')

#Retorna a função principal sempre que sua execução chega ao fim
if __name__ == "__main__":
    main()