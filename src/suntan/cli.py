import argparse
import json
from pathlib import Path

from suntan.adapters.neon_adapter import to_neon_origin_claim
from suntan.fixtures import create_trusted_fixture
from suntan.packet import build_bridge_packet
from suntan.pulse import append_pulse, build_pulse_event
from suntan.verifier import verify_packet


def write_json(path: str | Path, data: dict) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")


def read_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def build_and_write_packet(args, source: str | None = None, target: str | None = None):
    pulse_hash = None
    source_system = source or args.source
    target_system = target or args.target

    if args.pulse_log and args.summary:
        artifact_packet = build_bridge_packet(
            artifact_path=args.artifact,
            source_system=source_system,
            target_system=target_system,
            policy=args.policy,
            lineage=args.lineage,
        )
        event = build_pulse_event(
            artifact_hash=artifact_packet.artifact_hash,
            event_type="claim",
            summary=args.summary,
        )
        pulse_hash = append_pulse(args.pulse_log, event)

    packet = build_bridge_packet(
        artifact_path=args.artifact,
        source_system=source_system,
        target_system=target_system,
        policy=args.policy,
        lineage=args.lineage,
        pulse_hash=pulse_hash,
    ).to_dict()

    write_json(args.out, packet)
    print(f"packet written: {args.out}")


def cmd_claim(args):
    build_and_write_packet(args)


def cmd_export_loop(args):
    build_and_write_packet(args, source="project-512d", target=".Neon")


def cmd_verify(args):
    packet = read_json(args.packet)
    ok = verify_packet(packet, artifact_path=args.artifact)
    print("valid" if ok else "invalid")


def export_neon_claim(packet_path: str, artifact_path: str | None, out_path: str):
    packet = read_json(packet_path)

    if not verify_packet(packet, artifact_path=artifact_path):
        raise SystemExit("packet verification failed")

    claim = to_neon_origin_claim(packet)
    write_json(out_path, claim)
    print(f".Neon origin claim written: {out_path}")


def cmd_to_neon(args):
    export_neon_claim(args.packet, args.artifact, args.out)


def cmd_export_neon(args):
    export_neon_claim(args.packet, args.artifact, args.out)


def cmd_fixture(args):
    result = create_trusted_fixture(args.root)
    print("trusted fixture created")
    print(f"artifact: {result['artifact']}")
    print(f"packet:   {result['packet']}")
    print(f"claim:    {result['claim']}")


def add_packet_args(command):
    command.add_argument("artifact")
    command.add_argument("--source", default="project-512d")
    command.add_argument("--target", default=".Neon")
    command.add_argument("--policy", default="policy_v1")
    command.add_argument("--lineage", action="append", default=[])
    command.add_argument("--pulse-log")
    command.add_argument("--summary")
    command.add_argument("--out", required=True)


def add_neon_export_args(command):
    command.add_argument("packet")
    command.add_argument("--artifact")
    command.add_argument("--out", required=True)


def main():
    parser = argparse.ArgumentParser(prog="suntan")
    sub = parser.add_subparsers(dest="command")

    claim = sub.add_parser("claim")
    add_packet_args(claim)
    claim.set_defaults(func=cmd_claim)

    export_loop = sub.add_parser("export-loop")
    add_packet_args(export_loop)
    export_loop.set_defaults(func=cmd_export_loop)

    verify = sub.add_parser("verify")
    verify.add_argument("packet")
    verify.add_argument("--artifact")
    verify.set_defaults(func=cmd_verify)

    neon = sub.add_parser("to-neon")
    add_neon_export_args(neon)
    neon.set_defaults(func=cmd_to_neon)

    export_neon = sub.add_parser("export-neon")
    add_neon_export_args(export_neon)
    export_neon.set_defaults(func=cmd_export_neon)

    fixture = sub.add_parser("fixture")
    fixture.add_argument("root")
    fixture.set_defaults(func=cmd_fixture)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
