# Loop Compatibility

Loop refers to `project-512d`, the intelligence organ of the unified product.

Sun_Tan does not need to know Loop internals to bridge Loop outputs.

## Minimum Loop Artifact Contract

A Loop-compatible artifact must be a readable file produced by Loop or exported from a Loop run.

Examples:

- proof report
- inference output
- model artifact
- validation summary
- memory summary
- task-head export

## Required Sun_Tan behavior

Given a Loop artifact, Sun_Tan must:

1. Hash the artifact bytes.
2. Build a bridge packet.
3. Set `source_system` to `project-512d` by default.
4. Preserve optional lineage references.
5. Preserve optional pulse hash.
6. Verify before export.

## Default command

```bash
python -m suntan.cli claim path/to/loop_artifact \
  --source project-512d \
  --target .Neon \
  --out path/to/packet.json
```

## Boundary

Loop owns cognition and proof generation.

Sun_Tan owns bridge integrity.

.Neon owns continuity storage.
