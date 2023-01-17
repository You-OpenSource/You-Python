from youchat import Chat

from youdotcom import Webdriver

driver = Webdriver(webdriver_path="/usr/bin/chromedriver", hide=True).driver  # setting up the webdriver. use `webdriver_path=` if the pre-installed one does not work.


chat = Chat.send_message(driver=driver, message="how to make an python loop?")  # send a message to YouChat. passing the driver and messages

driver.close()  # close the webdriver


print(chat["message"])  # {'message': "It's been great! How about yours?", 'time': '11', 'error': 'False'}
