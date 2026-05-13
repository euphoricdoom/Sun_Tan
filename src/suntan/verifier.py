from suntan.canonical_json import canonical_json
from suntan.signer import DeterministicSigner


signer = DeterministicSigner()


REQUIRED_FIELDS = {
    "bridge_version",
    "source_system",
    "target_system",
    "artifact_hash",
    "payload_hash",
    "signature",
}


def verify_packet(packet: dict) -> bool:
    missing = REQUIRED_FIELDS.difference(packet.keys())

    if missing:
        return False

    payload = {
        k: v
        for k, v in packet.items()
        if k != "signature"
    }

    serialized = canonical_json(payload)

    return signer.verify(serialized, packet["signature"])
