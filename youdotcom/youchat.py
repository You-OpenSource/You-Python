import asyncio
import json
import os
import platform
import re
import time

import chromedriver_autoinstaller
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

    def send_message(driver, message: str) -> dict:

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

        driver.get("https://you.com/search?q=" + message + "&tbm=youchat")

        # Send the message

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
        textbox = driver.find_element(By.TAG_NAME, "textarea")

        # Sending emoji (from https://stackoverflow.com/a/61043442)
        # textbox.click()
        # driver.execute_script(
        #     """
        # var element = arguments[0], txt = arguments[1];
        # element.value += txt;
        # element.dispatchEvent(new Event('change'));
        # """,
        #     textbox,
        #     message,
        # )
        # textbox.send_keys(Keys.ENTER)

        # Wait for the response to be ready

        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="chatHistory"]/div/div[2]/p/p')))

        # Get the response element

        response = driver.find_element(By.XPATH, '//*[@id="chatHistory"]/div/div[2]')

        # Check if the response is an error

        # Return the response
        msg = markdownify.markdownify(response.text)

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
        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))
        if "Oops, I’m still learning and I couldn’t generate an answer right now. Please try again." in msg:
            error = True
        else:
            error = False
        return {"message": msg, "time": str(timedate), "error": str(error)}
