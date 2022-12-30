from youdotcom.youchat import Chat

chat = Chat()  # you can also specify a chrome webdriver if the pre-installed one does not work using 'webdriver_path='

response = chat.send_message(message="what is the time?")  # returns a json string with the message and time it took to complete

print(response["message"])  # returns only the message of the response
