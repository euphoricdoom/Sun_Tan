# .Neon Compatibility

`.Neon` is the continuity organ of the unified product.

Sun_Tan exports verified bridge packets into `.Neon`-style origin claim files.

## Minimum .Neon Origin Claim Shape

```json
{
  "claim_version": "0.1",
  "claim_type": "TRUSTED_ORIGIN",
  "source_system": "project-512d",
  "artifact_hash": "sha256:...",
  "bridge_payload_hash": "sha256:...",
  "bridge_signature": "...",
  "policy": "policy_v1",
  "lineage": [],
  "pulse_hash": null
}
```

## Required Sun_Tan behavior

Sun_Tan must verify a packet before creating an origin claim.

```bash
python -m suntan.cli to-neon packet.json \
  --artifact artifact.txt \
  --out artifact.origin.json
```

If verification fails, Sun_Tan must not emit the origin claim.

## Boundary

Sun_Tan creates a compatible claim export.

`.Neon` remains responsible for storage, traversal, ancestry, descendants, and long-term continuity mechanics.
