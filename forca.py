import os
from random import shuffle

def linha(msg):
    print(' ' * 30)
    print(f'{msg:^30}')
    print(' ' * 30)


def invalido(msg):
    os.system('cls')
    print('Escolha uma opção válida!')
    

forca = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

while True:
    os.system('cls')
    linha('JOGO DA FORCA!')
    print('Escolha a modlidade de jogo:')
    try:
        opc = int(input('''1 - Palavra definida pelo jogador
2 - Palavra aleatória

Sua opção: '''))
    except:
        invalido('Escolha uma opção válida!')
    else:
        if opc > 2 or opc < 1:
            invalido('Escolha uma opção válida!')
        else:
            break
while True:
    os.system('cls')
    try:
        rounds = int(input('Quantas rodadas? (máximo de 3): '))
    except:
        invalido('Digite uma opção válida!')
    else:
        if rounds > 3 or rounds < 1:
            invalido('Digite uma opção válida!')
        else:
            break
words = []
dic = {'Palavra': '', 'Dica': ''}
if opc == 1:
    for c in range(0, rounds):
        os.system('cls')
        dic['Palavra'] = input(f'Palavra {c + 1}: ').strip().upper() 
        dic['Dica'] = input(f'Dica da palavra {c + 1}: ')
        words.append(dic.copy())
        dic.clear()
else:
    words = [{'Palavra': 'SAPATO', 'Dica': 'Vestuário]'},
             {'Palavra': 'ARGENTINA', 'Dica': 'País'}, {'Palavra': 'PROFESSOR', 'Dica': 'Profissão'}]
    shuffle(words)
vidas = 0
for c in range(0, rounds):
    if vidas == 6:
        break
    palavra = words[c]['Palavra']
    dica = words[c]['Dica']
    falhas = []
    acertos = []
    while True:
        contador = 0
        os.system('cls')
        linha(f'RODADA {c + 1}')
        print(f'Dica: {dica}')
        print(f'Letras erradas: ', end='')
        for v in falhas:
            print(f'{v}  ', end='')
        print(forca[vidas], end='')
        for a, b in enumerate(palavra):
            if palavra[a] in acertos:
                print(palavra[a], end='')
            else:
                print('_ ', end='')
        if vidas == 6:
            print('\nGAME OVER!')
            print(f'A palavra era {palavra}')
            break
        for a in palavra:
            if a in acertos:
                contador += 1
        if contador == len(palavra):
            print('\nParabéns!')
            if c == rounds - 1:
                print('Você venceu o jogo!')
            else:
                os.system('pause')
            break
        letra = input('\nSua letra: ').strip().upper()
        if letra not in palavra:
            vidas += 1
            falhas.append(letra)
        else:
            acertos.append(letra)
