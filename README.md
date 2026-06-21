# Python Supabase Z-API Challenge

Projeto em Python que busca até 3 contatos ativos no Supabase e envia uma mensagem personalizada via Z-API.

## Tecnologias usadas

- Python
- Supabase
- Z-API
- python-dotenv
- requests

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/config.py`: carrega e valida variáveis de ambiente.
- `src/supabase_repository.py`: busca contatos ativos no Supabase.
- `src/zapi_client.py`: envia mensagens de texto pela Z-API.
- `src/message_service.py`: coordena busca, montagem e envio das mensagens.
- `docs/`: documentação das etapas do desenvolvimento.

## Setup da tabela no Supabase

```sql
create table contacts (
id uuid primary key default gen_random_uuid(),
name text not null,
phone text not null,
is_active boolean not null default true,
created_at timestamp with time zone default now()
);
```

Exemplo de inserts:

```sql
insert into contacts (name, phone) values
('Gabriel', '5553999999999'),
('Maria', '5553988888888'),
('João', '5553977777777');
```

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto usando o `.env.example` como base:

```text
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=
```

Não versione o arquivo `.env`.

## Instalação

Linux, WSL ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Como rodar

```bash
python main.py
```

## Observações

- O script envia mensagens para no máximo 3 contatos ativos.
- A mensagem enviada segue exatamente o formato: `"Olá, <nome_contato> tudo bem com você?"`
- Telefones devem estar no formato aceito pela Z-API, com DDI + DDD + número.
- O arquivo `.env` não deve ser versionado.
