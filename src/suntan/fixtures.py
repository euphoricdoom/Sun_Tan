from __future__ import annotations

import json
from pathlib import Path

from suntan.adapters.neon_adapter import to_neon_origin_claim
from suntan.packet import build_bridge_packet
from suntan.verifier import verify_packet


def create_trusted_fixture(root: str | Path) -> dict:
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)

    artifact_path = root / "trusted_artifact.txt"
    packet_path = root / "trusted_packet.json"
    claim_path = root / "trusted_origin.origin.json"

    artifact_path.write_text("trusted fixture artifact\n", encoding="utf-8")

    packet = build_bridge_packet(artifact_path).to_dict()

    if not verify_packet(packet, artifact_path=artifact_path):
        raise RuntimeError("fixture packet failed verification")

    claim = to_neon_origin_claim(packet)

    packet_path.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    claim_path.write_text(json.dumps(claim, indent=2), encoding="utf-8")

    return {
        "artifact": str(artifact_path),
        "packet": str(packet_path),
        "claim": str(claim_path),
    }
