Projeto de Infraestrutura de Comunicação
Professor: Eduardo Nascimento de Arruda

📡 WifiFound — Scanner de Dispositivos Wi-Fi

Aplicações desenvolvidas com Django(backend) e html e css(frontend) para realizar varreduras em redes Wi-Fi e exibir os dispositivos conectados.


Participantes:
Fábio Reis 
Victor Gabriel
Deyvison Gabriel
Gustavo Cassemiro
Caio Catão


🚀 Funcionalidades

Varredura da rede local usando nmap ou scapy

Exibição dos dispositivos encontrados (IP, MAC, Hostname)

Frontend React consumindo a API Django

Projeto simples e sem banco de dados

🛠️ 1. Pré-requisitos
✔️ Você precisa ter instalado:

Python 3.10+

pip

virtualenv (opcional, mas recomendado)

Node.js 16+ e NPM

nmap instalado no sistema

Windows: https://nmap.org/download.html

Linux: sudo apt install nmap

Fazer o git clone : https://github.com/FIGU3IR4/WifiFound.git


🐍 2. Configuração do Backend (Django)
2.1. Criar e ativar o ambiente virtual
python -m venv venv


Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

2.2. Instalar dependências
pip install -r requirements.txt


Se você não tiver o arquivo, instale manualmente:

pip install django djangorestframework python-nmap

2.3. Aplicar migrações
python manage.py migrate


Se aparecer:

No migrations to apply.


Significa que o Django já criou todas as tabelas necessárias e nada mais precisa ser feito.

2.4. Rodar o servidor Django
python manage.py runserver


A API ficará disponível em:

📌 http://127.0.0.1:8000/

📁 Estrutura do Projeto (WifiFound)
WifiFound/
│
├── cli/
│   └── scan_cli.py
│
├── scanner/
│   ├── __pycache__/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── apps.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── setup/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt