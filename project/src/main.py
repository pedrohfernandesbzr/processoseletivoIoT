import os
import time
import astf
from machine import Pin

# Inicialização
print("\n\nAssistente de Ensaios Técnicos (AST1000) está iniciando...")
input("Pressione enter para continuar...")


# Esqueleto do sistema
while True:
    astf.clean()
    print("--- AST CORPO DE PROVA DE CONCRETO ---\n")
    print("[1] - Iniciar novo e saio")
    opcao = input("Escolha uma opção válida.")

    # Esqueleto da opção NOVO ENSAIO
    if opcao == "1":
        astf.novoensaio()
        print("Quando o concreto estiver na forma, pronto para a secagem, aperte o botão verde")
    else:
        continue

    while True:
        button_run_pin = Pin(12, Pin.IN, Pin.PULL_UP)
        if button_run_pin.value() == 0:
            astf.clean()
            print("botão precionado")
            astf.ensaiando()
            input("Próximas etapas...")
            break
