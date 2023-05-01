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
