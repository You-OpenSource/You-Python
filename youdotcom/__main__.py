# type: ignore[attr-defined]
from typing import Optional

import glob
import os
import pathlib
import subprocess
import sys
import time
from enum import Enum
from importlib import metadata as importlib_metadata
from random import choice

import click
import requests
import typer
from click_shell import make_click_shell, shell
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

    print(search_results["results"]["mainline"]["third_party_search_results"])  # print all the search results

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
@click.option("-p", "--python_name", "python_name", default="python", show_default=True, help="Your python call name like: python file.py")
@click.option("-ip", "--input", "ip", default="0.0.0.0", show_default=True, help="IP used for hosting")
@click.option("-port", "--input", "port", default="80", show_default=True, help="Port on with the server is running")
def host(python_name, ip, port):
    print(f"[API] - PYTHON: {python_name}")
    print(f"[API] - IP: {ip}")
    print(f"[API] - PORT: {port}")
    p = subprocess.check_output(["pip", "show", "youdotcom"])
    out = p.decode("utf-8")

    data = out.split("\n")
    for line in data:
        if line.startswith("Location: "):

            path = str(line[10:])
            if "\\" in path:
                use_key = "\\"
            if "/" in path:
                use_key = "/"
            path1 = f"{path}{use_key}youdotcom{use_key}api_1.py"
            path2 = f"{path}{use_key}youdotcom{use_key}api_2.py"

    print(f"[API] - Starting...")

    api = subprocess.Popen([f"{python_name}", f"{path1}", f"{ip}", f"{port}"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    backend = subprocess.Popen([f"{python_name}", f"{path2}"])
    # api.terminate()
    # backend.terminate()


@app.command()
def chat():

    inputstr = input("Enter a message: ")
    webdriver = input("Enter webdriver_path (press enter for none): ")
    print("Please wait...")
    from youdotcom import Chat, Webdriver

    if webdriver:

        chat = Chat.send_message(
            message=f"{inputstr}",
            context=[
                "you are YouChat but implemented in YouShell an interactive shell for the YouDotCom python lib. Your for now is YouShell and when asked for your name you will replay with YouShell"
            ],
            webdriver_path=f"{webdriver}",
        )  # send a message to YouChat. passing the driver and messages
    else:
        chat = Chat.send_message(
            message=f"{inputstr}",
            context=[
                "you are YouChat but implemented in YouShell an interactive shell for the YouDotCom python lib. Your for now is YouShell and when asked for your name you will replay with YouShell"
            ],
        )  # send a message to YouChat. passing the driver and messages

    print(chat["message"])  # {'message': "It's been great! How about yours?", 'time': '11', 'error': 'False'}
    print(chat["time"])


@app.command()
def clear():
    try:
        os.system("clear")
    except:
        os.system("cls")


if __name__ == "__main__":
    app()
