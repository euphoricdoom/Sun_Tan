# Sun_Tan

Sun_Tan is the bridge layer between `project-512d` and `.Neon`.

It translates outputs from intelligence systems into deterministic bridge packets that can be hashed, verified, and later imported into `.Neon` continuity workflows.

## Core model

```text
project-512d produces artifacts, proofs, or model outputs
Sun_Tan wraps them into deterministic bridge packets
.Neon records origin, lineage, policy, and verification
```

## First principle

```text
verify before update
```

Sun_Tan preserves consistency before downstream systems import or promote an artifact.

## Planned foundation

- Bridge packet schema
- Deterministic canonical JSON
- SHA-256 artifact hashing
- Minimal local deterministic signature helper
- CLI packet creation and verification
- `.Neon` and `project-512d` adapter boundaries
- Contract document for bridge behavior
- Unit tests

## Repository role

```text
512D thinks.
Sun_Tan translates.
.NeoN remembers.
```
