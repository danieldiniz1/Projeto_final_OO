# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, trabalhos menos remunerados, casas melhor equipadas, entre outros.
# O código apresentado abaixo é apenas um modelo a ser utilizado como referência. O Grupo pode criar uma nova situação e inclusive melhorar o código abaixo.

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
        self.salario = 50
    
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

iniciar = True
dia = 1
relogio = Relogio()
personagem = Personagem()
casa = Casa()
cafe_da_manha = False
while iniciar == True:
    print("---")
    print("São "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até às 07:00.")
    print(personagem)
    print("")
    print("Ações:")
    print("1 - Tomar banho e escovar os dentes")
    print("2 - Fazer café da manhã")
    print("3 - Pedir café da manhã")
    print("4 - Tomar café da manhã")
    print("5 - Tomar remédio")
    print("6 - Comprar remédio")
    print("7 - Ir trabalhar")
    print("0 - Sair do jogo")
    opcao = input("Escolha sua ação:")
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
        print("-=-=-")
        print("Você foi trabalhar.")
        print(personagem)
        relogio.avancaTempo(5)
        print("-=-=-")
        recebido = personagem.salario
        if(not personagem.medicado):
            print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
            recebido = 0
        elif (personagem.medicado):
            while True:
                print()
                print("São "+str(relogio)+" do dia "+str(dia)+". Você tem que trabalhar até as 18:00.")
                print("Ações:")
                print("1 - Bater o ponto.")
                print("2 - Tomar café ")
                print("3 - Ir a mesa de trabalho.")
                print("4 - Enrolar")
                print("5 - Ir ao Almoxarifado")
                print("6 - Trabalhar de verdade.")
                print("7 - Conversar com os colegas.")
                print("8 - Participar da reunião.")
                print("9 - Almoçar.")
                print("10 - Ir para casa.")
                print("0 - Sair do jogo")
                opcao2= input("escola sua ação: ")
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
                    recebido -= personagem.salario - 30
                elif opcao2 == "5":
                    print("Você está no almoxarifado.")
                    relogio.avancaTempo(30)
                    recebido+= personagem.salario * 0.1
                elif opcao2 == "6":
                    print("Você está trabalhando...")
                    relogio.avancaTempo(240)
                    recebido+= personagem.salario * 4
                elif opcao2 == "7":
                    print("Você está conversando com os colegas.")
                    relogio.avancaTempo(20)
                elif opcao2 == "8":
                    print("Você em reunião...")
                    relogio.avancaTempo(30)
                    recebido+= personagem.salario - 20
                elif opcao2 == "9":
                    print("Você está almoçando...")
                    relogio.avancaTempo(90)
                elif opcao2 == "10":
                    print("Você foi para casa...")
                    relogio.avancaTempo(15)
                    personagem.dinheiro += recebido
                    relogio = Relogio()
                    while True:
                        print()
                        print("São "+str(relogio)+" do dia "+str(dia)+". Você está em casa e tem que dormir até as 24:00.")
                        print("Ações:")
                        print("1 - Ir para a academia.")
                        print("2 - Assistir série.")
                        print("3 - Estudar.")
                        print("4 - Tomar Banho")
                        print("5 - Jantar.")
                        print("6 - Ir a farmacia.")
                        print("7 - Ir ao mercado.")
                        print("8 - Dormir.")
                        print("0 - Sair do jogo.")
                        opcao3 = input("escolha sua ação: ")
                        if opcao3 == "1":
                            if personagem.dinheiro >= 10:
                                relogio.avancaTempo(60)
                                personagem.dinheiro-= 10
                                print("Você foi a academia...")
                            else:
                                ("Você não tem dinheiro para pagar a academia!")

                        elif opcao3 == "2":
                                if (personagem.dinheiro >=5):
                                    personagem.dinheiro -= 5
                                    print("Você assistiu suas séries.")
                                    relogio.avancaTempo(180)
                                else:
                                    print('Você não tem dinheiro para pagar a Netflix.')
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
                            print("Você foi a farmacia.")
                            if(personagem.dinheiro >= 20):
                               casa.remedios += 10
                               personagem.dinheiro -= 20
                               relogio.avancaTempo(30)
                            else:
                                print(f"A cartela com 10 remédios custa 20 reais, e você tem: R${personagem.dinheiro:.2f}")
                                relogio.avancaTempo(5)
                        elif opcao3 == "7":
                            if personagem.dinheiro >=150:
                                personagem.dinheiro -=150
                                casa.comida += 10
                                relogio.avancaTempo(120)
                                print("Você foi ao mercado.")
                            else:
                                print(f"As compras custam R$150.00, e você tem: R${personagem.dinheiro:.2f}")
                        elif opcao3 == "8":
                            print("Você foi dormir.")
                            personagem.dinheiro += recebido
                            personagem.dormir()
                            relogio = Relogio()
                            dia+=1
                            
                        elif opcao3 == "0":
                            print("Jogo finalizado.")
                            iniciar = False
                        else:
                            print("Opção inválida!")
                            relogio.avancaTempo(5)
                elif opcao2 == "0":
                    print("Programa finalizado.")
                    iniciar = False
                else:
                    print("Opção inválida!")
                    relogio.avancaTempo(5)

        #elif(personagem.sujo):
         #   print("Como você estava sujo, seus colegas reclamaram para seu chefe, e você levou uma advertência.")
          #  recebido *= 0.9
        #elif(personagem.fome):
         #   print("Como você estava com fome, você trabalhou metade do que consegue trabalhar.")
          #  recebido *= 0.5
        #elif(relogio.atrasado()):
         #   print("Como você chegou atrasado, você produziu menos do que de costume.")
          #  recebido *= 0.8
        #print("Você recebeu "+str(recebido)+" reais pelo seu trabalho hoje.")
        #print("-=-=-")

        #personagem.dinheiro += recebido
        #personagem.dormir()
        #relogio = Relogio()
        
    elif(opcao == "0"):
        iniciar = False
    else:
        print("Opção inválida!")
        relogio.avancaTempo(5)
