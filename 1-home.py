import os
import time
import colorama
from colorama import Fore,Style

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def item_1():
  pt_tk_kaneki = "1 - Camiseta Boxy/Oversized - Kaneki"
  pt_tk_kaneki_venda = """
  Camiseta Boxy/Oversized - Kaneki
  Preço normal: R$ 209,99 BRL
  EM ATÉ 12X
  Tamanho: [P] [M] [G] [GG]
  """
  print(pt_tk_kaneki)
  print(pt_tk_kaneki_venda)

def item_2():
  pt_tk_suzuyo = "2 - Camiseta Boxy/Oversized - Juuzou Suzuya"
  pt_tk_suzuyo_venda = """
  Camiseta Boxy/Oversized - Juuzou Suzuya
  Preço normal: R$ 209,99 BRL
  EM ATÉ 12X
  Tamanho: [P] [M] [G] [GG]
  """
  print(pt_tk_suzuyo)
  print(pt_tk_suzuyo_venda)

def item_3():
  pt_tk_touka = "3 - Camiseta Boxy/Oversized - Touka"
  pt_tk_touka_venda = """
  Camiseta Boxy/Oversized - Touka
  Preço normal: R$ 209,99 BRL
  EM ATÉ 12X
  Tamanho: [P] [M] [G] [GG]
  """
  print(pt_tk_touka)
  print(pt_tk_touka_venda)


