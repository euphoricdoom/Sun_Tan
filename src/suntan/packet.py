from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import UTC, datetime
from pathlib import Path

from suntan.canonical_json import canonical_json
from suntan.hashing import sha256_file, sha256_text
from suntan.signer import DeterministicSigner


@dataclass(frozen=True)
class BridgePacket:
    bridge_version: str
    source_system: str
    target_system: str
    artifact_hash: str
    payload_hash: str
    created_at: str
    signature: str
    policy: str | None = "policy_v1"
    lineage: list[str] = field(default_factory=list)
    pulse_hash: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def _unsigned_payload(data: dict) -> dict:
    return {key: value for key, value in data.items() if key != "signature"}


def build_bridge_packet(
    artifact_path: str | Path,
    source_system: str = "project-512d",
    target_system: str = ".Neon",
    policy: str | None = "policy_v1",
    lineage: list[str] | None = None,
    pulse_hash: str | None = None,
    signer: DeterministicSigner | None = None,
) -> BridgePacket:
    signer = signer or DeterministicSigner()

    payload = {
        "bridge_version": "0.1",
        "source_system": source_system,
        "target_system": target_system,
        "artifact_hash": f"sha256:{sha256_file(artifact_path)}",
        "created_at": datetime.now(UTC).isoformat(),
        "policy": policy,
        "lineage": lineage or [],
        "pulse_hash": pulse_hash,
    }

    payload["payload_hash"] = f"sha256:{sha256_text(canonical_json(payload))}"
    payload["signature"] = signer.sign(canonical_json(payload))

    return BridgePacket(**payload)


def packet_signing_payload(packet: dict) -> str:
    return canonical_json(_unsigned_payload(packet))
