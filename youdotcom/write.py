import asyncio
import json
import os
import platform
import re
import time

import cloudscraper
import markdownify
import undetected_chromedriver as uc
import urllib3
from pyvirtualdisplay import Display
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

urllib3.disable_warnings()


class Write:
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

    def write(message: str) -> dict:
        """
        Search on You.com\n
        Parameters:
        - message: The message you want to send\n
        Returns a `dict` with the following keys:
        - all the data!
        """
        start = time.time()
        scraper = cloudscraper.create_scraper()
        json_data = {
            "use_case": "essay",
            "tone": "",
            "audience": "",
            "message": f"{message}",
        }
        msg = scraper.post("https://you.com/api/copywrite", json=json_data).text
        msg = json.loads(msg)
        msg = msg["text"]
        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))
        return {"response": msg, "time": str(timedate)}
