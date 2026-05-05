import time
from machine import Pin

# Função de limpeza do terminal
def clean():
  print("\033[H\033[2J", end="")
clean()

# Função de Novo Ensaio
def novoensaio():
  clean()
  print("--- Novo Ensaio ---\n")

  print("-> Identificação Gerais do Ensaio")
  title_ensaio = ("Título do Ensaio: ")
  autors = input("Autor(es): " )
  descript_ensaio = input("Descreva brevemente este ensaio: ")
  
  t = time.localtime()                                      # Obtém a data e hora atual
  data_hora = "{:02d}/{:02d}/{}, às {:02d}:{:02d}:{:02d}".format(t[2], t[1], t[0], t[3], t[4], t[5])   # Dexa a data e hora formatadas
  print("Data e hora:", data_hora)

  print("\n-> Descrição do Concreto")
  aglom = input("Aglomerante: ")
  reag = input("Reagente: ")
  miudo = input ("Agregado Miúdo: ")
  graudo = input ("Agregado Graúdo: ")
  comp = input ("Composição/Adição: ")
  adt = input ("Aditivo: ")
  arm = input ("Tipo de Armadura: ")
  print("---------------------------------")
  time.sleep(0.5)

  confirm_defin = input("Confirma que as informações estão corretas?\n[Sim]     [Não]").lower().strip()

  if confirm_defin == "sim":
    print("Procigamos para o ensaio...")
  return
  novoensaio()


# Função para quando o ensaio estiver em progresso
def ensaiando():
  clean()

  t = time.localtime()   # Obtém a data e hora atual
  data_horap1 = "{:02d}/{:02d}/{}, às {:02d}:{:02d}:{:02d}".format(t[2], t[1], t[0], t[3], t[4], t[5])   # Dexa a data e hora formatadas
  print("Início da solidificação:", data_horap1)
  while True:
    print("\nSensores leem a humidade e temperatura internas e externas a cada 1 segundo\nE essas informações são mostradas no terminal")
    print("Após a solidificação do corpo de prova e início do endurecimento, clique no botão amarelo")
    time.sleep(1)
    button_run_pin = Pin(14, Pin.IN, Pin.PULL_UP)
    if button_run_pin.value() == 0:
      clean()
      print("botão precionado. Iniciando etpa de endurecimento às", data_horap1)
      break
  return
  ensaiando()