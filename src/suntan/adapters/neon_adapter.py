from __future__ import annotations


def to_neon_origin_claim(packet: dict) -> dict:
    """Translate a verified bridge packet into a minimal .Neon-style origin claim."""
    return {
        "claim_version": "0.1",
        "claim_type": "TRUSTED_ORIGIN",
        "source_system": packet["source_system"],
        "artifact_hash": packet["artifact_hash"],
        "bridge_payload_hash": packet["payload_hash"],
        "bridge_signature": packet["signature"],
        "policy": packet.get("policy", "policy_v1"),
        "lineage": packet.get("lineage", []),
        "pulse_hash": packet.get("pulse_hash"),
    }
