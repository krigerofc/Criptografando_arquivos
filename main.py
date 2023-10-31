from cryptography.fernet import Fernet

def criptografar(arquivo_nome:str):
    with open(arquivo_nome, 'rb') as file:
        arquivo_original = file.read()

    criptografia = fernet.encrypt(arquivo_original)

    with open(arquivo_nome, 'wb') as file:
        file.write(criptografia)


def remover_criptografia(arquivo_nome:str):
    with open(arquivo_nome, 'rb') as file:
        arquivo_criptografado = file.read()

    original = fernet.decrypt(arquivo_criptografado)

    with open(arquivo_nome, 'wb') as file:
        file.write(original)


try:
    with open('chave.key', 'rb') as file:
        key = file.read()
except:
    key = Fernet.generate_key()
    with open('chave.key', 'wb') as file:
        file.write(key)

fernet = Fernet(key)

criptografar('BANCO.txt')

