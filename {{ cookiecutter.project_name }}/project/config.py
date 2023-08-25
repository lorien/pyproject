from typing import Any

import yaml

CACHE: dict[str, Any] = {}


def get_config() -> dict[str, Any]:
    if "config" not in CACHE:
        with open("var/config.yml") as inp:
            config = yaml.safe_load(inp)
        CACHE["config"] = config
    return CACHE["config"]
