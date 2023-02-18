import asyncio
import json
import os
import platform
import re
import subprocess
import time
import urllib.parse

import chromedriver_autoinstaller
import cloudscraper
import markdownify
import requests
import undetected_chromedriver as uc
import urllib3
from pyvirtualdisplay import Display
from ratelimit import limits
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

urllib3.disable_warnings()


class Chat:
    """
    An unofficial Python wrapper for YOU.com YOUCHAT
    """

    # def __init__(
    #     self,
    #     verbose: bool = False,
    #     window_size: tuple = (800, 600),
    #     driver: object = None,
    # ) -> None:

    #     self.__verbose = verbose
    #     self.__driver = driver
    @limits(calls=6, period=100)
    def send_message(message: str, context=None, context_form_file=None, debug=False, webdriver_path=None, headless=True, keep=False, api_key: str = str(os.environ.get("BETTERAPI_API_KEY"))):

        """
        Send a message to YouChat\n
        Parameters:
        - message: The message you want to send\n
        - driver: pass the driver form the Init variable\n
        Returns a `json string` with the following keys:
        - message: The response from YouChat\n
        - time: the time it took to complete your request\n
        - some other data for issues reporting.
        """
        if api_key == "" or None:
            raise ValueError("Chat.api_key must be set before making a request. Don't have an api key? get one on https://api.betterapi.net/")
        data = requests.get(f"https://api.betterapi.net/youdotcom/chat?message={message}&key={api_key}").json()
        return data
