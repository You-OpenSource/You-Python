import asyncio
import json
import os
import platform
import re
import signal
import subprocess
import sys
import threading
import time
import urllib.parse

import aioredis
import cloudscraper
import markdownify
import undetected_chromedriver as uc
import urllib3
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi_queue import QueueWorker
from gtts import gTTS
from loguru import logger
from pyvirtualdisplay import Display
from ratelimit import limits
from selenium.common import exceptions as SeleniumExceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.requests import Request

urllib3.disable_warnings()
import random
import string
import traceback
from io import BytesIO

import requests
from fastapi import Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.responses import PlainTextResponse, RedirectResponse

from youdotcom import Webdriver

proxy_list = {"https": "https://24.106.221.230:53281"}
proxies = {"http": "http://202.164.152.229:8080", "https": "https://202.164.152.229:8080"}
driver = Webdriver(webdriver_path="/usr/bin/chromedriver", hide=True, headless=True).driver
driver.get(
    "https://you.com/api/streamingSearch?q=test&page=1&count=10&safeSearch=Moderate&onShoppingPage=false&mkt=&responseFilter=WebPages,Translations,TimeZone,Computation,RelatedSearches&domain=youchat&queryTraceId=&chat={}&sharedChatId={}"
)
driver.add_cookie({"name": "uuid_guest", "value": "dummystring"})
cookievar = driver.get_cookies()


from typing import Any, Optional

from datetime import datetime

import aioredis
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi_queue import DistributedTaskApplyManager
from pydantic import BaseModel

queueworker = None

scraper = cloudscraper.CloudScraper(browser={"browser": "chrome", "platform": "android", "mobile": True, "desktop": False}, debug=False)
for cookie in cookievar:
    scraper.cookies.set(cookie["name"], cookie["value"])


def sendmessagetochat(redis, mysql, message, contextid, ip, url):
    try:
        with open("logs.txt", "a+") as T:
            datetimestr = datetime.today()
            T.write(f"{ip} @ {datetimestr} @{url}\n")
        start = time.time()
        CloudflareChallengeError = False
        typeof = ""
        if contextid == "" or None:
            contextid = ""

        global chat
        chat = []
        headers = {
            "Accept": "text/event-stream",
            "Connection": "keep-alive",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "Referer": "https://you.com/search?q=hello&fromSearchBar=true&tbm=youchat",
            "Cookie": b"uuid_guest=dummystring;",
        }
        payload = {
            "q": message,
            "chat": "",
            "queryTraceId": "",
            "domain": "youchat",
            "page": "1",
            "count": "10",
            "safeSearch": "Off",
            "onShoppingPage": "false",
            "freshness": "Month",
            "mkt": "",
            "responseFilter": "WebPages,Translations,TimeZone,Computation,RelatedSearches",
            "sharedChatId": f"{contextid}",
        }
        try:
            response = scraper.get(f"https://you.com/api/streamingSearch?sharedChatId={contextid}", params=payload, headers=headers)
            CloudflareChallengeError = False
            typeof = "api"

        except cloudscraper.exceptions.CloudflareChallengeError as e:
            youchatapitimeout = True
            driver.get(
                f"https://you.com/api/streamingSearch?q={message}&page=1&count=10&safeSearch=Moderate&onShoppingPage=false&mkt=&responseFilter=WebPages,Translations,TimeZone,Computation,RelatedSearches&domain=youchat&queryTraceId=&chat={str(chat)}&sharedChatId={contextid}"
            )
            driver.add_cookie({"name": "uuid_guest", "value": "dummystring"})
            CloudflareChallengeError = True
            typeof = "webdriver"
            response = driver.page_source.split("\n")

            contextid

        output = ""
        if CloudflareChallengeError == True:
            for line in response:
                if line:
                    decoded_line = str(line)
                    key, value = decoded_line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    if key == "data":
                        if value == "I'm Mr. Meeseeks. Look at me.":
                            break
                        if value == "undefined":
                            output = "😔 Due to high demand, I'm experiencing issues briefly. Please try again later or use the All tab to get an answer in the meantime."
                            break
                        data = json.loads(value)
                        if "youChatToken" in data:
                            output += data["youChatToken"]
        if CloudflareChallengeError == False:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode("utf-8")
                    key, value = decoded_line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    if key == "data":
                        if value == "I'm Mr. Meeseeks. Look at me.":
                            break
                        if value == "undefined":
                            output = "😔 Due to high demand, I'm experiencing issues briefly. Please try again later or use the All tab to get an answer in the meantime."
                            break
                        data = json.loads(value)
                        if "youChatToken" in data:
                            output += data["youChatToken"]
        if len(chat) > 4:
            chat = chat[:-4]
        out = re.sub(r"\[.+?\]\(.+?\)", "", output[1:])
        timedate = time.time() - start
        timedate = time.strftime("%S", time.gmtime(timedate))

        return {"message": out, "time": str(timedate), "v2Captcha": str(CloudflareChallengeError), "type": str(typeof)}
    except:
        print(traceback.format_exc())


route_table = {
    "/chat": sendmessagetochat,
}

route_table_maximum_concurrency = {
    "/chat": 100,
}


async def main(pid, logger):
    global queueworker

    first_time_run = True
    while True:
        run_startup, first_time_run = (True if pid != 0 else False) and first_time_run, False
        redis = aioredis.Redis.from_url("redis://localhost")
        try:
            worker = QueueWorker(
                redis,
                threads=4,
                route_table_maximum_concurrency=route_table_maximum_concurrency,
                allowed_type_limit=None,
                run_startup=run_startup,
                logger=logger,
            )
            queueworker = worker
            [worker.method_register(name, func) for name, func in route_table.items()]
            await worker.run_serve()
            if worker.closeing():
                break
        except Exception as e:
            debug = True
            if debug:
                raise e
    await redis.close()
    logger.info(f"Pid: {worker.pid}, shutdown")


def sigint_capture(sig, frame):
    if queueworker:
        queueworker.graceful_shutdown(sig, frame)
    else:
        sys.exit(1)


logger.remove()
logger.add(sys.stderr, level="DEBUG", enqueue=True)
signal.signal(signal.SIGINT, sigint_capture)  # In order for the program to capture the `ctrl+c` close signal
for _ in range(3):
    pid = os.fork()
    if pid == 0:
        break
asyncio.run(main(pid, logger))
