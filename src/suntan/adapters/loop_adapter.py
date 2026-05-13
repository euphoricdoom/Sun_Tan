from __future__ import annotations

from pathlib import Path

from suntan.packet import BridgePacket, build_bridge_packet


LOOP_SYSTEM_NAME = "project-512d"


def export_loop_artifact(
    artifact_path: str | Path,
    target_system: str = ".Neon",
    lineage: list[str] | None = None,
    pulse_hash: str | None = None,
) -> BridgePacket:
    return build_bridge_packet(
        artifact_path=artifact_path,
        source_system=LOOP_SYSTEM_NAME,
        target_system=target_system,
        lineage=lineage,
        pulse_hash=pulse_hash,
    )
