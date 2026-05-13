from suntan.fixtures import create_trusted_fixture
from suntan.pulse import append_pulse, build_pulse_event


def test_pulse_append_returns_hash(tmp_path):
    pulse_log = tmp_path / ".neon" / "private" / "pulses" / "events.jsonl"
    event = build_pulse_event(
        artifact_hash="sha256:" + "a" * 64,
        event_type="claim",
        summary="small summary",
    )

    pulse_hash = append_pulse(pulse_log, event)

    assert pulse_hash.startswith("sha256:")
    assert pulse_log.exists()
    assert len(pulse_log.read_text(encoding="utf-8").splitlines()) == 1


def test_create_trusted_fixture(tmp_path):
    result = create_trusted_fixture(tmp_path)

    assert result["artifact"].endswith("trusted_artifact.txt")
    assert result["packet"].endswith("trusted_packet.json")
    assert result["claim"].endswith("trusted_origin.origin.json")
