# Sun_Tan

Sun_Tan is the bridge layer between `project-512d` / Loop and `.Neon`.

It translates outputs from intelligence systems into deterministic bridge packets that can be hashed, verified, and exported into `.Neon` continuity workflows.

## Core model

```text
Loop / project-512d produces artifacts, proofs, or model outputs
Sun_Tan wraps them into deterministic bridge packets
.Neon records origin, lineage, policy, and verification
```

## First principle

```text
verify before update
```

Sun_Tan preserves consistency before downstream systems import or promote an artifact.

## Quickstart

Install locally from the repo root:

```bash
python -m pip install -e .
```

Run tests:

```bash
python -m pytest -q
```

Create a trusted demo fixture:

```bash
suntan fixture examples/full_bridge_demo/generated
```

Create a bridge packet:

```bash
suntan claim examples/full_bridge_demo/artifact.txt --out examples/full_bridge_demo/packet.json
```

Verify the packet against the artifact:

```bash
suntan verify examples/full_bridge_demo/packet.json --artifact examples/full_bridge_demo/artifact.txt
```

Export a `.Neon` origin claim:

```bash
suntan to-neon examples/full_bridge_demo/packet.json \
  --artifact examples/full_bridge_demo/artifact.txt \
  --out examples/full_bridge_demo/origin.origin.json
```

Expected verification output:

```text
valid
```

## Implemented foundation

- Bridge packet schema
- Deterministic canonical JSON
- SHA-256 artifact hashing
- Minimal local deterministic signature helper
- CLI packet creation and verification
- `.Neon` and `project-512d` adapter boundaries
- Trusted fixture generator
- Pulse recorder
- Contract document for bridge behavior
- Unit tests
- GitHub Actions CI

## Repository role

```text
512D thinks.
Sun_Tan translates.
.NeoN remembers.
```