def verfy_pix():
    qr_code = """   
                    ⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
                    ⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣇⣿⣿⣀⡀⢸⣿⣿⡇⢀⣀⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡀
                    ⡀⢸⣿⡀⣤⣤⣤⣤⣤⡀⣿⡇⢠⣤⣿⣿⣼⣿⣧⣤⣤⣿⣧⣼⣿⠇⣿⣿⡀⣤⣤⣤⣤⡄⢸⣿⡇⡀
                    ⡀⢸⣿⡀⣿⣿⣿⣿⣿⡀⣿⡇⠘⠿⣿⣿⣿⣶⡿⢿⣿⣿⡿⠿⡀⡀⣿⣿⡀⣿⣿⣿⣿⡇⢸⣿⡇⡀
                    ⡀⢸⣿⡀⣿⣿⣿⣿⣿⡀⣿⡇⡀⡀⠛⠛⢻⣿⣿⣿⠛⣿⡇⡀⡀⡀⣿⣿⡀⣿⣿⣿⣿⡇⢸⣿⡇⡀
                    ⡀⢸⣿⡀⠉⠉⠉⠉⠉⡀⣿⡇⢸⣿⡆⣿⣿⣿⡏⠉⡀⠉⠁⡀⡀⡀⣿⣿⡀⠉⠉⠉⠉⠁⢸⣿⡇⡀
                    ⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣇⣿⣿⡀⣿⣿⡀⣿⡇⢸⣿⠇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡀
                    ⡀⢠⣤⡀⣤⣤⡀⡀⡀⡀⣤⣤⣤⡀⠿⣿⣿⡀⣿⣿⡀⠿⣧⣤⡀⡀⡀⢀⣤⡄⡀⡀⣤⡄⢠⣤⡄⡀
                    ⡀⠘⠿⣶⣿⢿⣶⣶⣶⡀⠿⠿⠟⡀⣶⣿⣿⡀⣿⣿⡀⡀⣿⣿⣶⣶⣶⣾⣿⡇⢰⣶⠿⣷⣾⣿⡇⡀
                    ⡀⢸⣿⠛⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⡇⡀
                    ⡀⠈⠉⡀⣿⣿⣿⣿⣿⣿⠉⣿⣿⣿⡇⣿⣿⣿⡏⠉⠉⣿⡏⠉⡀⡀⠈⠉⠉⠉⢹⣿⠉⠁⡀⠉⡀⡀
                    ⡀⢸⣿⣿⣿⣿⣿⣿⣿⡀⣿⣇⣀⡀⣿⣿⣀⡀⡀⢀⣀⣿⣇⣸⣿⣿⣿⣿⣀⡀⡀⡀⡀⣀⣸⣿⡇⡀
                    ⡀⢠⣤⣿⣿⠿⠿⠿⠿⡀⣤⣿⣿⡀⠿⣿⣿⣤⡄⠸⠿⡀⣿⣿⠿⠇⠿⠿⠿⠇⢠⣤⣤⡿⢿⣿⡇⡀
                    ⡀⠘⠛⠛⠋⡀⡀⡀⢰⣶⠛⣿⣿⡀⡀⠛⠛⠛⠃⡀⡀⡀⣿⣿⡀⡀⣴⣶⣶⣶⣾⣿⠛⠃⠘⠛⠃⡀
                    ⡀⢸⣿⣿⣷⡀⡀⣿⣿⠉⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⡀⡀⠉⢹⣿⣿⣿⣿⣿⣿⣿⠉⡀⣿⣿⡀⡀⡀
                    ⡀⢀⣉⣉⣁⣀⣀⣉⣁⣀⣉⡉⢹⣿⣿⣿⣿⠉⣿⣿⣿⡀⡀⢸⣿⡏⢉⣉⠉⣿⣿⡀⡀⠈⢹⣿⡇⡀
                    ⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⡿⢀⣤⣿⣿⡀⣤⣤⣼⣿⡇⢿⣿⡀⣿⣿⡀⡀⡀⠸⣿⠇⡀
                    ⡀⢸⣿⡀⣤⣤⣤⣤⣤⡀⣿⡇⡀⡀⡀⣤⣼⠿⣿⣿⡀⠿⣿⣿⣿⣧⣤⣤⣤⣿⣿⡀⡀⣤⣤⡀⡀⡀
                    ⡀⢸⣿⡀⣿⣿⣿⣿⣿⡀⣿⡇⡀⡀⣶⣿⣿⡀⠛⠛⡀⣶⣿⣿⠛⣿⣿⠛⠛⣿⣿⡀⣶⣿⣿⡀⡀⡀
                    ⡀⢸⣿⡀⣿⣿⣿⣿⣿⡀⣿⡇⢸⣿⡏⠉⢹⣿⡇⡀⡀⣿⣿⣿⡀⠉⠉⢰⣿⣿⣿⣿⠉⣿⣿⣿⡇⡀
                    ⡀⢸⣿⣀⣀⣉⣉⣉⣀⣀⣿⡇⢀⣉⣿⣿⣿⣿⣿⣿⡀⠉⠉⢹⣿⣿⣿⠸⣿⣿⣿⣉⡀⡀⠉⣉⡀⡀
                    ⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⡀⡀⡀⠸⣿⠇⡀⡀⡀⡀⢸⣿⡀⡀⠸⣿⠇⡀
                    ⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀⡀
    """
    print(qr_code)
    print("Gerador: 024025025025025025020520520")
    print("Esperando ...")
    time.sleep(10)
    clear()
    status = "Sucesso"
    print(status)


def verfy_cart():
    clear()
    name = input("Nome Completo: ")
    num = input("Numero do Cartão: ")
    valid = input("Validade: ")
    CC = input("CC: ")
    print("Validando ...")
    time.sleep(10)
    clear()
    status = "Sucesso"
    print(status)


met = """   
┌──────────────────┐
│ [PIX]   [CARTÃO] │
└──────────────────┘

"""

