# Desafio MBA Engenharia de Software com IA - Full Cycle

## Como executar

### Configuração

Crie uma cópia do arquivo `.env.example` com o nome `.env`

Altere as seguinte chaves com as keys da OpenIA e Gemini:
- OPENAI_API_KEY
- GOOGLE_API_KEY

Sinta-se a vontate para alterar as outras chaves

Defina o provider que será utilizado, entre 'openai' ou 'google'
```
ACTIVE_EMBEDDING_PROVIDER='openai'
ACTIVE_CHAT_PROVIDER='openai'
```

### Instalando as dependências

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Iniciando o projeto

Iniciar o docker container
```bash
docker compose up -d
```

### Rodando os scripts

Carregando o banco de dados
```bash
python src/ingest.py
```

Conversando com o chat
```bash
python src/chat.py
```