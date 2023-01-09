# type: ignore[attr-defined]
from typing import Optional

import os
import sys
import time
from enum import Enum
from importlib import metadata as importlib_metadata
from random import choice

import ascii_magic
import requests
import typer
from click_shell import shell
from colorama import Fore
from rich.console import Console

import youdotcom

# from youdotcom import version


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


@shell(prompt="YouShell > ", intro="Welcome to the YouShell an interactive shell for all YouDotCom commands\nEnter 'help' for a list of available commands.\nType 'exit' to stop.")
def YouShell():
    pass


@YouShell.command()
def Code():

    from youdotcom import Code  # import the write class

    inputstr = input("Enter a code completion prompt: ")
    print("Please wait...")
    text = Code.gen_code(f"{inputstr}")  # make an api call

    print(text["response"])  # print the AI made code

    print("Total time taken: " + text["time"])  # print total time taken to complete your request


@YouShell.command()
def search():

    from youdotcom import Search  # import the Search class

    inputstr = input("Enter a search prompt: ")
    print("Please wait...")
    search_results = Search.search_for(f"{inputstr}")  # search! No need to use the Webdriver class.

    print(search_results["results"]["mainline"]["bing_search_results"])  # print all the search results

    print("Total time taken: " + search_results["time"])  # print total time taken to complete your request


@YouShell.command()
def write():
    from youdotcom import Write  # import the write class

    inputstr = input("Enter a prompt: ")
    print("Please wait...")
    text = Write.write(f"{inputstr}")  # make an api call

    print(text["response"])  # print the AI made text

    print("Total time taken: " + text["time"])


if __name__ == "__main__":
    YouShell()
