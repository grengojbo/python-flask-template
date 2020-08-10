import hashlib
import hmac
from typing import Any, Dict

from .types import ContextProto, EventProto


def validate_HMAC(message: bytes, secret: str, hash: str) -> bool:

    # GitHub and the sign flag prefix the hash with "sha1="
    received_hash = get_hash(hash)

    # Hash message with secret
    expected_MAC = hmac.new(secret.encode(), message, hashlib.sha1)
    created_hash = expected_MAC.hexdigest()

    return hmac.compare_digest(received_hash, created_hash)


def get_hash(hash: str) -> str:
    if hash.startswith("sha1="):
        hash = hash[5:]
    return hash


def handle(event: EventProto, context: ContextProto) -> Dict[str, Any]:
    # We receive the hashed message in form of a header
    message_MAC = event.headers.get("Hmac", type=str)

    if message_MAC is None:
        return {"statusCode": 400, "body": "bad request"}

    # Read secret from inside the container
    with open("/var/openfaas/secrets/shared-secret", "r") as f:
        payload_secret = f.read()

    # Function to validate the HMAC
    if not validate_HMAC(event.body, payload_secret, message_MAC):
        return {"statusCode": 401, "body": "unauthorized"}

    return {"statusCode": 200, "body": "OK"}
