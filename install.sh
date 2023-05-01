#!/bin/bash

# Prompt para inserção da chave de ativação
echo "Insira a chave de ativação:"
read chave

# Validação da chave
if [ "$chave" != "leandro" ]; then
    echo "Chave inválida. Instalação abortada."
    exit 1
fi

# Função de instalação
function install() {
    # Instala as dependências do Python
    sudo apt-get update
    sudo apt-get install -y python3-pip

    # Define uma variável com o conteúdo do requirements.txt
    REQUIREMENTS=$(cat <<EOF
    hmac
    json
    hashlib
    time
    requests
    websock
    EOF
    )

    # Cria um arquivo temporário requirements.txt com o conteúdo da variável
    REQUIREMENTS_FILE=$(mktemp -t requirements.XXXXXX)
    echo "${REQUIREMENTS}" > "${REQUIREMENTS_FILE}"

    # Instala os pacotes listados no arquivo requirements.txt
    pip install -r "${REQUIREMENTS_FILE}"

    # Resto do seu script de instalação ...

    # Faz o download do arquivo Python
    wget https://raw.githubusercontent.com/leandoo/rsnxp/main/script.py

    # Executa o arquivo Python
    python3 script.py

    # Tornar o arquivo executável
    chmod +x install.sh

    # Executa o arquivo de instalação e execução
    ./install.sh
}

# Chama a função de instalação
install
