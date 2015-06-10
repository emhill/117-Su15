"""
Basic Eliza Chatterbot
Emily Hill for CSCI 117
http://en.wikipedia.org/wiki/ELIZA
"""

def introduction():
	"""
	prints a welcome message and gets the user's name
	"""
	print("> Greetings. My name is Eliza.")
	name = input("> With whom am I speaking?\n")
	return name

def goodbye(name):
	"""
	prints a farewell message
	"""
	print("> It was nice chatting with you today,", name + ".")
	print("> I hope we can chat again soon!")

user = introduction()
question = "Nice to meet you, %s. How are you today?" % user
response = input("> " + question + "\n")

# \ is used to continue a code statement across line breaks
while response.lower() != "goodbye" \
  and response.lower() != "exit" \
  and response.lower() != "quit":
	if "today" in question:
		question = "Me too.\n> I love movies. What's your favorite?"
	elif "movies" in question:
		question = response + " is my favorite too! Let's have a movie marathon!"
	elif "marathon" in question:
		question = "What else do you like to do?"
	elif "like" in question:
		question = "Tell me more!"
	elif "quit" in response.lower():
		question = "I'm sorry to hear that. Is there anything I can do?"
	else:
		question = "How does that make you feel?"
	
	response = input("> " + question + "\n")

goodbye(user)