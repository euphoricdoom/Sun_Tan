import json
import subprocess
import sys


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "suntan.cli", *args],
        check=True,
        text=True,
        capture_output=True,
    )


def test_cli_fixture_command(tmp_path):
    demo = tmp_path / "demo"

    result = run_cli("fixture", str(demo))

    assert "trusted fixture created" in result.stdout
    assert (demo / "trusted_artifact.txt").exists()
    assert (demo / "trusted_packet.json").exists()
    assert (demo / "trusted_origin.origin.json").exists()


def test_cli_claim_verify_to_neon(tmp_path):
    artifact = tmp_path / "artifact.txt"
    packet = tmp_path / "packet.json"
    claim = tmp_path / "origin.origin.json"

    artifact.write_text("demo artifact\n", encoding="utf-8")

    run_cli("claim", str(artifact), "--out", str(packet))
    verify = run_cli("verify", str(packet), "--artifact", str(artifact))
    run_cli("to-neon", str(packet), "--artifact", str(artifact), "--out", str(claim))

    assert "valid" in verify.stdout
    claim_data = json.loads(claim.read_text(encoding="utf-8"))
    assert claim_data["claim_type"] == "TRUSTED_ORIGIN"
