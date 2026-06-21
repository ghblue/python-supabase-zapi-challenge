import requests


class ZApiClient:
    def __init__(self, instance_id: str, token: str, client_token: str):
        self._base_url = (
            f"https://api.z-api.io/instances/{instance_id}/token/{token}"
        )
        self._client_token = client_token

    def send_text_message(self, phone: str, message: str) -> bool:
        if not phone:
            raise ValueError("O telefone nao pode estar vazio.")

        if not message:
            raise ValueError("A mensagem nao pode estar vazia.")

        url = f"{self._base_url}/send-text"
        headers = {
            "Client-Token": self._client_token,
            "Content-Type": "application/json",
        }
        payload = {
            "phone": phone,
            "message": message,
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=15,
            )
        except requests.Timeout as error:
            raise RuntimeError(
                "Tempo limite excedido ao enviar mensagem pela Z-API."
            ) from error
        except requests.ConnectionError as error:
            raise RuntimeError(
                "Erro de conexao ao enviar mensagem pela Z-API."
            ) from error
        except requests.RequestException as error:
            raise RuntimeError(
                "Erro inesperado ao enviar mensagem pela Z-API."
            ) from error

        if 200 <= response.status_code <= 299:
            return True

        raise RuntimeError(
            f"Falha ao enviar mensagem pela Z-API. Status HTTP: {response.status_code}."
        )
