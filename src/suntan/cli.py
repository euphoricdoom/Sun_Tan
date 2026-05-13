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


def cmd_claim(args):
    pulse_hash = None

    if args.pulse_log and args.summary:
        artifact_packet = build_bridge_packet(
            artifact_path=args.artifact,
            source_system=args.source,
            target_system=args.target,
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
        source_system=args.source,
        target_system=args.target,
        policy=args.policy,
        lineage=args.lineage,
        pulse_hash=pulse_hash,
    ).to_dict()

    write_json(args.out, packet)
    print(f"packet written: {args.out}")


def cmd_verify(args):
    packet = read_json(args.packet)
    ok = verify_packet(packet, artifact_path=args.artifact)
    print("valid" if ok else "invalid")


def cmd_to_neon(args):
    packet = read_json(args.packet)

    if not verify_packet(packet, artifact_path=args.artifact):
        raise SystemExit("packet verification failed")

    claim = to_neon_origin_claim(packet)
    write_json(args.out, claim)
    print(f".Neon origin claim written: {args.out}")


def cmd_fixture(args):
    result = create_trusted_fixture(args.root)
    print("trusted fixture created")
    print(f"artifact: {result['artifact']}")
    print(f"packet:   {result['packet']}")
    print(f"claim:    {result['claim']}")


def main():
    parser = argparse.ArgumentParser(prog="suntan")
    sub = parser.add_subparsers(dest="command")

    claim = sub.add_parser("claim")
    claim.add_argument("artifact")
    claim.add_argument("--source", default="project-512d")
    claim.add_argument("--target", default=".Neon")
    claim.add_argument("--policy", default="policy_v1")
    claim.add_argument("--lineage", action="append", default=[])
    claim.add_argument("--pulse-log")
    claim.add_argument("--summary")
    claim.add_argument("--out", required=True)
    claim.set_defaults(func=cmd_claim)

    verify = sub.add_parser("verify")
    verify.add_argument("packet")
    verify.add_argument("--artifact")
    verify.set_defaults(func=cmd_verify)

    neon = sub.add_parser("to-neon")
    neon.add_argument("packet")
    neon.add_argument("--artifact")
    neon.add_argument("--out", required=True)
    neon.set_defaults(func=cmd_to_neon)

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
