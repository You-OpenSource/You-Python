from youdotcom.youchat import Chat

chat = Chat()  # starts the webdriver and opens you.com when called

response = chat.send_message(message="what is the time?")  # returns a json string

print(response["message"])  # returns only the message of the response
