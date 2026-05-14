# One-Command Product Spine Runner

## Purpose

Run the full local product spine from one PowerShell command:

```text
Loop / project-512d artifact
→ Loop Sun_Tan packet export
→ Sun_Tan packet verification
→ Sun_Tan .Neon origin claim export
→ .Neon import-suntan
→ receipt check
```

## Prerequisite folder layout

Expected default layout:

```text
C:\Creations\
├── project-512d\
├── Sun_Tan\
└── .Neon\
```

## Command

From the `Sun_Tan` repo:

```powershell
.\scripts\run_product_spine.ps1
```

Custom root:

```powershell
.\scripts\run_product_spine.ps1 -Root "D:\Creations"
```

## What it does

1. Checks all three repos exist.
2. Installs Sun_Tan locally.
3. Runs Sun_Tan tests.
4. Installs `.Neon` locally.
5. Creates a Loop test artifact.
6. Runs `python suntan_export.py` inside `project-512d`.
7. Runs `suntan verify` inside `Sun_Tan`.
8. Runs `suntan export-neon` inside `Sun_Tan`.
9. Runs `neon init` inside `.Neon`.
10. Runs `neon import-suntan` inside `.Neon`.
11. Checks the `.Neon` Sun_Tan import receipt folder.

## Expected success message

```text
SUCCESS: Loop -> Sun_Tan -> .Neon product spine completed.
```

## Meaning

This proves the first local one-product operation:

```text
Loop exports.
Sun_Tan verifies/translates.
.NeoN imports/remembers.
```
