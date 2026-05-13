# COMMAND_INTEGRATION_v0.2

## Purpose

Define the first command-level integration surface for the unified product spine:

```text
Loop export
→ Sun_Tan verify/import/export
→ .Neon import
```

This document does not require Loop or `.Neon` to import Sun_Tan code directly. It defines the command contracts each organ can implement independently.

---

# Command Contract

## Loop command target

```bash
loop export-suntan <artifact> --out <packet.json>
```

Expected behavior:

1. Loop produces or selects an artifact.
2. Loop calls Sun_Tan-compatible packet generation or emits the artifact for Sun_Tan.
3. Output is a Sun_Tan bridge packet with `source_system = project-512d`.

Equivalent current Sun_Tan command:

```bash
suntan export-loop <artifact> --out <packet.json>
```

---

## Sun_Tan command target

```bash
suntan verify <packet.json> --artifact <artifact>
suntan export-neon <packet.json> --artifact <artifact> --out <origin.origin.json>
```

Expected behavior:

1. Verify packet shape.
2. Verify packet hash.
3. Verify local deterministic signature.
4. Verify artifact hash if artifact is supplied.
5. Refuse `.Neon` export if verification fails.

---

## .Neon command target

```bash
neon import-suntan <origin.origin.json>
```

Expected behavior:

1. Accept a verified Sun_Tan-origin claim export.
2. Preserve artifact hash.
3. Preserve bridge payload hash.
4. Preserve bridge signature.
5. Attach policy, lineage, and optional pulse hash.
6. Promote to `.Neon` continuity storage only after local validation.

Equivalent current Sun_Tan command:

```bash
suntan export-neon <packet.json> --artifact <artifact> --out <origin.origin.json>
```

---

# v0.2 Rule

Command-level integration must preserve the v0.1 invariant:

```text
verify before update
```

A command may prepare files, packets, and claims.

A command must not promote continuity state before verification passes.
