# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, trabalhos menos remunerados, casas melhor equipadas, entre outros.
# O código apresentado abaixo é apenas um modelo a ser utilizado como referência. O Grupo pode criar uma nova situação e inclusive melhorar o código abaixo.
from time import sleep

class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    
    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))

class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.dinheiro = 0
        self.salario = 40
    
    def __str__(self):
        return "\033[1;33m Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta.\033m "

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False

class Casa:
    def __init__(self):
        self.remedios = 1
        self.comida = 5

iniciarmanha = True
menu = ["Ações:", "1 - Tomar banho e escovar os dentes", "2 - Fazer café da manhã", "3 - Pedir café da manhã", "4 - Tomar café da manhã", "5 - Tomar remédio", "6 - Comprar remédio", "7 - Ir trabalhar", "0 - Sair do jogo"   ]
dia = 1
relogio = Relogio()
personagem = Personagem()
casa = Casa()
cafe_da_manha = False
nome = input("Digite seu nome: ")
while iniciarmanha == True:
    print()
    print('\033[1;33m',nome+" São "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até às 07:00.\033[m ")
    print(f"\033[1;33m Você tem {casa.comida} comida(s) em casa e {casa.remedios} remedio(s)!\033[m  ")
    print(personagem)
    print("")
    sleep(2)
    for decisao in menu:
        print(f'\033[1;31m {decisao}\033[m' )
        sleep(0.3)
    opcao = input(f"\033[1;32m Escolha sua ação:\033[m ")
    print()
    if(opcao == "1"):
        personagem.sujo = False
        relogio.avancaTempo(20)
    elif(opcao == "2"):
        if(casa.comida > 0):
            casa.comida -= 1
            cafe_da_manha = True
        else:
            print("Não há comida em casa.")
        relogio.avancaTempo(15)
    elif(opcao == "3"):
        if(personagem.dinheiro >= 15):
            personagem.dinheiro -= 15
            cafe_da_manha = True
        else:
            print("O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
        relogio.avancaTempo(5)
    elif(opcao == "4"):
        if(cafe_da_manha):
            personagem.fome = False
            cafe_da_manha = False
            relogio.avancaTempo(15)
        else:
            print("Não tem café da manhã na sua casa.")
            relogio.avancaTempo(5)
    elif(opcao == "5"):
        if(casa.remedios > 0):
            casa.remedios -= 1
            personagem.medicado = True
        else:
            print("Não tem remédio na sua casa")
        relogio.avancaTempo(5)
    elif(opcao == "6"):
        if(personagem.dinheiro >= 20):
            casa.remedios += 10
            personagem.dinheiro -= 20
            relogio.avancaTempo(10)
        else:
            print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
            relogio.avancaTempo(5)
    elif(opcao == "7"):
        recebido = personagem.salario
        if relogio.atrasado():
            print('Você está atrasado e seu salário será descontado R$ 10.00.')
            
        print("\033[1;36m Você foi trabalhar.\033[m")
        relogio.avancaTempo(5)
        #recebido = personagem.salario
        if(not personagem.medicado):
            print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
            recebido = 0
        elif (personagem.medicado):
            iniciartrabalho = True
            menu2 = ["Ações:", "1 - Bater o ponto.", "2 - Tomar café ", "3 - Beber água.", "4 - Enrolar", "5 - Ir ao Almoxarifado",  "6 - Trabalhar de verdade.", "7 - Conversar com os colegas.", "8 - Participar da reunião.", "9 - Almoçar.", "10 - Ir para casa.", "0 - Sair do jogo"   ]
            while iniciartrabalho == True:
                print()
                print('\033[1;33m',nome+ " São "+str(relogio)+" do dia "+str(dia)+". Você tem que trabalhar até as 18:00.")
                print(f' Você tem R${personagem.dinheiro:.2f} na conta.\033[m')
                print()
                sleep(2)
                for decisao2 in menu2:
                    print(f'\033[1;31m {decisao2}\033[m' )
                    sleep(0.3)
                opcao2= input(f"\033[1;32m Escolha sua ação:\033[m ")
                print()
                if opcao2 == "1":
                    print(f"\033[1;36m Você bateu o ponto.\033[m")
                    relogio.avancaTempo(5)
                elif opcao2 == "2":
                    print("\033[1;36m Você Tomou café.\033[m")
                    relogio.avancaTempo(30)
                elif opcao2 == "3":
                    print("\033[1;36m Você bebeu água.\033[m")
                    relogio.avancaTempo(5)
                elif opcao2 == "4":
                    print("\033[1;36m Você está enrolando...\033[m")
                    relogio.avancaTempo(120)
                    recebido -= 20
                elif opcao2 == "5":
                    print("\033[1;36m Você está no almoxarifado.\033[m")
                    relogio.avancaTempo(30)
                    recebido+= personagem.salario * 0.3
                elif opcao2 == "6":
                    print("\033[1;36m Você foi para seu Workspace...\033[m")
                    trabalhando = True
                    trabalhandoacoes = ["Ações:","1 - Fazer relatórios.", "2 - Fazer pesquisas.", "3 - Elaborar Documentos", "4 - Assinar os documentos", "0 - Sair do Workspace"]
                    while trabalhando == True:
                        print()
                        print("\033[1;35m Você está em seu Workspace...\033[m")
                        print('\033[1;35m',nome+ " São "+str(relogio)+" do dia "+str(dia)+". Você tem que trabalhar até as 18:00.\033[m")
                        print()
                        sleep(1)
                        for acoes in trabalhandoacoes:
                            print(f'\033[1;31m {acoes}\033[m' )
                        trab =  input(f"\033[1;32m Escolha sua ação:\033[m ")
                        print()
                        if trab == "1":
                            print("\033[1;36m Você está fazendo relatórios...\033[m")
                            relogio.avancaTempo(60)
                            recebido+= 15
                        elif trab == "2":
                            print("\033[1;36m Você está fazendo pesquisas...\033[m")
                            relogio.avancaTempo(60)
                            recebido+= 15
                        elif trab == "3":
                            print("\033[1;36m Você está elaborando documentos...\033[m")
                            relogio.avancaTempo(60)
                            recebido+= 15
                        elif trab == "4":
                            print("\033[1;36m Você está assinandos os documentos...\033[m")
                            relogio.avancaTempo(30)
                            recebido+= 7
                        elif trab == "0":
                            print("\033[1;36m Você saiu do seu Workspace!\033[m")
                            break
                elif opcao2 == "7":
                    print("\033[1;36m Você está conversando com os colegas.\033[m")
                    relogio.avancaTempo(20)
                elif opcao2 == "8":
                    print("\033[1;36m Você está em reunião...\033[m")
                    relogio.avancaTempo(30)
                    recebido += 20
                elif opcao2 == "9":
                    print("\033[1;36m Você está almoçando...\033[m")
                    relogio.avancaTempo(90)
                elif opcao2 == "10":
                    print("\033[1;36m Você foi para casa...\033[m ")
                    if relogio.atrasado():
                        recebido -= 10
                    relogio.avancaTempo(15)
                    personagem.dinheiro += recebido
                    iniciarnoite = True
                    menu3 = ["Ações:", "1 - Ir para a academia.", "2 - Assistir série.", "3 - Estudar.", "4 - Tomar Banho",  "5 - Jantar.",  "6 - Ir a farmácia.","7 - Ir ao mercado.", "8 - Dormir.", "0 - Sair do jogo."  ]                    
                    while iniciarnoite == True:
                        if relogio.horas >=24:
                            print(" \033[1;31m Passou das 00:00 e você foi dormir...\033[m ")
                            personagem.dormir()
                            relogio = Relogio()
                            dia+=1
                            iniciarnoite = False
                            iniciartrabalho =False
                            break
                         
                        print()
                        print("\033[1;33m",nome + " São "+str(relogio)+" do dia "+str(dia)+". Você está em casa e tem que dormir até as 00:00.\033[m")
                        print(f'\033[1;33m Você tem R${personagem.dinheiro:.2f} na conta, {casa.remedios} remédio(s) e {casa.comida} comida(s) em casa!\033[m')
                        print()
                        sleep(2)
                        for decisao3 in menu3:
                            print(f'\033[1;31m {decisao3}\033[m' )
                            sleep(0.3)
                        opcao3 = input(f"\033[1;32m Escolha sua ação:\033[m ")
                        print()
                        if opcao3 == "1":
                            if personagem.dinheiro >= 10:
                                relogio.avancaTempo(60)
                                personagem.dinheiro-= 10
                                print("\033[1;36m Você foi à academia...\033[m ")                       
                            else:
                                print("\033[1;36m Você não tem dinheiro para pagar à academia!\033[m ")
                                relogio.avancaTempo(15)
                        elif opcao3 == "2":
                                if (personagem.dinheiro >=5):
                                    personagem.dinheiro -= 5
                                    print("\033[1;36m Você assistiu suas séries.\033[m ")
                                    relogio.avancaTempo(180)
                                else:
                                    print('Você não tem dinheiro para pagar à Netflix.')
                        elif opcao3 == "3":
                            print("\033[1;36m Você está estudando...\033[m ")
                            relogio.avancaTempo(120)
                        elif opcao3 == "4":
                            print("\033[1;36m Você tomou banho.\033[m ")
                            relogio.avancaTempo(30)
                        elif opcao3 == "5":
                            print("\033[1;36m Você comeu seu jantar.\033[m ")
                            casa.comida -= 1
                            relogio.avancaTempo(45)
                        elif opcao3 == "6":
                            farm = True
                            print("\033[1;36m Você foi à farmacia.\033[m ")
                            print()
                            sleep(1)
                            while farm == True:
                                print()
                                print(f'\033[1;35m Você está na farmácia \033[m ')
                                print("\033[1;31m Ações: ")
                                print(" 1 - comprar 5 remédios")
                                print(" 2 - comprar 10 remédios")
                                print(" 0 - Sair da farmácia. \033[m")
                                farmopcao = input(f"\033[1;32m Escolha sua ação:\033[m ")
                                print()
                                if farmopcao == "1":
                                    if personagem.dinheiro >=10:
                                        print("\033[1;36m Você comprou a cartela com 5 remédios!")
                                        casa.remedios+=5
                                        personagem.dinheiro-=10
                                    else:
                                        print("\033[1;31m Você não tem dinheiro suficiente!\033[m")
                                elif farmopcao == "2":
                                    if personagem.dinheiro >=20:
                                        print("\033[1;36m Você comprou a cartela com 10 remédios!")
                                        casa.remedios+=10
                                        personagem.dinheiro -=20
                                    else:
                                        print("\033[1;31m Você não tem dinheiro suficiente!\033[m")
                                elif farmopcao == "0":
                                    print("\033[1;36m Você saiu da farmácia!\033[m")
                                    relogio.avancaTempo(45)
                                    break
                                else:
                                    print("\033[1;35m Opção inválida!\033[m ")
                                    relogio.avancaTempo(5)
                        elif opcao3 == "7":
                            print("\033[1;36m Você foi ao mercado.\033[m ")
                            print()
                            merc = True
                            merclis = ["Ações: ", "1 - Comprar lasanha ", "2 - Comprar arroz / feijão", "3 - Comprar carne", "4 - Comprar itens váriados (bolo, doces, salgados, embutidos e enlatados.) ", "0 - Sair do mercado!" ]
                            while merc == True:
                                sleep(1)
                                print(f'\033[1;35m Você está no mercado \033[m ')
                                print()
                                for food in merclis:
                                    print(f'\033[1;31m {food}\033[m')
                                mercopc = input(f"\033[1;32m Escolha sua ação:\033[m ")
                                if mercopc == "1":
                                    if personagem.dinheiro>=10:
                                        print("\033[1;36m Você comprou 2 unidades de lasanha!\033[m")
                                        personagem.dinheiro -=10
                                        casa.comida+= 2
                                        print()
                                    else:
                                        print("\033[1;31m Você não tem dinheiro suficiente!\033[m")
                                elif mercopc == "2":
                                    if personagem.dinheiro>=30:
                                        print("\033[1;36m Você comprou 5 unidades de arroz / feijão!\033[m")
                                        personagem.dinheiro -=30
                                        casa.comida+= 5
                                        print()
                                    else:
                                        print("\033[1;31m Você não tem dinheiro suficiente!\033[m")
                                elif mercopc == "3":
                                    if personagem.dinheiro>=25:
                                        print("\033[1;36m Você comprou 2 unidades de carne!\033[m")
                                        personagem.dinheiro -=25
                                        casa.comida+= 2
                                        print()
                                    else:
                                        print("\033[1;31m Você não tem dinheiro suficiente!\033[m")
                                elif mercopc == "4":
                                    if personagem.dinheiro>=20:
                                        print("\033[1;36m Você comprou produtos váriados!\033[m")
                                        personagem.dinheiro -=20
                                        casa.comida+= 4
                                        print()
                                    else:
                                        print("\033[1;31m Você não tem dinheiro suficiente!\033[m")
                                elif mercopc == "0":
                                    print("\033[1;36m Você saiu do mercado!\033[m")
                                    relogio.avancaTempo(120)
                                    break
                        elif opcao3 == "8":
                            print("\033[1;36m Você foi dormir.\033[m ")
                            #personagem.dinheiro += recebido
                            personagem.dormir()
                            relogio = Relogio()
                            dia+=1
                            iniciarnoite = False
                            iniciartrabalho =False
                        elif opcao3 == "0":
                            print("\033[1;35m Jogo finalizado!\033[m ")
                            iniciarmanha = False
                            iniciartrabalho = False
                            iniciarnoite = False
                        else:
                            print("\033[1;35m Opção inválida!\033[m ")
                            relogio.avancaTempo(5)
                elif opcao2 == "0":
                    print("\033[1;35m jogo finalizado!\033[m ")
                    iniciarmanha = False
                    iniciarnoite = False
                    iniciartrabalho = False
                else:
                    print("\033[1;35m Opção inválida!\033[m ")
                    relogio.avancaTempo(5)
    elif(opcao == "0"):
        print("\033[1;35m Jogo finalizado! \033[m ")
        iniciarmanha = False
    else:
        print("\033[1;35m Opção inválida!\033[m ")
        relogio.avancaTempo(5)


#Fechamento no jogo,
#apresentação, ideia do jogo
#separação em arquivos
#acabar com o looping infinito