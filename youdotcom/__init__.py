# type: ignore[attr-defined]
"""unofficial api wrapper for you.com and all of its apps"""

import sys
from importlib import metadata as importlib_metadata

from .apps import Apps

# from .youchat import Chat
from .code import Code
from .init import Init
from .search import Search


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


__all__ = ["YouDotCom"]
