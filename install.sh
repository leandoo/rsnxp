#!/bin/bash

# Instala as dependências necessárias
sudo apt-get update
sudo apt-get install -y python3-pip git

# Baixa o arquivo e suas dependências do GitHub
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
pip3 install -r requirements.txt

# Executa o arquivo .py
python3 seu_arquivo.py
