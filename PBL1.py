#Autor: Maria Clara Nunes Ramos
#Componente Curricular: Algoritmos I
#Concluido em:21 /04/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

inteira=0
#inteira
meia_estudante=0
#meia estudante
meia_outros=0
#meia outros
preço_inteira=30
#preço inteira
preço_meia=15
#preço meia
preço_ecomp=10
#preço ecomp
ec=0
#ecomp
cort=0
#cortesia
com=0
#comissao
Bio_enferm=0
#vendidos por biologia e enfermagem
Idade=0
#input da Idade
idades=0
#contador de Idade
Média=0
#Média das idades 
mais_vendido=0
#define o tipo de ingresso mais vendido
Vendedor=0
#define se o vendedor é do da ou de cursos comissionados
emitidas=0
#Ingressos emitidos
Total_Ingressos=int(2000)
#quantidade de ingresso
prazo=("27" or "28" or "30")
Menu_principal=0

print('=============== EVENTOS E INGRESSOS ==============')
data=input("Digite a data de hoje(dia):")

while Total_Ingressos !=0 :
#controle por fim de ingressos e encerramento de vendas

    Menu_principal=int(input('1-Ingresso\n2-Configurar\n3-Relatório\n'))
    #menu principal, com opção de rerirar ingresso,exibir o relatório,sair do programa e configurar valores

    if Menu_principal ==1:
        print('UEFS MUSIC FEST\nDIA 30/05\nLOCAL:ARENA UNIVERSITÁRIA-Av. Transnordestina, 3500 - Papagaio, Feira de Santana - BA, 44054-000')
        print(f"Ingressos disponíveis:{Total_Ingressos}") 
        Idade=int(input("Digite sua idade:"))
        #Página pra compra de ingressos

        Vendedor=(input("Informe se você é do DA[1] ou vendedor comissionado[2]"))
        while not (Vendedor).isdigit():
              Vendedor=(input("Informe se você é do DA[1] ou vendedor comissionado[2]"))
              Vendedor==int(Vendedor)
          #Verifica o vendedor e auxilia na contagem das comissões
        
        Tipo_Ingresso=input('Digite "cortesia" para cortesia; "comissão" para comissão ;"meia" para meia entrada;"inteira" para inteira e "ecomp" caso você seja estudante de engenharia de computação:')
        #Leitura e validação de dados de venda de cada ingresso (tipo: ecomp, inteira, meia, cortesia; disponibilidade: vendidos e restantes; preço)
          
        if Tipo_Ingresso in ('MEIAmeia'):
          print('Para meia entrada,são exigidos alguns documentos:')
          if Idade>=60:
            Rg=(input('Por favor, digite seu RG:'))
            while not (Rg).isdigit():
                  Rg=input('Por favor, digite seu RG')
                  Rg==int(Rg)
            P=input('Pagamento:R$')
            while P!=('15'):
              P=input('Por favor, digite novamente,R$15')
            meia_outros+=1
            Total_Ingressos-=1
            print("ingresso garantido!")
            if Vendedor ==2:
              Bio_enferm+=1
        #contagem de ingressos referente á outras meias 
          else:
            Comp=(input('Por favor, digite seu comprovante de matícula:'))
            while not (Comp).isdigit():
                  Comp=input('Por favor, digite seu RG')
                  Comp==int(Comp)
            P=input('Pagamento:R$')
            while P!=('15'):
              P=input('Por favor, digite novamente,R$15')
            meia_estudante+=1
            Total_Ingressos-=1
            print("ingresso garantido!")
            if Vendedor ==2:
              Bio_enferm+=1
        #contagem de ingressos referente ás meias para estudante

        elif Tipo_Ingresso in ('INTEIRAinteira'):
            P=(input('Pagamento:R$'))
            while P!=('30'):
              P=input('Por favor, digite novamente,R$30')
            inteira+=1
            Total_Ingressos-=1
            print("ingresso garantido!")
            if Vendedor ==2:
              Bio_enferm+=1
              #entrada,validação e contagem de ingressos referente ás inteiras

        elif Tipo_Ingresso in ('ECOMPecomp'):
            P=(input('Pagamento:'))
            Comp=(input('Comprovante de matrícula:'))
            while not (Comp).isdigit():
              Comp=input('Por favor, digite novamente,apenas números')
              Comp==int(Comp)
            while P!=('10'):
              P=input('Por favor, digite novamente,R$1')
            ec+=1
            Total_Ingressos-=1
            print("ingresso garantido!")
            if Vendedor ==2:
              Bio_enferm+=1
          #entrada,validação e contagem de ingressos referente á ecomp

        elif Tipo_Ingresso in ('CORTESIAcortesia'):
            senha=(input('Digite sua senha:'))
            while not (senha).isdigit():
              senha=input('Por favor, digite novamente,apenas números')
              senha==int(senha)
            cort+=1
            Total_Ingressos=Total_Ingressos-1
            print("ingresso garantido!")
          #entrada,validação e contagem de ingressos referente ás cortesias

        if (Bio_enferm)<=10:
            while (Bio_enferm)%10!=0:
              com+=1
              Total_Ingressos-=1
              break
        #controle de cortesias: a cada 10 vendas de vendedor comissionado, fornecer uma cortesia

        if Tipo_Ingresso in ('COMISSÃOcomissão'):
          com+=1
        Total_Ingressos-=1
        print("ingresso garantido!")
          #entrada,validação e contagem de ingressos referente ás comissões

        emitidas=ec+inteira+meia_outros+meia_estudante+com+cort
        vendidos=(inteira+meia_outros+meia_estudante+ec)
        #calculo de ingressos vendidos e retirados

        while vendidos>=2:
          idades=+Idade
          Média==idades/vendidos
        #calcula média entre as idades
  
        print('\nRelatório')
        print('Ingressos emitidos:',emitidas)
        #quantidade de ingressos emitidos 
        print('Ingressos não emitidos:',Total_Ingressos)
        #quantidade de ingressos não emitidos
        print('Inteiras vendidas:',inteira)
        print('Meias para estudantes vendidas: ',meia_estudante)
        print('Outras meias vendidas: ',meia_outros)
        #quantidade de meia estudante, de meia outros e de inteiras     
        print("Vendidos para ecomp:",ec)
        #quantidade de ingressos ecomp
        print('Cortesias emitidas:',cort)
        #quantidade de cortesias para DA e convidados
        print('Comissões emitidas:',com)
        #quantidade de cortesias para comissionados
        print('Vendidas por alunos de Biologia e Enfermagem:',Bio_enferm)
        #quantidade de ingressos vendidos por comissionados
        if vendidos>=2:
          print('Média de idade é: ',Média)
        else:
           print("Não fpi possível calcular a média de idade")
        #média de idade dos compradores
        print('Tipo de ingresso mais vendido: ',mais_vendido)
        #tipo de ingresso mais vendido
        print('Arrecadação geral:R$',ec*preço_ecomp+(meia_outros+meia_estudante)*preço_meia+preço_inteira*inteira)
        #total de dinheiro arrecadado
        print("Arrecadação por meias:R$", (meia_outros+meia_estudante)*preço_meia)
        print('Arrecadação por inteiras para ecomp:R$',ec*preço_ecomp)
        print('Arrecadação por inteiras:R$',inteira *preço_inteira) 
        #arrecadação por tipo de ingresso 
        if meia_estudante>meia_outros and meia_estudante>inteira and meia_estudante>ec:
          mais_vendido=('Meia estudante')
        elif meia_outros>meia_estudante and meia_outros>inteira and meia_outros>ec:
          mais_vendido=('Outras meias')
        elif inteira>meia_outros and inteira>meia_estudante and inteira>ec:
          mais_vendido=('Inteira')
        elif ec>meia_outros and ec>inteira and meia_estudante>meia_outros:
          mais_vendido=('Ecomp')
        #verifica e exibe o tipo de ingresso mais vendido    print('\nIngressos emitidos:',Emitidos) 

    if Menu_principal==2:
        preço_inteira=int(input ("Digite o novo valor do ingresso"))
        preço_ecomp=int(input("Digite o novo valor do ingresso com desconto"))
        preço_meia=preço_inteira/2
        cort=int(input ("A partir de quantos ingressos se separa uma cortesia?"))
        Total_Ingressos=('Digite o novo total e ingressos:')
      #Configurar novos valores em caso de outro evento

    elif Menu_principal==3:
        print('\nRelatório') 
        print('Ingressos emitidos:',emitidas)
        #quantidade de ingressos emitidos 
        print('Ingressos não emitidos:',Total_Ingressos)
        #quantidade de ingressos não emitidos
        print('Inteiras vendidas:',inteira)
        print('Meias para estudantes vendidas: ',meia_estudante)
        print('Outras meias vendidas: ',meia_outros)
        #quantidade de meia estudante, de meia outros e de inteiras     
        print("Vendidos para ecomp:",ec)
        #quantidade de ingressos ecomp
        print('Cortesias emitidas:',cort)
        #quantidade de cortesias para DA e convidados
        print('Comissões emitidas:',com)
        #quantidade de cortesias para comissionados
        print('Vendidas por alunos de Biologia e Enfermagem:',Bio_enferm)
        #quantidade de ingressos vendidos por comissionados
        print('Média de idade é: ',Média)
        #média de idade dos compradores
        print('Tipo de ingresso mais vendido: ',mais_vendido)
        #tipo de ingresso mais vendido
        print('Arrecadação geral:R$',ec*preço_ecomp+(meia_outros+meia_estudante)*preço_meia+preço_inteira*inteira)
        #total de dinheiro arrecadado
        print("Arrecadação por meias:R$", (meia_outros+meia_estudante)*preço_meia)
        print('Arrecadação por inteiras para ecomp:R$',ec*preço_ecomp)
        print('Arrecadação por inteiras:R$',inteira *preço_inteira)
        #arrecadação por tipo de ingresso
        if meia_estudante>meia_outros and meia_estudante>inteira and meia_estudante>ec:
          mais_vendido=('Meia estudante')
        elif meia_outros>meia_estudante and meia_outros>inteira and meia_outros>ec:
          mais_vendido=('Outras meias')
        elif inteira>meia_outros and inteira>meia_estudante and inteira>ec:
          mais_vendido=('Inteira')
        elif ec>meia_outros and ec>inteira and meia_estudante>meia_outros:
          mais_vendido=('Ecomp')
        #verifica e exibe o tipo de ingresso mais vendido    print('\nIngressos emitidos:',Emitidos)
        
print("Não há mais ingressos!")
if data != prazo:
  print("Fim do prazo de vendas!")