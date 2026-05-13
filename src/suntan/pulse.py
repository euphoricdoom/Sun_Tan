from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from suntan.canonical_json import canonical_json
from suntan.hashing import sha256_text


def build_pulse_event(
    artifact_hash: str,
    event_type: str,
    summary: str,
) -> dict:
    summary_hash = f"sha256:{sha256_text(summary)}"

    return {
        "timestamp": datetime.now(UTC).isoformat(),
        "artifact_hash": artifact_hash,
        "event_type": event_type,
        "summary_hash": summary_hash,
    }


def append_pulse(path: str | Path, event: dict) -> str:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    serialized = canonical_json(event)

    with path.open("a", encoding="utf-8") as handle:
        handle.write(serialized + "\n")

    return f"sha256:{sha256_text(serialized)}"
