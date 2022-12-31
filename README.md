
<h1 align="center">
  <br>
  <a href="https://github.com/SilkePilon/youdotcom/"><img src="https://github.com/SilkePilon/youdotcom/blob/main/youdotcom.png?raw=true" alt="Markdownify" width="200"></a>
  <br>
  YouDotCom for python
  <br>
</h1>

<h4 align="center">An unofficial python library wrapper for <a href="http://you.com/" target="_blank">you.com</a> and all of its apps.</h4>

<div align="center">

  [![Python Version](https://img.shields.io/pypi/pyversions/youdotcom.svg)](https://pypi.org/project/youdotcom/)
  [![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/silkepilon/youdotcom/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
  [![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
  [![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/silkepilon/youdotcom/blob/master/.pre-commit-config.yaml)
  [![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/silkepilon/youdotcom/releases)
  [![License](https://img.shields.io/github/license/silkepilon/youdotcom)](https://github.com/silkepilon/youdotcom/blob/master/LICENSE)
  ![Coverage Report](assets/images/coverage.svg)
  
</div>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#install">Install</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://raw.githubusercontent.com/SilkePilon/youdotcom/main/assets/images/YouDotCom.jpg)

## Key Features
* Bypass CloudFlare
* Server ready
  - Supports non-gui operating systems.
* Cross platform
  - Windows, macOS and Linux ready.

## How To Use

First you need to <a href="#install">Install</a> YouDotCom, then as example code for YouChat:
> **Warning!**
> Do not spam or harm the you.com servers in any way!

```python
from youdotcom.init import Init  # import the Init class
from youdotcom.youchat import Chat  # import YouChat

driver = Init().driver  # setting up the webdriver. use `webdriver_path=` if the pre-installed one does not work.


chat = Chat.send_message(driver=driver, message="how is your day?")  # send a message to YouChat. passing the driver and messages

driver.close()  # close the webdriver


print(chat)  # {'message': "It's been great! How about yours?", 'time': '11', 'error': 'False'}
```
or use:

```youdotcom -example```

> **Note**
> YouDotCom is in Alpha and there will be bugs!


## install

```pip install youdotcom --upgrade```

## Discord

YouDotCom also has an official [discord server](https://discord.gg/SD7wZMFSvV), chat and help developers with there projects!

## Credits

This software uses the following open source packages:

- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)


## License

MIT

---


