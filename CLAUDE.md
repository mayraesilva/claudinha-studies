# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Pacote Python `members-csv-claude-fcc` para leitura e processamento de arquivos CSV com dados de membros. Projeto de estudos baseado no curso Python for Beginners da freeCodeCamp.

## Environment

- Python 3.14.4 via `.venv` local
- Sem dependências externas (usa apenas biblioteca padrão)

## Commands

```powershell
# Ativar ambiente virtual
.venv\Scripts\Activate.ps1

# Instalar o pacote em modo editável (necessário para importar/usar a CLI)
pip install -e .

# Usar a CLI após instalação
members-csv members.csv
```

## Structure

```
src/members_csv_claude_fcc/
    __init__.py   — exporta read_members e get_full_names
    reader.py     — funções principais com type hints e docstrings
    cli.py        — entry point da CLI (members-csv <filepath>)
pyproject.toml    — metadados do pacote e entry point
members.csv       — arquivo de dados de exemplo (1.000 registros)
```

## Package API

- `read_members(filepath)` → `list[dict]` — lê qualquer CSV e retorna todas as linhas
- `get_full_names(filepath)` → `list[str]` — retorna `"first_name last_name"` de cada linha

Ambas aceitam `str` ou `pathlib.Path`. Esperam CSV UTF-8 com linha de cabeçalho.
