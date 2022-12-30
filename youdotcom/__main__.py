# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import requests
import typer
from rich.console import Console

from youdotcom import version


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="youdotcom",
    help="unofficial api wrapper for you.com and all of its apps",
    add_completion=False,
)
console = Console()


def exampleprint(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        data = requests.get("https://raw.githubusercontent.com/SilkePilon/youdotcom/main/examples/youchat.py")
        console.print(f"status code: {data.status_code}\nCode:\n{data.text}")
        raise typer.Exit()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]youdotcom[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="")
def main(
    example: bool = typer.Option(
        None,
        "-e",
        "--example",
        callback=exampleprint,
        is_eager=True,
        help="Prints the example code.",
    ),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the youdotcom package.",
    ),
) -> None:
    """YouDotCom - unofficial python api wrapper for you.com and all of its apps"""

    console.print(f".")


if __name__ == "__main__":
    app()
