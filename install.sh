#!/bin/bash

# Instala as dependências do Python
sudo apt-get update
sudo apt-get install -y python3-pip
sudo pip3 install -r requirements.txt

# Faz o download do arquivo Python
wget https://raw.githubusercontent.com/leandoo/rsnxp/main/script.py?token=GHSAT0AAAAAACB2A3RCSDNHUI5LDDTOJFRUZCPFOZA

# Executa o arquivo Python
python3 script.py

# Prompt para inserção da chave

echo "Insira a chave de ativação:"

read chave

# Validação da chave

if [ "$chave" != "leandro" ]

then

    echo "Chave inválida. Instalação abortada."

    exit 1

fi

# Verificação da chave
chave_correta = "leandro"
chave_inserida = input("Insira a chave de ativação: ")
if chave_inserida != chave_correta:
    print("Chave inválida. Encerrando o script.")
    sys.exit(1)
