# 🌱 Sistema de Monitoramento Agrícola Inteligente (Flask + Abstract Factory + Singleton + XML)

Este projeto simula um sistema de **monitoramento agrícola inteligente** que opera em dois ambientes: **Estufa** e **Campo Aberto**, utilizando os padrões de projeto **Abstract Factory** e **Singleton**, com **persistência de dados em XML**.

## 🧠 Padrões de Projeto Utilizados

- **Abstract Factory**: Criação de sensores e módulos de irrigação diferentes, dependendo do ambiente.
- **Singleton**: Garantia de uma única instância de leitura do XML durante toda a execução da aplicação.
- **XML como banco de dados simulado**: Dados dos sensores e irrigação são carregados a partir de um arquivo XML.

## 📁 Estrutura de Pastas
```projeto_flask/
├── app.py                  # Arquivo principal com rotas Flask
├── fabrica/                # Implementações do Abstract Factory
│   ├── interfaces.py       # Interfaces abstratas dos sensores e módulos
│   ├── estufa.py           # Implementação da fábrica concreta para estufa
│   ├── campo.py            # Implementação da fábrica concreta para campo
│   └── fabrica.py          # (Opcional) Interface abstrata da fábrica
├── singleton/
│   └── conexao_xml.py      # Singleton que lê o XML
├── dados/
│   └── banco.xml           # Arquivo XML com os dados simulados
├── static/
│   └── style.css           # Estilos da página
├── templates/
│   ├── index.html          # Formulário para escolha de ambiente
│   └── resultado.html      # Resultado da simulação
└── README.md               # Este arquivo```


## 🚀 Como Executar o Projeto

### 1. Clone o repositório (ou copie os arquivos)
```bash
git clone <url-do-repositorio>
cd projeto_flask

 2. Crie e ative um ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

3. Instale as dependências
pip install flask

4. Execute a aplicação
python app.py

5. Acesse no navegador
Abra http://127.0.0.1:5000 no seu navegador.

🖥️ Funcionalidade
🔧 Página inicial (/)
Formulário onde o usuário escolhe entre Estufa ou Campo.

📊 Página de resultado (/resultado)
Após envio do formulário, o sistema exibe:

Leitura do sensor de temperatura

Status da irrigação

Com base no ambiente selecionado, as informações são lidas do arquivo banco.xml.

🗂️ Exemplo de banco.xml
xml
Copiar
Editar
<Agricultura>
    <Estufa>
        <SensorTemperatura>28.5°C (com proteção UV)</SensorTemperatura>
        <ModuloIrrigacao>Irrigação ativada via microaspersor</ModuloIrrigacao>
    </Estufa>
    <Campo>
        <SensorTemperatura>31.2°C (sensor resistente à chuva)</SensorTemperatura>
        <ModuloIrrigacao>Irrigação ativada via gotejamento</ModuloIrrigacao>
    </Campo>
</Agricultura>
✅ Requisitos Atendidos
 Interface com Flask

 Abstract Factory para sensores e irrigação

 Singleton para leitura de XML

 Persistência em XML

 Templates HTML e CSS aplicados

 README completo




👨‍💻 Autor
Helder Oliveira Gomes de Souza

Curso: Ciência da Computação

Disciplina: Projeto e Implementação de Software

📝 Licença
Este projeto é apenas para fins educacionais.

