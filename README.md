# Alura Challenge Back-End Python

<p align="center">

<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/rafaelladuarte/challenge_back_end_python_alura?style=plastic">
<img alt="GitHub code size" src="https://img.shields.io/github/languages/code-size/rafaelladuarte/challenge_back_end_python_alura?color=red&style=plastic">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/rafaelladuarte/challenge_back_end_python_alura?style=plastic">

</p>

<p align="center">
<img width='500px'  src='arquivos/image/challenge_backend.jpg'/>
</p>

<p align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

</p>

Repositório dedicado a solução do Alura Challenge Back End, onde foi desenvolvia uma API Rest em Python.

## 🚀 Começando
### 📋 Pré-Requisitos

- Python 3 
- Virtualenv ou Pyenv

### 🔧 Instalação
Criando o ambiente virtual
```sh
python3 -m venv venv
```
Ativando o ambiente virtual
```sh
source venv/bin/activate
```
Instalando as dependências
```sh
pip install --upgrade pip
pip install -r requirements.txt
```
### ✨Execução
Execute o seguinte comando
```sh
uvicorn domain.main:app --reload
```
Você verá a seguinte saída
```sh
INFO:     Will watch for changes in these directories: ['local da aplicação na sua maquina local']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [10892] using watchgod
INFO:     Started server process [10894]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
O servidor está rodando, visite http://127.0.0.1:8000/ no seu navegador de internet


## 📦 Desenvolvimento
### Arquitetura

