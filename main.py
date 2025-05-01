
from cryptography.fernet import Fernet
from colorama import Fore, Style, init
import os

init(autoreset=True)

CHAVE_ARQUIVO = "chave.key"

def gerar_chave():
    chave = Fernet.generate_key()
    with open(CHAVE_ARQUIVO, "wb") as f:
        f.write(chave)
    print(Fore.GREEN + "Chave gerada e salva em 'chave.key'")

def carregar_chave():
    if not os.path.exists(CHAVE_ARQUIVO):
        print(Fore.YELLOW + "Chave não encontrada. Gerando nova...")
        gerar_chave()
    with open(CHAVE_ARQUIVO, "rb") as f:
        return f.read()

def criptografar(mensagem):
    chave = carregar_chave()
    fernet = Fernet(chave)
    cifrada = fernet.encrypt(mensagem.encode())
    print(Fore.CYAN + "Mensagem criptografada:\n" + cifrada.decode())

def descriptografar(mensagem_cifrada):
    try:
        chave = carregar_chave()
        fernet = Fernet(chave)
        decifrada = fernet.decrypt(mensagem_cifrada.encode())
        print(Fore.CYAN + "Mensagem decifrada:\n" + decifrada.decode())
    except Exception as e:
        print(Fore.RED + "Erro ao descriptografar. Verifique a chave e a mensagem.")

def menu():
    while True:
        print(Style.BRIGHT + Fore.BLUE + "\n--- Menu de Criptografia ---")
        print("1. Gerar nova chave")
        print("2. Criptografar mensagem")
        print("3. Descriptografar mensagem")
        print("4. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            gerar_chave()
        elif escolha == "2":
            mensagem = input("Digite a mensagem a ser criptografada: ")
            criptografar(mensagem)
        elif escolha == "3":
            mensagem = input("Digite a mensagem criptografada: ")
            descriptografar(mensagem)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print(Fore.YELLOW + "Opção inválida.")

if __name__ == "__main__":
    menu()
