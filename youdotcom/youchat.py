import asyncio
import json
import os
import platform
import re
import time

import chromedriver_autoinstaller
import markdownify
import undetected_chromedriver as uc
from pyvirtualdisplay import Display
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_autoinstaller.install()


class Chat:
    """
    An unofficial Python wrapper for YOU.com YOUCHAT
    """

    def __init__(
        self,
        verbose: bool = False,
        window_size: tuple = (800, 600),
    ) -> None:

        self.__verbose = verbose

        self.__is_headless = platform.system() == "Linux" and "DISPLAY" not in os.environ
        self.__verbose_print("[0] Platform:", platform.system())
        self.__verbose_print("[0] Display:", "DISPLAY" in os.environ)
        self.__verbose_print("[0] Headless:", self.__is_headless)
        self.__init_browser()

    def __del__(self):
        """
        Close the browser and virtual display (if any)
        """
        if hasattr(self, "driver"):
            self.driver.quit()
        if hasattr(self, "display"):
            self.display.stop()

    def __verbose_print(self, *args, **kwargs) -> None:
        """
        Print if verbose is enabled
        """
        if self.__verbose:
            print(*args, **kwargs)

    def __init_browser(self) -> None:

        """
        Initialize the browser
        """
        # Detect if running on a headless server
        if self.__is_headless:
            try:
                self.display = Display()
            except FileNotFoundError as e:
                if "No such file or directory: 'Xvfb'" in str(e):
                    raise ValueError("Headless machine detected. Please install Xvfb to start a virtual display: sudo apt install xvfb")
                raise e
            self.__verbose_print("[init] Starting virtual display")
            self.display.start()

        # Start the browser
        options = uc.ChromeOptions()
        options.add_argument(f"--window-size={800},{600}")
        if self.__proxy:
            options.add_argument(f"--proxy-server={self.__proxy}")
        try:
            self.__verbose_print("[init] Starting browser")
            self.driver = uc.Chrome(options=options, enable_cdp_events=True)
        except TypeError as e:
            if str(e) == "expected str, bytes or os.PathLike object, not NoneType":
                raise ValueError("Chrome installation not found")
            raise e

        # Restore session token

        # Block moderation

        # Ensure that the Cloudflare cookies is still valid
        self.__verbose_print("[init] Ensuring Cloudflare cookies")

        # Open the chat page
        self.__verbose_print("[init] Opening chat page")

        # Dismiss the ChatGPT intro
        self.__verbose_print("[init] Check if there is intro")

    def send_message(self, message: str) -> dict:

        """
        Send a message to the chatbot\n
        Parameters:
        - message: The message you want to send\n
        Returns a `dict` with the following keys:
        - message: The message the chatbot sent
        - conversation_id: The conversation ID
        - parent_id: The parent ID
        """
        # Ensure that the Cloudflare cookies is still valid
        self.__verbose_print("[send_msg] Ensuring Cloudflare cookies")
        self.driver.get("https://you.com/search?q=" + message)

        # Send the message
        self.__verbose_print("[send_msg] Sending message")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
        textbox = self.driver.find_element(By.TAG_NAME, "textarea")

        # Sending emoji (from https://stackoverflow.com/a/61043442)
        textbox.click()
        self.driver.execute_script(
            """
        var element = arguments[0], txt = arguments[1];
        element.value += txt;
        element.dispatchEvent(new Event('change'));
        """,
            textbox,
            message,
        )
        textbox.send_keys(Keys.ENTER)

        # Wait for the response to be ready
        self.__verbose_print("[send_msg] Waiting for completion")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="chatHistory"]/div/div[2]/p/p')))

        # Get the response element
        self.__verbose_print("[send_msg] Finding response element")
        response = self.driver.find_element(By.XPATH, '//*[@id="chatHistory"]/div/div[2]')

        # Check if the response is an error

        # Return the response
        msg = markdownify.markdownify(response.text)

        # type(headers) == str

        # while True:
        #     try:
        #         if WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "flex-1 text-ellipsis max-h-5 overflow-hidden break-all relative"), "New Chat")):
        #             text = self.driver.find_elements(
        #                 By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/nav/div/div/a[1]/div[1]'
        #             )[-1].text
        #             break
        #     except:
        #         continue

        return {"message": msg}

    def reset_conversation(self) -> None:
        """
        Reset the conversation
        """
        self.__verbose_print("Resetting conversation")
        self.driver.find_element(By.LINK_TEXT, "New chat").click()
