import os


class Color():
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    VERDE_CLARO = '\033[1;92m'
    NEGRITO = '\033[;1m'
    RESET = '\033[0m'


def desliga1():
    os.system("sudo shutdown -h +1")

def desliga5():
    os.system("sudo shutdown -h +5")

def desliga10():
    os.system("sudo shutdown -h +10")

def desliga20():
    os.system("sudo shutdown -h +20")

def desliga60():
    os.system("sudo shutdown -h +60")

def desliga120():
    os.system("sudo shutdown -h +120")


print(Color.AMARELO + "[1] 1 MIN")
print("[5] 5 MIN")
print("[10] 10 MIN")
print("[20] 20 MIN")
print("[60] 1 HORA")
print("[120] 2 HORAS")


try:
    id1 = int(input(Color.VERDE + "PARA AGENDAR O DESLIGAMENTO DO SEU PC, DIGITE O NUMERO CORRESPONDENTE:"))

except ValueError:
    print("digite apenas numeros")

except NameError:
    print("digite apenas numeros")


if id1 == 1:
    desliga1()

if id1 == 5:
    desliga5()

if id1 == 10:
    desliga10()

if id1 == 20:
    desliga20()

if id1 == 60:
    desliga60()

if id1 == 120:
    desliga120()
