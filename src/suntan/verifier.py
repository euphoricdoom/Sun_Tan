from __future__ import annotations

from pathlib import Path

from suntan.canonical_json import canonical_json
from suntan.hashing import sha256_file, sha256_text
from suntan.signer import DeterministicSigner


REQUIRED_FIELDS = {
    "bridge_version",
    "source_system",
    "target_system",
    "artifact_hash",
    "payload_hash",
    "created_at",
    "signature",
}


def _unsigned_payload(packet: dict) -> dict:
    return {key: value for key, value in packet.items() if key != "signature"}


def _payload_hash_payload(packet: dict) -> dict:
    return {
        key: value
        for key, value in packet.items()
        if key not in {"signature", "payload_hash"}
    }


def verify_packet(packet: dict, artifact_path: str | Path | None = None) -> bool:
    missing = REQUIRED_FIELDS.difference(packet.keys())

    if missing:
        return False

    payload_hash_payload = _payload_hash_payload(packet)
    expected_payload_hash = f"sha256:{sha256_text(canonical_json(payload_hash_payload))}"

    if packet["payload_hash"] != expected_payload_hash:
        return False

    signed_payload = _unsigned_payload(packet)
    serialized_signed_payload = canonical_json(signed_payload)

    signer = DeterministicSigner()
    if not signer.verify(serialized_signed_payload, packet["signature"]):
        return False

    if artifact_path is not None:
        expected_artifact_hash = f"sha256:{sha256_file(artifact_path)}"
        if packet["artifact_hash"] != expected_artifact_hash:
            return False

    return True
