1 import validators
  2 import requests
  3 import os
  4
  5
  6 def logo():
  7     print("""
  8
  9  , ,  _,,   ,   __   _, ,  ,
 10  |_|,/_,|   |  '|_) / \,\_/                                                          11 '| |'\_'|__'|___|_)'\_/, /`
 12  ' `   `  '   '     ' (_/
 13
 14  """)
 15
 16 def carregar_dirs(nome_arquivo):
 17     try:
 18         with open(nome_arquivo, 'r') as arquivo:
 19             return arquivo.read().splitlines()                                       20     except FileNotFoundError:
 21         print("O arquivo de diretórios não foi encontrado.")
 22         return []
 23
 24 def Hellboy():                                                                       25     nome_arquivo = "wordlist.txt"                                                    26     dirs = carregar_dirs(nome_arquivo)
 27     if not dirs:
 28         return  # Encerra a função se não foi possível carregar os diretórios
 29                                                                                      30     U_rl = input("Url: ")
 31     if validators.url(U_rl):                                                         32         print("URL válida.")
 33         with open("validos.txt", 'w') as arquivo:
 34             for dir_name in dirs:
 35                 Jun = U_rl + "/" + dir_name
 36                 try:
 37                     response = requests.head(Jun)
 38                     if response.status_code == 200:                                  39                         arquivo.write(Jun + "\n")  # Escreve a URL válida no arquivo
 40                         print(Jun + " - Válido")
 41                     else:
 42                         print(Jun + " - Inválido (Código de status: " + str(response    .status_code) + ")")
 43                 except requests.exceptions.RequestException as e:
 44                     print(Jun + " - Erro ao tentar acessar: " + str(e))
 45     else:
 46         print("URL inválida.")
 47
 48 os.system("clear")
 49 logo()
 50 Hellboy()
 51