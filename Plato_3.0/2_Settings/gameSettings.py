'''
Plato Bot
Copyright © 2025, Quira Walker. All Rights Reserved.
This Code is licensed under the "GNU AGPL" License, a copy of this license is contained in this Folder.
If you did not receive a copy, you may find it at: https://www.gnu.org/licenses/agpl-3.0.html
'''
from Settings.botSettings import serverNode, punctuation, random, re

#TIME IN MINUTES
menuTimer = 1
guessTimer = 2

#DICTIONARY FILE AND WORD PREP
dictOptions = ['full','cmu','mit','first','last']
if serverNode == "Master":
	firstNameDict = open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Game_Files/DICTS/NAMES/first-names.txt', 'r')
	lastNameDict  = open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Game_Files/DICTS/NAMES/last-names.txt', 'r')
	fullDict      = open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Game_Files/DICTS/FULL_DICT.txt', 'r')
	olderDict     = open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Game_Files/DICTS/main_cambridge.txt', 'r')
	newerDict     = open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Game_Files/DICTS/main_mit.txt', 'r')

words 	   = []
wordList   = []
wordLength = {}

def ready_chosen_dict(data):
    for word in data:
        word = word.lower().strip(punctuation)
        words.append(word)
    for word in words:
        wordList.append(re.sub('\n', '', word))
    for word in wordList:
        clean_word = re.sub('\n', '', word)
        wordLength.setdefault(len(clean_word), []).append(clean_word)

def shuffle_word(word):
    lst = [*word]
    random.shuffle(lst)
    return ''.join(lst)

#WORD GAME
G1_Intro = f"""
        **`Word Scramble:`**
        Use the following menu to navigate the game: (command : command explination)
            Play    : Starts the Game
            Rules   : Display Game Rules
            Info    : Display Game Info
            Contact : Display Creator Contact

        *I will auto reset if no input is received for {menuTimer} Minute.*
        """
Info = "This game was custom created and designed to help build your vocabulary.\nIt can also challenge your knowledge.\nThere are nearly 200,000 words that you may face. :eyes:"
Rules = "You must choose a word with anywhere from 1 to 25 letters or 28, 29 letter words\nYou will have 5 guesses & 2 minutes\nIf you wish to give up type *Giveup*."
Contact = f"This game was created by Quira Waker with assistance by HackySack.\nIf there are issues or suggestions with/for the bot or game, please contact\n\t* Discord: <@1249781579383963682>"
Dictionary_Selection = """
        **`Dictionary List Selection:`**
        Please use the following list to choose the dictionary you wish to use: (command : dictionary explination)
            **Full**  : This is a combo of the Carnegie Mellon and MIT dictionaries it will contain new and old world words.
            **CMU**   : This is a the Carnegie Mellon University dictionary and will house almost all english words including some that are archaic.
            **MIT**   : This is a dictionary made by MIT and contains, as they said, 10,000 of the most commonly used english words. Don't expect to find archaic words here.
            **First** : Not a list of words, but rather a list of first names.
            **Last**  : Not a list of words, but rather a list of last names.
        """