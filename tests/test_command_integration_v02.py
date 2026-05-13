import json
import os
import subprocess
import sys


def run_cli(*args):
    env = os.environ.copy()
    env["PYTHONPATH"] = "src" + os.pathsep + env.get("PYTHONPATH", "")

    return subprocess.run(
        [sys.executable, "-m", "suntan.cli", *args],
        check=True,
        text=True,
        capture_output=True,
        env=env,
    )


def test_phase_2_command_level_flow(tmp_path):
    artifact = tmp_path / "loop_artifact.json"
    packet = tmp_path / "packet.json"
    origin = tmp_path / "origin.origin.json"

    artifact.write_text(
        json.dumps(
            {
                "source_system": "project-512d",
                "artifact_type": "loop_command_export_fixture",
                "task": "phase_2_command_level_flow",
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    run_cli(
        "export-loop",
        str(artifact),
        "--lineage",
        ".N/example-root",
        "--out",
        str(packet),
    )

    verify = run_cli("verify", str(packet), "--artifact", str(artifact))

    run_cli(
        "export-neon",
        str(packet),
        "--artifact",
        str(artifact),
        "--out",
        str(origin),
    )

    assert "valid" in verify.stdout

    packet_data = json.loads(packet.read_text(encoding="utf-8"))
    origin_data = json.loads(origin.read_text(encoding="utf-8"))

    assert packet_data["source_system"] == "project-512d"
    assert packet_data["target_system"] == ".Neon"
    assert origin_data["claim_type"] == "TRUSTED_ORIGIN"
    assert origin_data["lineage"] == [".N/example-root"]
