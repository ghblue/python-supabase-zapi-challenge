import logging


logger = logging.getLogger(__name__)


class MessageService:
    def __init__(self, contact_repository, zapi_client):
        self._contact_repository = contact_repository
        self._zapi_client = zapi_client

    def send_messages_to_active_contacts(self) -> dict[str, int]:
        contacts = self._contact_repository.get_active_contacts(limit=3)

        if not contacts:
            logger.info("Nenhum contato ativo encontrado para envio.")
            return {
                "total_contacts": 0,
                "sent_count": 0,
                "failed_count": 0,
            }

        sent_count = 0
        failed_count = 0

        for contact in contacts:
            name = contact.name.strip() if contact.name else ""
            phone = contact.phone.strip() if contact.phone else ""

            if not name or not phone:
                failed_count += 1
                logger.warning(
                    "Contato invalido ignorado. Nome: %s | Telefone: %s",
                    contact.name,
                    contact.phone,
                )
                continue

            message = f"Olá, {name} tudo bem com você?"

            try:
                self._zapi_client.send_text_message(phone, message)
            except (RuntimeError, ValueError) as error:
                failed_count += 1
                logger.error(
                    "Falha ao enviar mensagem para %s | Telefone: %s | Erro: %s",
                    name,
                    phone,
                    error,
                )
                continue

            sent_count += 1
            logger.info(
                "Mensagem enviada com sucesso para %s | Telefone: %s",
                name,
                phone,
            )

        return {
            "total_contacts": len(contacts),
            "sent_count": sent_count,
            "failed_count": failed_count,
        }
