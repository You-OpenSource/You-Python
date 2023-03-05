
<h1 align="center">
  <br>
  <a href="https://github.com/SilkePilon/youdotcom/"><img src="https://github.com/SilkePilon/youdotcom/blob/main/youdotcom.png?raw=true" alt="YouDotCom" width="200"></a>
  <br>
  <br>
  YouDotCom for python v2.0.23
  <br>
</h1>

<h4 align="center">An python library for <a href="http://you.com/" target="_blank">you.com</a> and all of its apps.</h4>

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
  <a href="#how-to-install">Install</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<!-- ![screenshot](https://raw.githubusercontent.com/SilkePilon/youdotcom/main/assets/images/YouDotCom.jpg) -->

## About
Welcome to the YouDotCom Python Library!

This library allows users to easily access and utilize all of the functionality of the You.com platform through a simple and intuitive Python interface. With the library, users can access a variety of You.com apps and services, including but not limited to:

* Search
* YouChat
* YouCode
* YouWrite

To get started with the YouDotCom Python Library, simply <a href="#install">install</a> the package using pip and import it into your Python script. From there, you can use the provided functions and classes to easily interact with the You.com platform.

We hope you enjoy using the YouDotCom Python Library and all of the features it has to offer!
> by Chat GPT


## Key Features
* Bypass CloudFlare
* Interact with YouChat
* Find code examples
* Server ready
  - Supports non-gui operating systems.
* Cross platform
  - Windows, macOS and Linux ready.


## How to install

To install the YouDotCom Python Library, use the following command:

```
pip install youdotcom
```
This will install the latest version of the youdotcom package. Always make sure to be up-to-date so you don't miss any features, use:

```
pip install youdotcom --upgrade
```

Once the installation is complete, you can use the youdotcom package in your Python scripts by importing it:

```python
import youdotcom
```


## How To Use

To help users get started with the YouDotCom Python Library, we have provided a selection of code examples that demonstrate common use cases for the library. These examples can be found below and cover a range of functionality.

To use the code examples, simply copy and paste the relevant code into your Python script and customize it to fit your specific needs. You can also use the examples as a starting point for your own code, using them as a guide to understand how the library functions can be used to build your own applications and integrations with the You.com platform.

We hope that these code examples will make it easier for users to get up and running with the YouDotCom Python Library and start building with the You.com platform.
> :warning: **Warning!**
> Do not spam or harm the you.com servers in any way!


<details>
<summary>YouChat example</summary>
<br>
<h1 align="center">
  <br>
  <a href="https://github.com/SilkePilon/youdotcom/"><img src="https://github.com/You-OpenSource/You-Python/blob/main/assets/images/YouChat.png?raw=true" alt="YouChat" width="200"></a>
  <br>
</h1>


> **Note**
> YouChat is currently disabled because you.com does not yet support the trafic.


```python
from youdotcom import Chat # import all the classes

chat = Chat.send_message(message="how is your day?", api_key="YOUR API KEY HERE") # send a message to YouChat. passing the message and your api key.

# you can get an api key form the site: https://api.betterapi.net/ (with is also made by me)

print(chat)  # returns the message and some other data
```


#### Context
> **Note**
> at the moment there is no context support YET. becuase of new api.
  
 
> **Note**
> Your context will not always be used in the response message is is not a code bug but a YouChat thing. Note its still in beta
  
YouDotCom's YouChat feature is a powerful tool that allows for context to be utilized in your conversations. By passing a list or a file in the JSON format, you can provide the chatbot with additional information to better understand and respond to your questions.

To use the context option, you can change the way you send your message by changing the `Chat.send_message` method. This method allows you to pass in a driver, a message, and a context_form_file or a context parameter.

For example, if you want to use a file, you can pass the file name as the `context_form_file` parameter, like this:
  
```python
Chat.send_message(driver=driver, message="YOUR QUESTION HERE", context_form_file="FILE_NAME.json")
```
  
Make sure to change the `FILE_NAME` to the name of the file you are using and include a question in the `message` parameter.

Alternatively, you can also use the context directly without a file by passing in a list as the `context` parameter. Like this:
  
```python
Chat.send_message(driver=driver, message="YOUR QUESTION HERE", context=['context #1', '#2', 'etc...'])
```

By providing context to your conversations, you can expect more accurate and personalized responses from YouChat, which can help to improve your overall experience.

The following is an example of a JSON file that can be used as the `context_form_file` parameter in the `Chat.send_message` method:

```json
{  
    "context": [ 
        "my name is test",
        "i love coding",
        "my hobby's are making pictures in nature"
    ]  
}  
```

In this example, the `context` field contains an array of strings that provide additional information about the user. The strings can include any relevant information that could help the chatbot understand the context of the conversation.

  
</details>

<details>
<summary>YouCode example</summary>
<br>

<h1 align="center">
  <br>
  <a href="https://github.com/SilkePilon/youdotcom/"><img src="https://cdn.you.com/img/app-icons/icon-youcode.svg" alt="YouCode" width="200"></a>
  <br>
</h1>



#### Find code

  
```python
from youdotcom import Webdriver, Code # import all the classes

driver = Webdriver().driver # setting up the webdriver. use `webdriver_path=` if the pre-installed one does not work.

code = Code.find_code(driver, search="how to make an python loop?") # get all the code displayed on screen. passing the driver and search string.

for string in code['response']: # loop through all the code
    print(string) # print 1 at an time.
    
print(code['time']) # print the time taken to complete you search.
```
  
This code imports the Code and Webdriver classes from the youdotcom library. The Code class is used to search for code snippets, while the Webdriver class is used to set up a webdriver.

First, the Webdriver class is instantiated with Webdriver(). The driver attribute of the resulting object is then stored in the driver variable. The driver attribute returns a webdriver object that can be used to automate web browsing tasks.

Next, the find_code method of the Code class is called with driver and a search string as arguments. This method searches for code snippets related to the specified search string using the webdriver. The result of the method call is stored in the code variable.

The code variable is a dictionary containing a list of code snippets in the response field and the time taken to complete the search in the time field. The code then loops through the response list and prints each code snippet to the console one at a time. Finally, the time taken to complete the search is printed to the console.
  
---
  
#### Generate code
  
> **Note**
> Code complete has an daily limit of 20 requests.

```python
from youdotcom import Code # import the write class 

text = Code.gen_code("python loop") # make an api call

print(text['response']) # print the AI made code

print(text['time']) # print total time taken to complete your request
```
  
This code imports the Code class from the youdotcom module. It then calls the gen_code method of the Code class, passing in the string "python loop" as an argument. The gen_code method makes an API call and returns a dictionary with two keys: response and time. The code then prints the value associated with the response key, which is the AI-generated code. It also prints the value associated with the time key, which is the total time taken to complete the request.
  
</details>

<details>
<summary>Search example</summary>
<br>
  
```python
from youdotcom import Search # import the Search class

search_results = Search.search_for("how to make an python loop?") # search! No need to use the Webdriver class.

print(search_results['results']) # print all the search results

print(search_results['time']) # print the total time taken (les then 3 seconds on average)
```
  
This code imports the Search class from the youdotcom module. It then calls the search_for method of the Search class, passing in the string "how to make an python loop?" as an argument. The search_for method returns a dictionary with two keys: results and time. The code then prints the value associated with the results key, which is a list of search results. It also prints the value associated with the time key, which is the total time taken to perform the search.
  
</details>

<details>
<summary>YouWrite example</summary>
<br>
  
  
<h1 align="center">
  <br>
  <a href="https://github.com/SilkePilon/youdotcom/"><img src="https://cdn.you.com/img/app-icons/icon-youwrite.svg" alt="YouCode" width="200"></a>
  <br>
</h1>
  
> **Note**
> YouWrite has an daily limit of 10 requests.
  
```python
from youdotcom import Write # import the write class 

text = Write.write("how to write well?") # make an api call

print(text['response']) # print the AI made text

print(text['time']) # print total time taken to complete your request
```
  
This code imports the Write class from the youdotcom module. It then calls the write method of the Write class, passing in the string "how to write well?" as an argument. The write method makes an API call and returns a dictionary with two keys: response and time. The code then prints the value associated with the response key, which is a text generated by an AI. It also prints the value associated with the time key, which is the total time taken to complete the request.
  
</details>

> **Note**
> YouDotCom is in Alpha and there will be bugs!


## Interactive shell
The YouDotCom python library offers a wide range of functionality to its users, and one of the ways in which users can access and utilize this functionality is through an interactive terminal shell. With the interactive shell, users are able to execute commands and manipulate the library in real-time, allowing for a more flexible and dynamic experience.

to use the interactive shell, use the following command in your terminal:

```
youdotcom
```

you will get something like this:

```bash
Welcome to YouShell an interactive shell for all YouDotCom commands
Enter 'help' for a list of available commands.
Type 'exit' to stop.


YouShell >
```

> **Note**
> You may sometimes get the following error message: 
> ```
> Detected a Cloudflare version 2 Captcha challenge, This feature is not available in the opensource (free) version.
> ```





## API

> **Note**
> The request limit is 15 per minute.

Welcome to the YouDotCom Python library! Our library now features an easy-to-use public API that allows you to interact with YouChat. With this API, you can easily integrate YouChat into your own projects and applications, providing a convenient and user-friendly way for you to access and utilize the capabilities of the chat bot.

To get started, you will first need to get an API key on our [website](https://betterapi.net/). This key will be required to authenticate each API request.

base url: `api.betterapi.net`

To send a message to YouChat and receive a JSON response, you can make an HTTP GET request to the endpoint `/youdotcom/chat`, including the message to be sent as a query parameter. The key is `message` and the value should be the message text encoded in URL format. For example, to send the message `hello there`, the endpoint would be `https://api.betterapi.net/youdotcom/chat?message=hello%20there&key=YOUR_API_KEY`. The JSON response will include the message sent by YouChat, time, v2Captcha, and type of the request.

You also need to set your API key, you can do this by providing it as an parameter like this `/youdotcom/chat?message=hello%20there&key=YOUR_API_KEY`


auto updating docs can be found at: https://betterapi.net/redoc

Make sure to include the API key in the url of each request to authenticate it.

We are constantly improving and updating the YouDotCom library and API, so make sure to check back for new features and updates. If you have any questions or need assistance, feel free to reach out in the Discusions tab. I'm always happy to help.

## Discord bot
```python
from typing import Optional

import discord
from discord import app_commands


MY_GUILD = discord.Object(id=0)  # replace with your guild id


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)
betterapi_token = "YOUR API KEY HERE"

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
@app_commands.describe(message='The message to YouChat')
async def joined(interaction: discord.Interaction, message:str = "hi there"):
    """Send a message to YouChat"""
    await interaction.response.defer()
    data = requests.get(f"https://api.betterapi.net/youdotcom/chat?message={message}&key={betterapi_token}").json()
    try: 
        msg = data['message']
    except:
        msg = "got an error!"
    await interaction.followup.send(f"{msg}")

client.run('token')
```


## YouDotCom roadmap
* [x] add youchat
* [x] add youcode
* [ ] swith to using you.com/api
* [ ] make code faster
* [ ] add code translate 
* [ ] add all of you.com apps




## YouDotCom projects!
- [telegram bot](https://github.com/samezarus/you_telegram_bot)



## Discord
In addition to the YouDotCom Python Library, we also have an active [Discord server](https://discord.gg/SD7wZMFSvV) where you can chat with developers and get help with using the library. Our Discord community is a great place to ask questions, share your projects, and get feedback from other developers.


## Credits

This software uses the following open source packages:

- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)


## License

MIT

---
