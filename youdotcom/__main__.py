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
def chat():

    inputstr = input("Enter a message: ")
    webdriver = input("Enter webdriver_path (press enter for none): ")
    print("Please wait...")
    from youdotcom import Chat, Webdriver

    if webdriver:
        driver = Webdriver(webdriver_path=f"{webdriver}", hide=True).driver  # setting up the webdriver. use `webdriver_path=` if the pre-installed one does not work.
    else:
        driver = Webdriver(hide=True).driver  # setting up the webdriver. use `webdriver_path=` if the pre-installed one does not work.
    chat = Chat.send_message(
        driver=driver,
        message=f"{inputstr}",
        context=["you are YouChat but implemented in YouShell an interactive shell for the YouDotCom python lib. Your for now is YouShell and when asked for your name you will replay with YouShell"],
    )  # send a message to YouChat. passing the driver and messages

    driver.close()

    print(chat["message"])  # {'message': "It's been great! How about yours?", 'time': '11', 'error': 'False'}
    print(chat["time"])


@app.command()
def clear():
    try:
        os.system("clear")
    except:
        os.system("cls")


@app.command()
def exit():
    exit()


@app.command()
def quit():
    quit()


if __name__ == "__main__":
    app()
