import os
import requests

from dotenv import load_dotenv


# ============================================================
# LOAD ENVIRONMENT
# ============================================================

load_dotenv()

BANK_ID = os.getenv("HINDSIGHT_BANK_ID")
BASE_URL = os.getenv(
    "HINDSIGHT_BASE_URL",
    "https://api.hindsight.vectorize.io"
)
API_KEY = os.getenv("HINDSIGHT_API_KEY")


# ============================================================
# COMMON HEADERS
# ============================================================

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}


# ============================================================
# SIMPLE MEMORY OBJECT
# ============================================================

class Memory:
    def __init__(
        self,
        text,
        memory_type=None,
        memory_id=None
    ):
        self.text = text
        self.type = memory_type
        self.id = memory_id

    def __str__(self):
        return self.text


# ============================================================
# RECALL MEMORY
# ============================================================

def recall(query):

    if not API_KEY:
        raise RuntimeError(
            "HINDSIGHT_API_KEY is missing from .env"
        )

    if not BANK_ID:
        raise RuntimeError(
            "HINDSIGHT_BANK_ID is missing from .env"
        )

    url = (
        f"{BASE_URL}/v1/default/banks/"
        f"{BANK_ID}/memories/recall"
    )

    payload = {
        "query": query,
        "max_tokens": 1000,
        "budget": "low"
    }

    try:

        response = requests.post(
            url,
            headers=HEADERS,
            json=payload,
            timeout=60
        )

    except requests.exceptions.Timeout:

        raise RuntimeError(
            "Hindsight request timed out. "
            "Please try again once."
        )

    except requests.exceptions.RequestException as e:

        raise RuntimeError(
            f"Hindsight connection error: {str(e)}"
        )


    # ========================================================
    # CREDIT ERROR
    # ========================================================

    if response.status_code == 402:

        raise RuntimeError(
            "Hindsight credits are insufficient "
            "(HTTP 402 Payment Required)."
        )


    # ========================================================
    # API KEY ERROR
    # ========================================================

    if response.status_code == 401:

        raise RuntimeError(
            "Hindsight API key is invalid or expired "
            "(HTTP 401)."
        )


    # ========================================================
    # PERMISSION ERROR
    # ========================================================

    if response.status_code == 403:

        raise RuntimeError(
            "Hindsight API key does not have permission "
            "for this memory bank (HTTP 403)."
        )


    # ========================================================
    # BANK NOT FOUND
    # ========================================================

    if response.status_code == 404:

        raise RuntimeError(
            f"Hindsight memory bank '{BANK_ID}' "
            "was not found (HTTP 404)."
        )


    # ========================================================
    # OTHER API ERRORS
    # ========================================================

    if not response.ok:

        try:
            error_data = response.json()
        except Exception:
            error_data = response.text

        raise RuntimeError(
            f"Hindsight API error "
            f"(HTTP {response.status_code}): "
            f"{error_data}"
        )


    # ========================================================
    # SUCCESS
    # ========================================================

    try:

        data = response.json()

    except Exception:

        raise RuntimeError(
            "Hindsight returned an invalid response."
        )


    results = data.get(
        "results",
        []
    )

    memories = []

    for item in results:

        memory = Memory(
            text=item.get(
                "text",
                ""
            ),
            memory_type=item.get(
                "type"
            ),
            memory_id=item.get(
                "id"
            )
        )

        memories.append(
            memory
        )

    return memories


# ============================================================
# RETAIN / SAVE MEMORY
# ============================================================

def remember(content):

    if not API_KEY:
        raise RuntimeError(
            "HINDSIGHT_API_KEY is missing from .env"
        )

    if not BANK_ID:
        raise RuntimeError(
            "HINDSIGHT_BANK_ID is missing from .env"
        )

    url = (
        f"{BASE_URL}/v1/default/banks/"
        f"{BANK_ID}/memories"
    )

    payload = {
        "items": [
            {
                "content": content
            }
        ]
    }

    try:

        response = requests.post(
            url,
            headers=HEADERS,
            json=payload,
            timeout=60
        )

    except requests.exceptions.Timeout:

        raise RuntimeError(
            "Hindsight retain request timed out."
        )

    except requests.exceptions.RequestException as e:

        raise RuntimeError(
            f"Hindsight connection error: {str(e)}"
        )


    # ========================================================
    # CREDIT ERROR
    # ========================================================

    if response.status_code == 402:

        raise RuntimeError(
            "Hindsight credits are insufficient "
            "(HTTP 402 Payment Required)."
        )


    # ========================================================
    # API KEY ERROR
    # ========================================================

    if response.status_code == 401:

        raise RuntimeError(
            "Hindsight API key is invalid or expired "
            "(HTTP 401)."
        )


    # ========================================================
    # PERMISSION ERROR
    # ========================================================

    if response.status_code == 403:

        raise RuntimeError(
            "Hindsight API key does not have permission "
            "for this memory bank (HTTP 403)."
        )


    # ========================================================
    # OTHER ERRORS
    # ========================================================

    if not response.ok:

        try:
            error_data = response.json()
        except Exception:
            error_data = response.text

        raise RuntimeError(
            f"Hindsight API error "
            f"(HTTP {response.status_code}): "
            f"{error_data}"
        )


    # ========================================================
    # SUCCESS
    # ========================================================

    try:
        return response.json()

    except Exception:
        return {
            "success": True
        }