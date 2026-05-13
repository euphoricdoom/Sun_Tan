from hashlib import sha256

DEFAULT_LOCAL_SALT = "suntan-local-v0"


class DeterministicSigner:
    """Minimal deterministic local signing helper.

    This is intentionally simple and is not a replacement for
    real asymmetric cryptography.
    """

    def __init__(self, salt: str = DEFAULT_LOCAL_SALT):
        self.salt = salt

    def sign(self, payload: str) -> str:
        data = f"{self.salt}:{payload}".encode("utf-8")
        return sha256(data).hexdigest()

    def verify(self, payload: str, signature: str) -> bool:
        return self.sign(payload) == signature
