import requests
import os

class Hellboy:

    @staticmethod
    def logo():
        """
        Função para imprimir o logotipo do programa.
        """
        print("""
  , ,  _,,   ,   __   _, ,  ,
  |_|,/_,|   |  '|_) / \,\_/
 '| |'\_'|__'|___|_)'\_/, /`
  ' `   `  '   '     ' (_/
  """)

    @staticmethod
    def carregar_dirs(nome_arquivo):
        """
        Função para carregar uma lista de diretórios a partir de um arquivo.
        
        Args:
            nome_arquivo (str): O nome do arquivo que contém os diretórios.
        
        Returns:
            list: Uma lista de diretórios carregados do arquivo.
        """
        try:
            with open(nome_arquivo, 'r') as arquivo:
                return arquivo.read().splitlines()  # Lê o arquivo e retorna uma lista de linhas
        except FileNotFoundError:
            print("O arquivo de diretórios não foi encontrado.")
            return []  # Retorna uma lista vazia se o arquivo não for encontrado

    @staticmethod
    def url_validador(u_rl):
        """
        Função para validar diretórios em uma URL fornecida.
        
        Args:
            u_rl (str): A URL base fornecida pelo usuário.
        """
        nome_arquivo = "a.txt"
        dirs = Hellboy.carregar_dirs(nome_arquivo)
        if not dirs:
            return  # Encerra a função se não foi possível carregar os diretórios

        try:
            r = requests.get(u_rl)  # Tenta fazer uma requisição GET para a URL fornecida
            status_code = r.status_code  # Obtém o código de status da resposta
        except:
            print(f"Erro ao tentar acessar a URL:")
            return
        if status_code == 200:  # Verifica se a requisição inicial foi bem-sucedida
            with open("validos.txt", 'w') as arquivo:  # Abre o arquivo para escrever URLs válidas
                for dir_name in dirs:
                    jun_cao = u_rl + "/" + dir_name  # Concatena a URL base com o diretório
                    try:
                        response = requests.head(jun_cao)  # Tenta fazer uma requisição HEAD para o URL completo
                        if response.status_code == 200:
                            arquivo.write(jun_cao + "\n")  # Escreve a URL válida no arquivo
                            print(jun_cao + " - Válido")
                        else:
                            print(jun_cao + " - Inválido (Código de status: " + str(response.status_code) + ")")
                    except requests.exceptions.RequestException as e:
                        print(jun_cao + " - Erro ao tentar acessar: " + str(e))
        else:
            print("URL inválida.")  # Imprime uma mensagem se a URL inicial não for válida

if __name__ == "__main__":
    os.system("clear")  # Limpa a tela do terminal
    Hellboy.logo()  # Chama a função para imprimir o logotipo
    u_rl = input("Url: ")
    Hellboy.url_validador(u_rl)  # Chama a função principal
### https://www.xvideos.com/