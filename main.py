import logging

from src.config import load_settings
from src.message_service import MessageService
from src.supabase_repository import SupabaseContactRepository
from src.zapi_client import ZApiClient


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:
        settings = load_settings()
        repository = SupabaseContactRepository(
            supabase_url=settings.supabase_url,
            supabase_key=settings.supabase_key,
        )
        zapi_client = ZApiClient(
            instance_id=settings.zapi_instance_id,
            token=settings.zapi_token,
            client_token=settings.zapi_client_token,
        )
        message_service = MessageService(
            contact_repository=repository,
            zapi_client=zapi_client,
        )
        summary = message_service.send_messages_to_active_contacts()
    except ValueError as error:
        print(f"Erro ao carregar configuracoes: {error}")
        return
    except RuntimeError as error:
        print(f"Erro ao executar fluxo de mensagens: {error}")
        return

    print(f"Total de contatos processados: {summary['total_contacts']}")
    print(f"Mensagens enviadas com sucesso: {summary['sent_count']}")
    print(f"Falhas: {summary['failed_count']}")


if __name__ == "__main__":
    main()
