# Full Bridge Demo

This example shows the first complete Sun_Tan bridge flow:

```text
artifact.txt
→ packet.json
→ origin.origin.json
→ verification: valid
```

## Run from repo root

```bash
python -m suntan.cli fixture examples/full_bridge_demo/generated
```

Or run the manual flow:

```bash
printf "demo artifact\n" > examples/full_bridge_demo/artifact.txt

python -m suntan.cli claim examples/full_bridge_demo/artifact.txt \
  --out examples/full_bridge_demo/packet.json

python -m suntan.cli verify examples/full_bridge_demo/packet.json \
  --artifact examples/full_bridge_demo/artifact.txt

python -m suntan.cli to-neon examples/full_bridge_demo/packet.json \
  --artifact examples/full_bridge_demo/artifact.txt \
  --out examples/full_bridge_demo/origin.origin.json
```

Expected verification output:

```text
valid
```

## What this proves

- The artifact is hashed.
- The bridge packet is canonically serialized.
- The packet hash is reproducible.
- The local deterministic signature verifies.
- Artifact tampering breaks verification.
- A verified packet can become a `.Neon`-style origin claim.
