import asyncio
import json
import os
import platform
import re
import time

import chromedriver_autoinstaller
import cloudscraper
import markdownify
import undetected_chromedriver as uc
import urllib3
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

urllib3.disable_warnings()


class Code:
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

    def find_code(driver, search: str) -> dict:

        """
        Send a message to YouChat\n
        Parameters:
        - message: The message you want to send\n
        - driver: pass the driver form the Init variable\n
        Returns a `dict` with the following keys:
        - message: The response from YouChat\n
        - time: the time it took to complete your request
        """
        start = time.time()
        # Ensure that the Cloudflare cookies is still valid

        driver.get("https://you.com/search?q=" + search + "&tbm=youcode")

        # Send the message

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "main")))
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@data-eventactiontitle="Copy Button"]')))
        # Get the response element

        response = driver.find_elements(By.XPATH, '//*[@data-eventactiontitle="Copy Button"]')

        # Check if the response is an error

        # Return the response

        # msg = markdownify.markdownify(response.text)

        # type(headers) == str

        # while True:
        #     try:
        #         if WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "flex-1 text-ellipsis max-h-5 overflow-hidden break-all relative"), "New Chat")):
        #             text = driver.find_elements(
        #                 By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/nav/div/div/a[1]/div[1]'
        #             )[-1].text
        #             break
        #     except:
        #         continue

        msg = []
        for code in response:
            msg.append(str(code.get_attribute("data-eventactioncontent")))
        msg = list(dict.fromkeys(msg))
        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))
        return {"response": msg, "time": str(timedate)}

    def gen_code(message: str) -> dict:
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
            "engine": "cushman-codex",
            "prompt": f"{message}",
            "get_rate_limit": False,
            "temperature": 0.35,
            "max_tokens": 512,
            "top_p": 1,
            "best_of": 3,
            "frequency_penalty": 0.8,
            "presence_penalty": 0.8,
            "stop": [
                "\\n",
            ],
            "version": 2,
        }
        msg = scraper.post("https://you.com/api/codex", json=json_data).text
        msg = json.loads(msg)
        msg = msg["text"]
        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))
        return {"response": msg, "time": str(timedate)}
