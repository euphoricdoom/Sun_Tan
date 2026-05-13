# Product Spine Proof

This example proves the first full product spine:

```text
Loop artifact
→ Sun_Tan bridge packet
→ Sun_Tan verification
→ .Neon origin claim
```

## Source fixture

```text
examples/product_spine_proof/loop_artifact.json
```

The fixture represents a Loop / project-512d proof or inference artifact.

## Run the proof manually

From repo root:

```bash
python -m suntan.cli claim examples/product_spine_proof/loop_artifact.json \
  --source project-512d \
  --target .Neon \
  --lineage loop/demo-root \
  --out examples/product_spine_proof/loop_packet.json

python -m suntan.cli verify examples/product_spine_proof/loop_packet.json \
  --artifact examples/product_spine_proof/loop_artifact.json

python -m suntan.cli to-neon examples/product_spine_proof/loop_packet.json \
  --artifact examples/product_spine_proof/loop_artifact.json \
  --out examples/product_spine_proof/loop_origin.origin.json
```

Expected verification output:

```text
valid
```

## Meaning

This demonstrates the current one-product spine:

```text
Loop thinks.
Sun_Tan translates.
.NeoN remembers.
```
