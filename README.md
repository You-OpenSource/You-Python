
<h1 align="center">
  <br>
  <a href="https://github.com/SilkePilon/youdotcom/"><img src="https://github.com/SilkePilon/youdotcom/blob/main/youdotcom.png?raw=true" alt="Markdownify" width="200"></a>
  <br>
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
  <a href="#about">About</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#install">Install</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<!-- ![screenshot](https://raw.githubusercontent.com/SilkePilon/youdotcom/main/assets/images/YouDotCom.jpg) -->

## About
Welcome to the YouDotCom Python Library!

This library allows users to easily access and utilize all of the functionality of the You.com platform through a simple and intuitive Python interface. With the library, users can access a variety of You.com apps and services, including but not limited to:

* ~~YouChat~~ (not suppoted yet by the you.com servers)
* YouCode

To get started with the YouDotCom Python Library, simply <a href="#install">install</a> the package using pip and import it into your Python script. From there, you can use the provided functions and classes to easily interact with the You.com platform.

We hope you enjoy using the YouDotCom Python Library and all of the features it has to offer!
> by Chat GPT


## Key Features
* Bypass CloudFlare
* ~~Interact with YouChat~~
* Find code examples
* Server ready
  - Supports non-gui operating systems.
* Cross platform
  - Windows, macOS and Linux ready.

## How To Use

To help users get started with the YouDotCom Python Library, we have provided a selection of code examples that demonstrate common use cases for the library. These examples can be found below and cover a range of functionality.

To use the code examples, simply copy and paste the relevant code into your Python script and customize it to fit your specific needs. You can also use the examples as a starting point for your own code, using them as a guide to understand how the library functions can be used to build your own applications and integrations with the You.com platform.

We hope that these code examples will make it easier for users to get up and running with the YouDotCom Python Library and start building with the You.com platform.
> :warning: **Warning!**
> Do not spam or harm the you.com servers in any way!
<details>
<summary>YouChat example</summary>
<br>

> **Note**
> YouChat is currently disabled because you.com does not yet support the trafic.


```python
from youdotcom import Init, Chat # import all the classes

driver = Init().driver  # setting up the webdriver. use `webdriver_path=` if the pre-installed one does not work.


chat = Chat.send_message(driver=driver, message="how is your day?")  # send a message to YouChat. passing the driver and messages

driver.close()  # close the webdriver


print(chat)  # {'message': "It's been great! How about yours?", 'time': '11', 'error': 'False'}
```

This code imports two classes from the youdotcom library: Init and Chat. The Init class is used to set up a webdriver, which is a tool that allows you to automate web browsing tasks. The Chat class is used to send a message to the YouChat service.

First, the Init class is instantiated with Init(). The driver attribute of the resulting object is then stored in the driver variable. The driver attribute returns a webdriver object that can be used to automate web browsing tasks.

Next, the send_message method of the Chat class is called with driver and a message as arguments. This method sends the specified message to the YouChat service using the webdriver. The result of the method call is stored in the chat variable.

Finally, the webdriver is closed with driver.close(), and the value of chat is printed to the console.
  
</details>

<details>
<summary>YouCode (only code search for now) example</summary>
<br>
  
```python
from youdotcom import Init, Code # import all the classes

driver = Init().driver # setting up the webdriver. use `webdriver_path=` if the pre-installed one does not work.

code = Code.find_code(driver, search="how to make an python loop?") # get all the code displayed on screen. passing the driver and search string.

for string in code['response']: # loop through all the code
    print(string) # print 1 at an time.
    
print(code['time']) # print the time taken to complete you search.
```
  
This code imports the Code and Init classes from the youdotcom library. The Code class is used to search for code snippets, while the Init class is used to set up a webdriver.

First, the Init class is instantiated with Init(). The driver attribute of the resulting object is then stored in the driver variable. The driver attribute returns a webdriver object that can be used to automate web browsing tasks.

Next, the find_code method of the Code class is called with driver and a search string as arguments. This method searches for code snippets related to the specified search string using the webdriver. The result of the method call is stored in the code variable.

The code variable is a dictionary containing a list of code snippets in the response field and the time taken to complete the search in the time field. The code then loops through the response list and prints each code snippet to the console one at a time. Finally, the time taken to complete the search is printed to the console.
  
</details>

or use:

```
youdotcom -example
```

> **Note**
> YouDotCom is in Alpha and there will be bugs!


## install

To install the YouDotCom Python Library, use the following command:

```
pip install youdotcom
```
This will install the latest version of the youdotcom package. To install a specific version, use:

```
pip install youdotcom==0.3.0
```
Once the installation is complete, you can use the youdotcom package in your Python scripts by importing it:

```python
import youdotcom
```

## YouDotCom roadmap
* [x] add youchat
* [x] add youcode
* [ ] swith to using you.com/api
* [ ] make code faster
* [ ] add code translate 
* [ ] add all of you.com apps


## Discord
In addition to the YouDotCom Python Library, we also have an active [Discord server](https://discord.gg/SD7wZMFSvV) where you can chat with developers and get help with using the library. Our Discord community is a great place to ask questions, share your projects, and get feedback from other developers.


## Credits

This software uses the following open source packages:

- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)


## License

MIT

---