list = """
1 - Camiseta Boxy/Oversized - Kaneki
2 - Camiseta Boxy/Oversized - Juuzou Suzuya
3 - Camiseta Boxy/Oversized - Touka
"""
tamanho = """
Tamanho: [P] [M] [G] [GG]
"""
def carrinho():
    global nome
    global tam
    print("\n")
    print("Colocar no Carrinho")
    print("Sim / Não")
    escolhas = input("Digita: ").lower()
    if escolhas in ["sim","s"]:
        clear()
        print("Qual Tamanho") 
        print(tamanho) 
        tam = input("Digita: ").upper()
        clear()
        print(list)
        prut = input("Qual Protudo: ")
        if prut == "1":
            clear()
            nome = "1 - Camiseta Boxy/Oversized - Kaneki"
            print(nome)
            print(tam)
            print("Confirma")
            print("Sim/Não")
            con = input("Digita: ")
            if con in ["sim","s"]:
                clear()
                carrinho_verfy()
            elif con in ["n","Não","Nao"]:
                input("ok")
        elif prut == "2":
            clear()
            nome = "2 - Camiseta Boxy/Oversized - Juuzou Suzuya"
            print(nome)
            print(tam)
            print("Confirma")
            print("Sim/Não")
            con = input("Digita: ")
            if con in ["sim","s"]:
                clear()
                carrinho_verfy()
            elif con in ["n","Não","Nao"]:
                input("ok")
        elif prut == "3":
            clear()
            nome = "3 - Camiseta Boxy/Oversized - Touka"
            print(nome)
            print(tam)
            print("Confirma")
            print("Sim/Não")
            con = input("Digita: ")
            if con in ["1","sim","s"]:
                clear()
                carrinho_verfy()
            elif con in ["2","n","Não","Nao"]:
                input("ok")
    elif escolhas in ["n","Não","Nao"]:
        input("ok")


def carrinho_verfy():
    try:
        print(nome)
        print(f"Tamanho: [{tam}]")
        print("R$ 209,99 BRL")
        print("\n")
        print("Forma de Pagamento")
        print(met)
        escolhas_met = input("Digita: ")
        if escolhas_met in ["pix","PIX"]:
            clear()
            verfy_pix()
        elif escolhas_met in  ["cartão","CARTÃO"]:
            verfy_cart()
    except Exception as e:
        input(e)

logo =  """ 
  ██████   ██░ ██  ▄▄▄     ▓█████▄  ▒█████   █     █░      ▄▄▄▄     ██▓    ▄▄▄       ▄████▄  ██ ▄█▀
▒██    ▒ ▒▓██░ ██ ▒████▄   ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░     ▓█████▄  ▓██▒   ▒████▄    ▒██▀ ▀█  ██▄█▒ 
░ ▓██▄   ░▒██▀▀██ ▒██  ▀█▄ ░██   █▌▒██░  ██▒▒█░ █ ░█      ▒██▒ ▄██ ▒██░   ▒██  ▀█▄  ▒▓█    ▄▓███▄░ 
  ▒   ██▒ ░▓█ ░██ ░██▄▄▄▄██░▓█▄   ▌▒██   ██░░█░ █ ░█      ▒██░█▀   ▒██░   ░██▄▄▄▄██▒▒▓▓▄ ▄██▓██ █▄ 
▒██████▒▒ ░▓█▒░██▓▒▓█   ▓██░▒████▓ ░ ████▓▒░░░██▒██▓     ▒░▓█  ▀█▓▒░██████▒▓█   ▓██░▒ ▓███▀ ▒██▒ █▄
▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░▒▒   ▓▒█ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒      ░░▒▓███▀▒░░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ▒ ▒▒ ▓▒
░ ░▒  ░    ▒ ░▒░ ░░ ░   ▒▒  ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░      ░▒░▒   ░ ░░ ░ ▒  ░ ░   ▒▒    ░  ▒  ░ ░▒ ▒░
░  ░  ░    ░  ░░ ░  ░   ▒   ░ ░  ░ ░ ░ ░ ▒    ░   ░        ░    ░    ░ ░    ░   ▒   ░       ░ ░░ ░ 
      ░    ░  ░  ░      ░     ░        ░ ░      ░        ░ ░      ░    ░        ░   ░ ░     ░  ░   
"""
Menu = f""" 
┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│MENU  Tokyo Ghoul Collection                                                          Shadow Black   │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘

"""

Tokyo = """  Tokyo Ghoul Collection  

1 - Camiseta Boxy/Oversized - Kaneki      2 - Camiseta Boxy/Oversized - Juuzou Suzuya      3 - Camiseta Boxy/Oversized - Touka

""" 

while True:
  clear()
  print(logo)
  print(Menu)
  print(Tokyo)
  buscador = input("Digita: ")
  if buscador == "1":
      clear()
      item_1()
      carrinho()
  elif buscador == "2":
      clear()
      item_2()
      carrinho()
  elif buscador == "3":
      clear()
      item_3()
      carrinho()
  input("...")
  clear()