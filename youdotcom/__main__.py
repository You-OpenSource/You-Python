# type: ignore[attr-defined]
from typing import Optional

import sys
from enum import Enum
from importlib import metadata as importlib_metadata
from random import choice

import ascii_magic
import requests
import typer
from colorama import Fore
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


def logo() -> None:
    """Print the version of the package."""
    console.print(f"╭──────────────────────────────────────────────────────────────╮")
    try:
        my_art = ascii_magic.from_url("https://github.com/SilkePilon/youdotcom/raw/main/youdotcom.png?raw=true", columns=27, width_ratio=2.2)
    except OSError as e:
        print(f"Could not load the image, server said: {e.code} {e.msg}")
    my_art = my_art.split("\n")
    index = 0
    for line in my_art:
        line = line.replace("\n", "")
        if index == 3:
            print(f"{Fore.RESET}| " + line + f"{Fore.RESET}     YouDotCom - {version}")
        if index == 5:
            print(f"{Fore.RESET}| " + line + f"{Fore.RESET}  Made by Silke Pilon on GitHub")
        else:
            print(f"{Fore.RESET}| " + line)
        index += 1
    console.print(f"╰──────────────────────────────────────────────────────────────╯")
    raise typer.Exit()


def exampleprint() -> None:
    """Print the version of the package."""
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
    logo: bool = typer.Option(
        None,
        "-icon",
        "-logo",
        "--logo",
        callback=logo,
        is_eager=True,
        help="Prints the nice logo of YouDotCom",
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

# hi
