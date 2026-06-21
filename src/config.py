import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    supabase_url: str
    supabase_key: str
    zapi_instance_id: str
    zapi_token: str
    zapi_client_token: str


def load_settings() -> Settings:
    load_dotenv()

    required_variables = {
        "SUPABASE_URL": os.getenv("SUPABASE_URL"),
        "SUPABASE_KEY": os.getenv("SUPABASE_KEY"),
        "ZAPI_INSTANCE_ID": os.getenv("ZAPI_INSTANCE_ID"),
        "ZAPI_TOKEN": os.getenv("ZAPI_TOKEN"),
        "ZAPI_CLIENT_TOKEN": os.getenv("ZAPI_CLIENT_TOKEN"),
    }

    missing_variables = [
        name for name, value in required_variables.items() if not value
    ]

    if missing_variables:
        missing_names = ", ".join(missing_variables)
        raise ValueError(f"Variaveis obrigatorias ausentes: {missing_names}")

    return Settings(
        supabase_url=required_variables["SUPABASE_URL"],
        supabase_key=required_variables["SUPABASE_KEY"],
        zapi_instance_id=required_variables["ZAPI_INSTANCE_ID"],
        zapi_token=required_variables["ZAPI_TOKEN"],
        zapi_client_token=required_variables["ZAPI_CLIENT_TOKEN"],
    )
