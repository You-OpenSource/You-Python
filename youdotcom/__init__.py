# type: ignore[attr-defined]
"""unofficial api wrapper for you.com and all of its apps"""

import sys
from importlib import metadata as importlib_metadata

from .apps import Apps
from .code import Code
from .imagine import Imagine
from .init import Init as Webdriver
from .search import Search
from .write import Write
from .youchat import Chat

# from .api import Api
# form .backend import Backend


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


# __all__ = ["YouDotCom"]
