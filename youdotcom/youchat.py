import asyncio
import json
import os
import platform
import re
import time
import urllib.parse

import chromedriver_autoinstaller
import cloudscraper
import markdownify
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
    def send_message(driver, message: str, context=None, context_form_file=None) -> dict:

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
        if context_form_file:

            with open(context_form_file) as F:
                textjson = json.load(F)
                context = textjson["context"]

            message = str(message).replace(" ", "%20")
            totalcontext = "["
            for item in context:
                print(item)
                item = str(item)
                totalcontext += '{"question":"' + item + '","answer":" "},'
            totalcontext += "]"
            totalcontext = str(totalcontext).replace(" ", "%20")

            print(f"https://you.com/api/youchatStreaming?question={message}&chat={totalcontext}")
            driver.get(f"https://you.com/api/youchatStreaming?question={message}&chat={totalcontext}")
        if context and context_form_file == None:
            message = str(message).replace(" ", "%20")
            totalcontext = "["
            for item in context:
                print(item)
                totalcontext += '{"question":"' + item + '","answer":" "},'
            totalcontext += "]"
            totalcontext = str(totalcontext).replace(" ", "%20")

            print(f"https://you.com/api/youchatStreaming?question={message}&chat={totalcontext}")
            driver.get(f"https://you.com/api/youchatStreaming?question={message}&chat={totalcontext}")
        if not context and not context_form_file:
            message = urllib.parse.quote(message)
            print(f"https://you.com/api/youchatStreaming?question={message}&chat=[dwadwadwa]")
            driver.get(f"https://you.com/api/youchatStreaming?question={message}&chat=[]")

        try:
            textdatastr = (
                str(
                    driver.page_source.replace("event: token", "")
                    .replace('data: {"token": "', "")
                    .replace('<html><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">event: serp_results', "")
                    .replace("</pre></body></html>", "")
                    .replace("\n", "")
                    .replace('"}', "")
                )
                .replace("event: donedata: I'm Mr. Meeseeks. Look at me.", "")
                .split("]} ", 1)[1]
            )
        except:
            textdatastr = "error"

        msg = markdownify.markdownify(textdatastr)

        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))
        if "Oops, I’m still learning and I couldn’t generate an answer right now. Please try again." in msg:
            error = True
        else:
            error = False
        return {"message": msg, "time": str(timedate), "error": str(error)}
