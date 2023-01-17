from youchat import Chat

from youdotcom import Webdriver

driver = Webdriver(webdriver_path="/usr/bin/chromedriver", hide=True).driver


chat = Chat.send_message(driver=driver, message="write an short text about the story", context_form_file="config.json")


driver.close()


print(chat)
