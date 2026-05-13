# Sun_Tan v0.1-alpha

## Release Marker

This file marks the first green functional bridge slice.

Base green commit:

```text
6bf442dbebad496951a957ee48099f5ee9ca1a60
Make CLI subprocess tests src-layout safe
```

## Status

```text
Sun_Tan v0.1-alpha demo slice: GREEN
```

## What Exists

- Deterministic bridge packet builder
- Packet verifier
- Artifact hash verification
- Local deterministic signature helper
- `.Neon` origin claim adapter
- Loop / project-512d adapter boundary
- Pulse event recorder
- Trusted fixture generator
- CLI commands:
  - `suntan claim`
  - `suntan verify`
  - `suntan to-neon`
  - `suntan fixture`
- Full bridge demo docs
- GitHub Actions CI

## Product Spine

```text
Loop / project-512d
  produces intelligence artifacts and proofs

Sun_Tan
  translates and verifies artifact packets

.Neon
  receives continuity-compatible origin claims
```

## Release Rule

This is not the final product.

This is the first working bridge spine.

Future work should preserve:

```text
Infinite product surface.
Finite contracts.
Verified exchanges.
Replaceable kernels.
```
