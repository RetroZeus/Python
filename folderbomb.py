import string
import random
import os

wordlist = [] 
wordlist.extend(list(string.ascii_uppercase)) 
guess_list = []
PATH = f"C:\\Users\\{os.getlogin()}\\Desktop"

def connect_characters(wordnum):
	global wordlist
	random.shuffle(wordlist) 
	word = wordlist[0:wordnum] 
	complete_word = ''.join(word)
	return complete_word

def already_found():
	global guess_list
	guess_list.extend(range(25)) 
	get_number = random.choice(guess_list) 
	folder_name = connect_characters(wordnum=get_number) 
	os.mkdir(folder_name) 
	print("Created")
	

def create_folder(name):
	global PATH
	global guess_list
	try:
		if not os.getcwd() in PATH:
			os.chdir(PATH)
			os.mkdir(name) 
		else:
			os.mkdir(name) 

		msg = "Successfully created"
		return msg
	except FileExistsError as err:
		print(err)
		print("Creating another one")
		already_found()

timer = 0
end_time = 2
while True:
	if time != end_time:
		timer += 1
		create_folder(name="MAC")
	elif time == end_time:
		quit()

