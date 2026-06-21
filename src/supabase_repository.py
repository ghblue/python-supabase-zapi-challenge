from dataclasses import dataclass

from supabase import create_client


@dataclass(frozen=True)
class Contact:
    id: str
    name: str
    phone: str


class SupabaseContactRepository:
    def __init__(self, supabase_url: str, supabase_key: str):
        self._client = create_client(supabase_url, supabase_key)

    def get_active_contacts(self, limit: int = 3) -> list[Contact]:
        safe_limit = min(limit, 3)

        if safe_limit <= 0:
            return []

        try:
            response = (
                self._client.table("contacts")
                .select("id,name,phone")
                .eq("is_active", True)
                .order("created_at", desc=False)
                .limit(safe_limit)
                .execute()
            )

            contacts_data = response.data or []

            return [
                Contact(
                    id=str(contact["id"]),
                    name=contact["name"],
                    phone=contact["phone"],
                )
                for contact in contacts_data
            ]
        except Exception as error:
            raise RuntimeError(
                "Falha ao buscar contatos ativos no Supabase."
            ) from error
