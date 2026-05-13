import argparse
import json
from datetime import datetime, UTC
from pathlib import Path

from suntan.canonical_json import canonical_json
from suntan.hashing import sha256_file, sha256_text
from suntan.signer import DeterministicSigner
from suntan.verifier import verify_packet


signer = DeterministicSigner()


def build_packet(path: str, source: str, target: str) -> dict:
    artifact_hash = sha256_file(path)

    payload = {
        "bridge_version": "0.1",
        "source_system": source,
        "target_system": target,
        "artifact_hash": artifact_hash,
        "created_at": datetime.now(UTC).isoformat(),
    }

    payload_hash = sha256_text(canonical_json(payload))
    payload["payload_hash"] = payload_hash

    serialized = canonical_json(payload)
    payload["signature"] = signer.sign(serialized)

    return payload


def cmd_claim(args):
    packet = build_packet(args.artifact, args.source, args.target)

    out_path = Path(args.out)
    out_path.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    print(f"packet written: {out_path}")


def cmd_verify(args):
    packet = json.loads(Path(args.packet).read_text(encoding="utf-8"))

    ok = verify_packet(packet)

    print("valid" if ok else "invalid")


def main():
    parser = argparse.ArgumentParser(prog="suntan")
    sub = parser.add_subparsers(dest="command")

    claim = sub.add_parser("claim")
    claim.add_argument("artifact")
    claim.add_argument("--source", required=True)
    claim.add_argument("--target", required=True)
    claim.add_argument("--out", required=True)
    claim.set_defaults(func=cmd_claim)

    verify = sub.add_parser("verify")
    verify.add_argument("packet")
    verify.set_defaults(func=cmd_verify)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
