import asyncio
import json
import os
import platform
import re
import shutil
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


class Imagine:
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

    def Imagine(message: str) -> dict:
        """
        Search on You.com\n
        Parameters:
        - message: The message you want to send\n
        Returns a `dict` with the following keys:
        - all the data!
        """
        start = time.time()
        scraper = cloudscraper.create_scraper()
        data = '{"url":"api/stableDiffusion","headers":{},"data":{"prompt":"' + message + '"},"appName":"stable_diffusion"}'
        msg = scraper.get("https://you.com/api/template_api", data=data, timeout=30).text
        # if "<!DOCTYPE html>" in msg.text:
        #     msg = "error, gateway time-out"
        # else:
        #     msg = "image.png"
        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))
        return {"image_name": msg, "time": str(timedate)}
