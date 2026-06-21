from src.config import load_settings


def main():
    try:
        load_settings()
        print("Configuracoes carregadas com sucesso.")
    except ValueError as error:
        print(f"Erro ao carregar configuracoes: {error}")


if __name__ == "__main__":
    main()
