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
        self.salario = 30
    
    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta."

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
    print("---")
    print(nome+" São "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até às 07:00.")
    print(f"Você tem {casa.comida} comida(s) em casa e {casa.remedios} remedio(s)! ")
    print(personagem)
    print("")
    sleep(1)
    for decisao in menu:
        print(decisao)
        #sleep(0.5)
    sleep(1)
    opcao = input("Escolha sua ação: ")
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
            
        print("-=-=-")
        print("Você foi trabalhar.")
        print(personagem)
        relogio.avancaTempo(5)
        print("-=-=-")
        #recebido = personagem.salario
        if(not personagem.medicado):
            print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
            recebido = 0
        elif (personagem.medicado):
            iniciartrabalho = True
            menu2 = ["Ações:", "1 - Bater o ponto.", "2 - Tomar café ", "3 - Ir a mesa de trabalho.", "4 - Enrolar", "5 - Ir ao Almoxarifado",  "6 - Trabalhar de verdade.", "7 - Conversar com os colegas.", "8 - Participar da reunião.", "9 - Almoçar.", "10 - Ir para casa.", "0 - Sair do jogo"   ]
            while iniciartrabalho == True:
                print()
                print(nome+ " São "+str(relogio)+" do dia "+str(dia)+". Você tem que trabalhar até as 18:00.")
                print(f'Você tem R${personagem.dinheiro:.2f} na conta.')
                print()
                sleep(1)
                for decisao2 in menu2:
                    print(decisao2)
                    #sleep(0.5)
                opcao2= input("escola sua ação: ")
                print()
                if opcao2 == "1":
                    print("Você bateu o ponto.")
                    relogio.avancaTempo(5)
                elif opcao2 == "2":
                    print("Você Tomou café.")
                    relogio.avancaTempo(30)
                elif opcao2 == "3":
                    print("Você está no seu Workspace.")
                    relogio.avancaTempo(5)
                elif opcao2 == "4":
                    print("Você está enrolando...")
                    relogio.avancaTempo(120)
                    recebido -= 20
                elif opcao2 == "5":
                    print("Você está no almoxarifado.")
                    relogio.avancaTempo(30)
                    recebido+= personagem.salario * 0.3
                elif opcao2 == "6":
                    print("Você está trabalhando...")
                    relogio.avancaTempo(240)
                    recebido += personagem.salario 
                elif opcao2 == "7":
                    print("Você está conversando com os colegas.")
                    relogio.avancaTempo(20)
                elif opcao2 == "8":
                    print("Você está em reunião...")
                    relogio.avancaTempo(30)
                    recebido += 20
                elif opcao2 == "9":
                    print("Você está almoçando...")
                    relogio.avancaTempo(90)
                elif opcao2 == "10":
                    print("Você foi para casa...")
                    if relogio.atrasado():
                        recebido -= 10
                    relogio.avancaTempo(15)
                    personagem.dinheiro += recebido
                    iniciarnoite = True
                    menu3 = ["Ações:", "1 - Ir para a academia.", "2 - Assistir série.", "3 - Estudar.", "4 - Tomar Banho",  "5 - Jantar.",  "6 - Ir a farmácia.","7 - Ir ao mercado.", "8 - Dormir.", "0 - Sair do jogo."  ]                    
                    while iniciarnoite == True:
                        print()
                        print(nome + " São "+str(relogio)+" do dia "+str(dia)+". Você está em casa e tem que dormir até as 24:00.")
                        print(f'Você tem R${personagem.dinheiro:.2f} na conta, {casa.remedios} remédio(s) e {casa.comida} comida(s) em casa!')
                        print()
                        sleep(1)
                        for decisao3 in menu3:
                            print(decisao3)
                            sleep(0.5)
                        opcao3 = input("escolha sua ação: ")
                        print()
                        if opcao3 == "1":
                            if personagem.dinheiro >= 10:
                                relogio.avancaTempo(60)
                                personagem.dinheiro-= 10
                                print("Você foi à academia...")                       
                            else:
                                print("Você não tem dinheiro para pagar à academia!")
                                relogio.avancaTempo(15)
                        elif opcao3 == "2":
                                if (personagem.dinheiro >=5):
                                    personagem.dinheiro -= 5
                                    print("Você assistiu suas séries.")
                                    relogio.avancaTempo(180)
                                else:
                                    print('Você não tem dinheiro para pagar à Netflix.')
                        elif opcao3 == "3":
                            print("Você está estudando...")
                            relogio.avancaTempo(120)
                        elif opcao3 == "4":
                            print("Você tomou banho.")
                            relogio.avancaTempo(30)
                        elif opcao3 == "5":
                            print("Você comeu seu jantar.")
                            casa.comida -= 1
                            relogio.avancaTempo(90)
                        elif opcao3 == "6":
                            print("Você foi à farmacia.")
                            if(personagem.dinheiro >= 20):
                               casa.remedios += 5
                               personagem.dinheiro -= 20
                               relogio.avancaTempo(30)
                            else:
                                print(f"A cartela com 10 remédios custa 20 reais e você tem: R${personagem.dinheiro:.2f}")
                                relogio.avancaTempo(5)
                        elif opcao3 == "7":
                            if personagem.dinheiro >=75:
                                personagem.dinheiro -=75
                                casa.comida += 5
                                relogio.avancaTempo(120)
                                print("Você foi ao mercado.")
                            else:
                                print(f"As compras custam R$150.00 e você tem: R${personagem.dinheiro:.2f}")
                        elif opcao3 == "8":
                            print("Você foi dormir.")
                            #personagem.dinheiro += recebido
                            personagem.dormir()
                            relogio = Relogio()
                            dia+=1
                            iniciarnoite = False
                            iniciartrabalho =False
                        elif opcao3 == "0":
                            print("Jogo finalizado!")
                            iniciarmanha = False
                            iniciartrabalho = False
                            iniciarnoite = False
                        else:
                            print("Opção inválida!")
                            relogio.avancaTempo(5)
                elif opcao2 == "0":
                    print("jogo finalizado!")
                    iniciarmanha = False
                    iniciarnoite = False
                    iniciartrabalho = False
                else:
                    print("Opção inválida!")
                    relogio.avancaTempo(5)
    elif(opcao == "0"):
        print("Jogo finalizado! ")
        iniciarmanha = False
    else:
        print("Opção inválida!")
        relogio.avancaTempo(5)
