from typing import Any, TypedDict

import yaml


class Cache(TypedDict, total=False):
    config: dict[str, Any]


CACHE: Cache = {}


def get_config() -> dict[str, Any]:
    if "config" not in CACHE:
        with open("var/config.yml", encoding="utf-8") as inp:
            config = yaml.safe_load(inp)
        CACHE["config"] = config
    return CACHE["config"]
