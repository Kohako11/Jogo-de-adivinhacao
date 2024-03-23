import random
import os
from colorama import Fore, Style

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

acertos = 0
erros = 0

while True: 
    número = random.randint(1, 100)
    print("""
-------------------------------------------          
          ADVINHE O NÚMERO
-------------------------------------------
Olá, esse jogo é sobre advinhação.
Resumindo te daremos um número de 1 a 100
Você terá 5 tentativas
-------------------------------------------
""")
    for tentativa in range(5):
        palpite = int(input(f'Tentativa {tentativa + 1} ! Digite seu palpite:'))
        if palpite < número:
            print(Fore.RED + f'O {palpite} é menor que o número!'+ Style.RESET_ALL)
        elif palpite > número:
            print(Fore.RED + f'O {palpite} é maior que o número!'+ Style.RESET_ALL)
        else:
            print(Fore.GREEN + 'Você acertou o número misterioso!!!'+ Style.RESET_ALL)
            print('Parábens')
            acertos =+ 1
            break
    else:
        print(Fore.YELLOW + f'O número era {número}, as suas tentativas acabaram'+ Style.RESET_ALL)
        erros =+ 1
    jogar_de_novo = input('Deseja jogar de novo? (s/n):')
    if jogar_de_novo == 's':
        print('Ok, vamos voltar para o inicio')
        limpar_terminal()
    else:
        print(Fore.CYAN + f'Essa foi a sua pontuação!  acertos:{acertos} e erros:{erros} '+ Style.RESET_ALL)
        print('Vamos encerrar o programa!!!')
        break
