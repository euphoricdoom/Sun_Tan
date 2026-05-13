import json

from suntan.adapters.neon_adapter import to_neon_origin_claim
from suntan.packet import build_bridge_packet
from suntan.verifier import verify_packet


def test_build_and_verify_packet(tmp_path):
    artifact = tmp_path / "artifact.txt"
    artifact.write_text("hello bridge\n", encoding="utf-8")

    packet = build_bridge_packet(artifact).to_dict()

    assert packet["artifact_hash"].startswith("sha256:")
    assert packet["payload_hash"].startswith("sha256:")
    assert verify_packet(packet, artifact_path=artifact)


def test_packet_fails_when_artifact_changes(tmp_path):
    artifact = tmp_path / "artifact.txt"
    artifact.write_text("first\n", encoding="utf-8")

    packet = build_bridge_packet(artifact).to_dict()

    artifact.write_text("changed\n", encoding="utf-8")

    assert not verify_packet(packet, artifact_path=artifact)


def test_neon_claim_translation(tmp_path):
    artifact = tmp_path / "artifact.txt"
    artifact.write_text("claim me\n", encoding="utf-8")

    packet = build_bridge_packet(artifact).to_dict()
    claim = to_neon_origin_claim(packet)

    assert claim["claim_type"] == "TRUSTED_ORIGIN"
    assert claim["artifact_hash"] == packet["artifact_hash"]
    assert claim["bridge_payload_hash"] == packet["payload_hash"]
