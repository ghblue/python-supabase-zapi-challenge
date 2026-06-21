from src.config import load_settings
from src.supabase_repository import SupabaseContactRepository
from src.zapi_client import ZApiClient


def main():
    try:
        settings = load_settings()
        zapi_client = ZApiClient(
            instance_id=settings.zapi_instance_id,
            token=settings.zapi_token,
            client_token=settings.zapi_client_token,
        )
        repository = SupabaseContactRepository(
            supabase_url=settings.supabase_url,
            supabase_key=settings.supabase_key,
        )
        contacts = repository.get_active_contacts()
    except ValueError as error:
        print(f"Erro ao carregar configuracoes: {error}")
        return
    except RuntimeError as error:
        print(f"Erro ao buscar contatos: {error}")
        return

    print(f"{len(contacts)} contato(s) ativo(s) encontrado(s).")

    for contact in contacts:
        print(f"Nome: {contact.name} | Telefone: {contact.phone}")

    print("Cliente Z-API configurado com sucesso.")


if __name__ == "__main__":
    main()
