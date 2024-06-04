from math import floor
from time import sleep
from os import system

def leiaint(msg, erro='ERRO! Digite um número inteiro válido.'):
    while True:
        try:
            n = int(input(msg))
        except:
            print(erro)
        else:
            return n
        

def conta(soma):
    '''system('cls')'''
    for i, c in enumerate(soma):
        if i == half:
            print(f'+ {c}')
        else:
            print(f'  {c}')
    print(f' ‾{"‾" * len(soma[0])}')


def show():
    print('  ', end='')
    for d in reserva:
        print(d, end='', flush=True)
    print('')
    conta(partext)
    spaces2 = f'{" " * (len(s) - len(s[c*-1:]))}'
    if c == len(s):
        if len(s) < len(partext2[0]):
            print(f'  {spaces2}{s}', end='', flush=True)
        else:
            print(f' {spaces2}{s}', end='', flush=True)
    else:
        if len(s) < len(partext2[0]):
            print(f'  {spaces2}{s[c*-1:]}', end='', flush=True)
        else:
            print(f' {spaces2}{s[c*-1:]}', end='', flush=True)


# Administrando a interação
parcelas = []
valores = []
unidades = []
reserva = []
system('cls')
quant = leiaint('Quantos números você irá somar? ', 'Digite uma quantidade válida!')
half = quant / 2
if float(half):
    half = floor(half)
for c in range(1, quant+1):
    parcelas.append(leiaint(f'{c}º número: ', 'Digite um número válido!'))
# Formatando a interface
parcelas.sort(reverse=True)
partext = parcelas[:]
partext2 = parcelas[:]
for i, c in enumerate(partext):
    partext[i] = str(c)
    partext2[i] = str(c)
for i, c in enumerate(partext):
    if len(c) < len(partext[0]):
        spaces = f'{" " * (len(partext[0]) - len(c))}' 
        partext[i] = (f'{spaces}{c}')
system('cls')
print(' ')
conta(partext)
sleep(1.5)
# Separando ordens numéricas 
for i, c in enumerate(parcelas):
    cont = 1
    loop = 0
    for v in range(1, len(partext2[i])+1):
        try:
            valores[loop].append((c // cont % 10))
        except:
            unidades.append((c // cont % 10))
            valores.append(unidades[:])
            unidades.clear()
        cont *= 10
        loop += 1
# Resultado aparecendo de forma animada
s = str(sum(parcelas))
for c in range(0, len(partext2[0])):
    reserva.append(' ')
for c in range(1, len(s)+1):
    if c > 1:
        sleep(1.5)
    system('cls')
    show()
    try:
        s2 = sum(valores[c-1])
    except:
        s2 = 0
    else:
        if s2 > 9 and c < len(partext2[0]):
            try:
                valores[c].append(s2 // 10)
                reserva[(c+1)*-1] = s2 // 10
                system('cls')
                show()
            except:
                valores[c-1].append(s2 // 10)
                reserva[(c+1)*-1] = s2 // 10
                system('cls')
                show()
