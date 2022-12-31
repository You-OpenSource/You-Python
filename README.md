
<h1 align="center">
  <br>
  <a href="https://github.com/SilkePilon/youdotcom/"><img src="https://github.com/SilkePilon/youdotcom/blob/main/youdotcom.png?raw=true" alt="Markdownify" width="200"></a>
  <br>
  YouDotCom for python
  <br>
</h1>

<h4 align="center">An unofficial python library wrapper for <a href="http://you.com/" target="_blank">you.com</a> and all of its apps.</h4>

<div align="center">

  [![Build status](https://github.com/silkepilon/youdotcom/workflows/build/badge.svg?branch=master&event=push)](https://github.com/silkepilon/youdotcom/actions?query=workflow%3Abuild)
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

![screenshot](https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.gif)

## Key Features
* Bypass CloudFlare
* Server ready
  - Supports non-gui operating systems.
* Cross platform
  - Windows, macOS and Linux ready.

## How To Use

First you need to <a href="#install">Install</a> YouDotCom, then as example code for YouChat:

```python
from youdotcom.init import Init  # import the Init class
from youdotcom.youchat import Chat  # import YouChat

driver = Init().driver  # setting up the webdriver. use `webdriver_path=` if the pre-installed one does not work.


chat = Chat.send_message(driver=driver, message="what is the time?")  # send a message to YouChat. passing the driver and messages

driver.close()  # close the webdriver


print(chat)  # {'message': 'The current time is Saturday, December 31, 2022 09:47:30 UTC.', 'time': '25'}
```
or use:

```youdotcom -example```

> **Note**
> If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.


## install

```pip install youdotcom --upgrade```

## Discord

YouDotCom also has an official [discord server](https://discord.gg/SD7wZMFSvV), chat and help developers with there projects!

## Credits

This software uses the following open source packages:

- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

## Related

[markdownify-web](https://github.com/amitmerchant1990/markdownify-web) - Web version of Markdownify

## Support

<a href="https://www.buymeacoffee.com/5Zn8Xh3l9" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p> 

<a href="https://www.patreon.com/amitmerchant">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## You may also like...

- [Pomolectron](https://github.com/amitmerchant1990/pomolectron) - A pomodoro app
- [Correo](https://github.com/amitmerchant1990/correo) - A menubar/taskbar Gmail App for Windows and macOS

## License

MIT

---

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant)

