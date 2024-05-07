import validators
import requests

def carregar_dirs(nome_arquivo): 
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read().splitlines()
    except FileNotFoundError:
        print("O arquivo de diretórios não foi encontrado.")
        return []

def Hellboy():
    nome_arquivo = "/home/anonymous/small.txt"
    dirs = carregar_dirs(nome_arquivo)
    if not dirs:
        return  # Encerra a função se não foi possível carregar os diretórios

    U_rl = input("Url: ")
    if validators.url(U_rl):
        print("URL válida.") 
        with open("validos.txt", 'w') as arquivo:
            for dir_name in dirs:
                Jun = U_rl + "/" + dir_name
                try:
                    response = requests.head(Jun)
                    if response.status_code == 200:
                        arquivo.write(Jun + "\n")  # Escreve a URL válida no arquivo
                        print(Jun + " - Válido")
                    else:
                        print(Jun + " - Inválido (Código de status: " + str(response.status_code) + ")")
                except requests.exceptions.RequestException as e:
                    print(Jun + " - Erro ao tentar acessar: " + str(e))
    else:
        print("URL inválida.")

Hellboy()

