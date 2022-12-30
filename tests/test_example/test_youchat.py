from youdotcom.youchat import Chat

chat = Chat()

response = chat.send_message(message="who are you?")

print(response)
# {'message': 'I am an AI-powered language model from You.com. I am designed to assist with tasks and provide answers to questions, as well as engage in conversations on a wide range of topics.'}
