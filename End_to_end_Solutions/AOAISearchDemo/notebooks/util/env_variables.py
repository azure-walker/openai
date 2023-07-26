import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Env:
    """
    loads all environment variables into a predefined set of properties
    """

    load_dotenv()
    client_secret: Optional[str] = os.environ.get("AZURE_CLIENT_SECRET")
    client_id: Optional[str] = os.environ.get("AZURE_CLIENT_ID")
    tenant_id: Optional[str] = os.environ.get("AZURE_TENANT_ID")