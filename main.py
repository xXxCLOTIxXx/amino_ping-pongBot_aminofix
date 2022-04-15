import aminofix

client = aminofix.Client()

email = "Почта"
password = "Пароль"

try:
	client.login(email=email, password=password)
	print("Succesful")
except:
	print("\nInvalid email or password\n")
	exit()


@client.event("on_text_message")
def on_msg(data):
	chat_id = data.message.chatId
	com_id = data.comId
	sub_client = aminofix.SubClient(comId=com_id, profile=client.profile)
	ct = data.message.content
	content = ct.lower().split(" ")
	chat_tit = sub_client.get_chat_thread(chat_id).title
	id = data.message.messageId
	user_name = data.message.author.nickname
	user_id = data.message.author.userId
	try:
		replyNick = data.message.extensions["replyMessage"]["author"]["nickname"]
		replyCont = data.message.extensions["replyMessage"]["content"]
		replyId = data.message.extensions["replyMessage"]["author"]["uid"]
	except:
		replyId = "none"
		replyNick = "Нет"
		replyCont = "Сообщение не содержит ответ на другое сообщение"
	print(f"\n\nЧат: {chat_tit}\nНик: {user_name}\nЧто написал: {ct}\nКому ответил {replyNick}\nНа что ответил: {replyCont}")

	if content[0][0] == '/':
		if content[0][1:] == 'ping':
			sub_client.send_message(message="pong!", chatId=chat_id, replyTo=id)
		elif content[0][1:] == 'pong':
			sub_client.send_message(message="ping!", chatId=chat_id)