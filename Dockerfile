# Use a imagem oficial do Python como imagem base
FROM python:3.9-slim

# Atualize o sistema e instale o wget
RUN apt-get update && apt-get install -y wget
RUN pip install requests

# Defina o diretório de trabalho
WORKDIR /app

# Baixe o arquivo da URL fornecida usando wget e salve como Directories_All.wordlist
RUN wget -O Directories_All.wordlist https://raw.githubusercontent.com/emadshanab/WordLists-20111129/master/Directories_All.wordlist

# Copie todos os arquivos do diretório de trabalho atual para o diretório /app no container
COPY . /app 

# Execute o script Python
CMD ["python3", "Hellboy.py"]

