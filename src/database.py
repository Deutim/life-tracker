import sqlite3
from pathlib import Path

CAMINHO_BANCO = Path(__file__).resolve().parent.parent / "life_tracker.db"


def conectar():
    return sqlite3.connect(CAMINHO_BANCO)


def criar_tabelas():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS habitos(
        id INTEGER PRIMARY KEY, 
        nome TEXT NOT NULL
        );
    """)

    conexao.commit()
    conexao.close()

