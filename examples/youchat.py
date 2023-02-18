from youdotcom.init import Init  # import the Init class
from youdotcom.youchat import Chat  # import YouChat

driver = Init().driver  # setting up the webdriver. use `webdriver_path=` if the pre-installed one does not work.


chat = Chat.send_message(driver=driver, message="what is the time?")  # send a message to YouChat. passing the driver and messages

driver.close()  # close the webdriver


print(chat)  # {'message': 'The current time is Saturday, December 31, 2022 09:47:30 UTC.', 'time': '25'}
