# Unified Structure Plan

## Mission

Use Sun_Tan to bridge `.Neon` and Loop (`project-512d`) into a single coordinated structure without collapsing their responsibilities into one tangled codebase.

## System Roles

```text
Loop / project-512d
  Generates intelligence artifacts, proofs, inference outputs, task heads, memory outputs, and validation records.

Sun_Tan
  Translates Loop outputs into deterministic bridge packets and verifies packet integrity before export/import.

.Neon
  Stores origin, lineage, claim state, policy attachment, and continuity traversal.
```

## Target Unified Shape

```text
Unified Artifact
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

## Integration Rule

Sun_Tan should connect the systems through contracts and packets, not by copying code from one repo into another.

## First Unified Flow

```text
1. Loop produces an artifact.
2. Sun_Tan hashes the artifact.
3. Sun_Tan creates a bridge packet.
4. Sun_Tan verifies the packet.
5. .Neon imports the verified packet as an origin/lineage claim.
6. Future tools traverse the combined Loop + .Neon continuity chain.
```

## Boundary Rule

Do not let any repo absorb the others.

```text
Loop thinks.
Sun_Tan translates.
.NeoN remembers.
```

## Next Build Requirements

- Add bridge packet schema.
- Add adapter interfaces for Loop and .Neon.
- Add trusted fixture generator.
- Add packet verification tests.
- Add CI validation.
- Add import/export examples.
