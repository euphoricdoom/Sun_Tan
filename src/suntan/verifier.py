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


def verify_packet(packet: dict, artifact_path: str | Path | None = None) -> bool:
    missing = REQUIRED_FIELDS.difference(packet.keys())

    if missing:
        return False

    unsigned = _unsigned_payload(packet)
    serialized = canonical_json(unsigned)

    expected_payload_hash = f"sha256:{sha256_text(serialized)}"
    if packet["payload_hash"] != expected_payload_hash:
        return False

    signer = DeterministicSigner()
    if not signer.verify(serialized, packet["signature"]):
        return False

    if artifact_path is not None:
        expected_artifact_hash = f"sha256:{sha256_file(artifact_path)}"
        if packet["artifact_hash"] != expected_artifact_hash:
            return False

    return True
