import json
from typing import Any


def canonical_json(data: Any) -> str:
    """Return deterministic JSON serialization."""
    return json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
