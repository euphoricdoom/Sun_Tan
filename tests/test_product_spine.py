import json

from suntan.adapters.neon_adapter import to_neon_origin_claim
from suntan.packet import build_bridge_packet
from suntan.verifier import verify_packet


def test_loop_to_suntan_to_neon_product_spine(tmp_path):
    loop_artifact = tmp_path / "loop_artifact.json"
    loop_artifact.write_text(
        json.dumps(
            {
                "artifact_type": "loop_proof_fixture",
                "source_system": "project-512d",
                "task": "demo_zero_forgetting_bridge",
                "metrics": {
                    "retention_gate": "pass",
                    "quality_gate": "pass",
                    "forgetting_delta": 0.0,
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    packet = build_bridge_packet(
        artifact_path=loop_artifact,
        source_system="project-512d",
        target_system=".Neon",
        lineage=["loop/demo-root"],
    ).to_dict()

    assert verify_packet(packet, artifact_path=loop_artifact)

    neon_claim = to_neon_origin_claim(packet)

    assert neon_claim["claim_type"] == "TRUSTED_ORIGIN"
    assert neon_claim["source_system"] == "project-512d"
    assert neon_claim["artifact_hash"] == packet["artifact_hash"]
    assert neon_claim["bridge_payload_hash"] == packet["payload_hash"]
    assert neon_claim["lineage"] == ["loop/demo-root"]
