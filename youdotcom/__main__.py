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


@shell(prompt="YouShell > ", intro="Welcome to YouShell an interactive shell for all YouDotCom commands\nEnter 'help' for a list of available commands.\nType 'exit' to stop.\n\n")
def app():
    pass


@app.command()
def Code():

    from youdotcom import Code  # import the write class

    inputstr = input("Enter a code completion prompt: ")
    print("Please wait...")
    text = Code.gen_code(f"{inputstr}")  # make an api call

    print(text["response"])  # print the AI made code

    print("Total time taken: " + text["time"])  # print total time taken to complete your request


@app.command()
def search():

    from youdotcom import Search  # import the Search class

    inputstr = input("Enter a search prompt: ")
    print("Please wait...")
    search_results = Search.search_for(f"{inputstr}")  # search! No need to use the Webdriver class.

    print(search_results["results"]["mainline"]["bing_search_results"])  # print all the search results

    print("Total time taken: " + search_results["time"])  # print total time taken to complete your request


@app.command()
def write():
    from youdotcom import Write  # import the write class

    inputstr = input("Enter a prompt: ")
    print("Please wait...")
    text = Write.write(f"{inputstr}")  # make an api call

    print(text["response"])  # print the AI made text

    print("Total time taken: " + text["time"])


@app.command()
def clear():
    try:
        os.system("clear")
    except:
        os.system("cls")


if __name__ == "__main__":
    app()
