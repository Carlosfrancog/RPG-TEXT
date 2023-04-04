import random
from time import sleep
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


print("""
                                            -------------------------------------------------------------------------------------                
                                            |  ##   ##   ##  ##             ####   ### ###   #####    ######    ####    ######  |
                                            |  ### ###   ##  ##            ##  ##  ##   ##  ##   ##   # ## #   ##  ##   ##      |
                                            |  #######    #  #            ##       ##   ##  ##   ##     ##    ##        ##      |
                                            |  #######    ####            ##       #######  ##   ##     ##    ##        #####   |
                                            |  ## # ##     ##             ##       ##   ##  ##   ##     ##    ##        ##      |
                                            |  ##   ##     ##              ##  ##  ##   ##  ##   ##   # ## #   ##  ##   ##      |
                                            |  ##   ##     ##               ####   ### ###   #####    ######    ####    ######  |
                                            -------------------------------------------------------------------------------------

            """)
menu_quest = str(input(''' 
         [A] para jogar
         [B] para ir para as confingurações
         [C] para sair
         :''')).upper().strip()[0]

while menu_quest not in 'ABC':
   print("""
                                            -------------------------------------------------------------------------------------                
                                            |  ##   ##   ##  ##             ####   ### ###   #####    ######    ####    ######  |
                                            |  ### ###   ##  ##            ##  ##  ##   ##  ##   ##   # ## #   ##  ##   ##      |
                                            |  #######    #  #            ##       ##   ##  ##   ##     ##    ##        ##      |
                                            |  #######    ####            ##       #######  ##   ##     ##    ##        #####   |
                                            |  ## # ##     ##             ##       ##   ##  ##   ##     ##    ##        ##      |
                                            |  ##   ##     ##              ##  ##  ##   ##  ##   ##   # ## #   ##  ##   ##      |
                                            |  ##   ##     ##               ####   ### ###   #####    ######    ####    ######  |
                                            -------------------------------------------------------------------------------------

            """)
   print('OPÇÃO INVÁLIDA!') 
   menu_quest = str(input(''' 
         [A] para jogar
         [B] para ir para as confingurações
         [C] para sair
         :''')).upper().strip()[0]


if menu_quest in 'A':
   sleep(0.5)
   clear_screen()
   print('''
            Olá forasteiro, vejo que não é desse mundo! 
            Me diga então seu nome para que eu possa me lembrar de você
                             _       _
                            (_\     /_)
                              ))   ((
                            .-"""""""-.
                        /^\/  _.   _.  \/^\ 
                        \(   /__\ /__\   )/
                         \,  \_°/_\°_/  ,/
                           \    (_)    /
                            `-.'==='.-'
                             __) - (__
                            /  `~~~`  \ 
                           /  /     \  \ 
                           \ :       ; /
                            \|==(*)==|/
                             :       :
                              \  |  /
                            ___)=|=(___
                           (____/ \____)''')
      
   name = str(input('DIGITE AQUI O SEU NOME: '))
   clear_screen()
   print(f'Muito bem, {name}')
   print(f'''
            Alguma vez você já se perguntou se controla realmente suas ações
            ou se apenas tem a ilusão de que está controlando?
            Saiba que você {name} está entrando em campos muito perigosos...
            Neste mundo ninguém é confiavél. Será que são eles que estão seguindo
            as suas vidas como querem ou tem algo além por trás? Se ficou curioso
            te convido a tentar descobir, e te proponho um desáfio. Me diga o nome
            de três seres divinos que estão escondidos nesse mundo, se conseguir, eu te 
            revelo se isso é apenas um jogo ou não...
                             _       _
                            (_\     /_) 
                              ))   ((
                            .-"""""""-.
                        /^\/  _.   _.  \/^\ 
                        \(   /__\ /__\   )/
                         \,  \_°/_\°_/  ,/
                           \    (_)    /
                            `-.'==='.-'
                             __) - (__
                            /  `~~~`  \ 
                           /  /     \  \ 
                           \ :       ; /
                            \|==(*)==|/
                             :       :
                              \  |  /
                            ___)=|=(___
                           (____/ \____)  
            ''')
   quest = str(input('Aceita? [S/N]:' )).upper().strip()[0]
   while quest not in 'SN':
      print('OPS! Resposta inválida!')
      quest = str(input('Aceita? [S/N]:' )).upper().strip()[0]
      
   if quest in 'N':
      print(f'''
            Muito bem {name}, até a próxima!
                             _       _
                            (_\     /_)
                              ))   ((
                            .-"""""""-.
                        /^\/  _.   _.  \/^\ 
                        \(   /__\ /__\   )/
                         \,  \_°/_\°_/  ,/
                           \    (_)    /
                            `-.'==='.-'
                             __) - (__
                            /  `~~~`  \ 
                           /  /     \  \ 
                           \ :       ; /
                            \|==(*)==|/
                             :       :
                              \  |  /
                            ___)=|=(___
                           (____/ \____)''')
      sleep(1.5)
      clear_screen()
   else:
      sleep(1.5)
      clear_screen()
      print('''
            Você aceitou o desafio de Pixie duente.
            
            Você abre seus olhos e percebe estar em uma pequena
            cama de madeira, num quarto escuro, umido e fedido.
            Consegue ver uma janela e uma porta dento do quarto, apenas.
            ''')
   
      quest = str(input('''
                     [A] Ir ver a janela
                     [B] Ir até a porta
                     ESCOLHA AQUI:''')).upper()[0]
      while quest not in 'AB':
         print('Opção inválida!')
         quest = str(input('''
                     [A] Ir ver a janela
                     [B] Ir até a porta
                     ESCOLHA AQUI:''')).upper()[0]
      if quest in 'A': # resposta ir para a janela
         print('''
               Você vai para a janela, ela está trancada.
               ao olhar pela janela você percebe estar em uma pequena vila 
               medieaval. Mas a vila parece estar quieta, não há
               pessoas ou animais fora das casas. O sol está se pondo e uma grande lua
               vermelha nasce do horizonte.
               ''')
         quest = str(input('''
                           [A] Dar um soco na janela
                           [B] Ir ver a porta
                           [C] Dar uma cabeçada na janela
                           ESCOLHA AQUI:''')).upper()[0]
         while quest not in 'ABC':
            print('Opcão inválida!')
            quest = str(input('''
                              [A] Dar um soco na janela
                              [B] Ir ver a porta
                              [C] Dar uma cabeçada na janela
                              ESCOLHA AQUI:''')).upper()[0]
         if quest in 'A':
            clear_screen()
            print('SOCO')
         elif quest in 'B':
            clear_screen()
            print('PORTA')
         else:
            clear_screen()
            print('CABEÇA')
            
      else: #resposta ir para a porta
         print('''
               A porta parece estar trancada, porem é muito frágil.
               ''')
         quest = str(input('''
                           [A] Dar um soco na porta
                           [B] Dar um chute na porta
                           ESCOLHA AQUI:''')).upper()[0]
         while quest not in 'AB':
            print('Opção inválida!')
            quest = str(input('''
                              [A] Dar um soco na porta
                              [B] Dar um chute na porta
                              ESCOLHA AQUI:''')).upper()[0]
         if quest in 'A':
            clear_screen()
            print('Soco')
         else:
            clear_screen()
            print('chute')
            
            
            