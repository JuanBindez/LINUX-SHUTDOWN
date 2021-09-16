#python3 shutdown.py

import os

#................... FUNÇÕES....................

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

# ................FIM DAS FUNÇÕES.................



#................INICIO DO PROGRAMA...............

print("[1] 1 MIN")
print("[5] 5 MIN")
print("[10] 10 MIN")
print("[20] 20 MIN")
print("[60] 1 HORA")
print("[120] 2 HORAS")

id1 = int(input("PARA AGENDAR O DESLIGAMENTO DO SEU PC, DIGITE O NUMERO CORRESPONDENTE:"))


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

# ................FIM DO PROGRAMA.................

