import json
from pathlib import Path

from suntan.adapters.neon_adapter import to_neon_origin_claim
from suntan.packet import build_bridge_packet
from suntan.verifier import verify_packet


ROOT = Path(__file__).resolve().parents[1]


def test_real_neon_golden_shape_contract():
    fixture = ROOT / "examples" / "cross_repo_proof" / "neon_golden_shape.neon"
    data = json.loads(fixture.read_text(encoding="utf-8"))

    assert data["kind"] == "artifact"
    assert data["artifact_id"].startswith(".N/")
    assert "parents" in data["lineage"]
    assert "events" in data["lineage"]
    assert data["proof"]["hash_algorithm"] == "sha256"


def test_loop_512d_shape_can_bridge_to_neon_origin_claim():
    fixture = ROOT / "examples" / "cross_repo_proof" / "loop_512d_readme_shape.json"
    data = json.loads(fixture.read_text(encoding="utf-8"))

    assert data["source_system"] == "project-512d"
    assert "task head export" in data["artifact_family"]
    assert data["architecture"]["readout"] == "isolated task heads"

    packet = build_bridge_packet(
        artifact_path=fixture,
        source_system="project-512d",
        target_system=".Neon",
        lineage=[".N/example-root"],
    ).to_dict()

    assert verify_packet(packet, artifact_path=fixture)

    claim = to_neon_origin_claim(packet)

    assert claim["claim_type"] == "TRUSTED_ORIGIN"
    assert claim["source_system"] == "project-512d"
    assert claim["lineage"] == [".N/example-root"]
    assert claim["artifact_hash"] == packet["artifact_hash"]
