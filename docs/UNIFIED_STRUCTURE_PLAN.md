# Unified Product Structure Plan

## Mission

Build one product from three modular subsystems:

- Loop (`project-512d`)
- Sun_Tan
- `.Neon`

The product should feel unified to the user while preserving clean internal subsystem boundaries.

## Product Model

```text
One product.
Three internal organs.
Shared truth layer.
```

## Internal Subsystem Roles

```text
Loop / project-512d
  Intelligence engine.
  Generates artifacts, proofs, inference outputs, task heads, memory outputs, and validation records.

Sun_Tan
  Bridge and verification layer.
  Translates Loop outputs into deterministic bridge packets and verifies packet integrity before export/import.

.Neon
  Continuity layer.
  Stores origin, lineage, claim state, policy attachment, and continuity traversal.
```

## Target Unified Product Shape

```text
Product Artifact
├── Loop payload
│   ├── model/proof output
│   ├── task identity
│   ├── validation summary
│   └── artifact hash
├── Sun_Tan bridge packet
│   ├── bridge version
│   ├── source system
│   ├── target system
│   ├── canonical payload hash
│   ├── deterministic signature
│   └── verification status
└── .Neon continuity wrapper
    ├── origin claim
    ├── lineage references
    ├── policy reference
    ├── optional pulse hash
    └── traversal metadata
```

## Product Rule

The user experiences one product.

The codebase preserves modular organs.

Do not turn modular boundaries into product fragmentation.

## Integration Rule

Sun_Tan connects the subsystems through contracts and packets, not by copying all code into one tangled runtime.

## First Unified Product Flow

```text
1. Loop produces an artifact.
2. Sun_Tan hashes the artifact.
3. Sun_Tan creates a bridge packet.
4. Sun_Tan verifies the packet.
5. .Neon imports the verified packet as an origin/lineage claim.
6. The product presents the combined Loop + .Neon continuity chain as one user-facing structure.
```

## Boundary Rule

One product does not mean one blob.

```text
Loop thinks.
Sun_Tan translates.
.NeoN remembers.
The product orchestrates all three.
```

## Next Build Requirements

- Add bridge packet schema.
- Add adapter interfaces for Loop and .Neon.
- Add trusted fixture generator.
- Add packet verification tests.
- Add CI validation.
- Add import/export examples.
- Add product-level orchestration notes.
