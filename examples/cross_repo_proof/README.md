# Cross-Repo Compatibility Proof

This folder captures the first compatibility proof based on real shapes from the two neighboring repos:

- `.Neon`
- `project-512d` / Loop

## Real .Neon shape

The `.Neon` file format requires:

- `neon_version`
- `kind`
- `artifact_id`
- `title`
- `artifact_type`
- `creator`
- `origin`
- `lineage`
- `proof`

Important invariants:

- `kind` must be `artifact`
- `artifact_id` must begin with `.N/`
- `lineage` must contain `parents` and `events`
- `proof.hash_algorithm` must be `sha256`

Fixture:

```text
examples/cross_repo_proof/neon_golden_shape.neon
```

## Real Loop / project-512d shape

The Loop / project-512d README describes a zero-forgetting continual-learning substrate with:

- fixed encoder
- isolated task heads
- `.npz` model artifacts
- proof/reproduction outputs
- int8 model artifacts
- kernel lattice outputs
- zero-forgetting metrics

Fixture:

```text
examples/cross_repo_proof/loop_512d_readme_shape.json
```

## Proof

The test suite verifies that:

1. The `.Neon` compatibility fixture satisfies the real `.neon` contract shape.
2. The Loop compatibility fixture can be wrapped by Sun_Tan.
3. The Sun_Tan packet verifies against the Loop artifact.
4. The verified packet becomes a `.Neon`-compatible origin claim.

Run:

```bash
python -m pytest tests/test_cross_repo_compatibility.py -q
```

## Meaning

This is the first ecosystem proof:

```text
Real Loop shape
→ Sun_Tan bridge packet
→ verified exchange
→ real .Neon-shaped continuity claim
```
