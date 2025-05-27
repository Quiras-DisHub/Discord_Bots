'''
Plato Bot
Copyright © 2025, Quira Walker. All Rights Reserved.
This Code is licensed under the "GNU AGPL" License, a copy of this license is contained in this Folder.
If you did not receive a copy, you may find it at: https://www.gnu.org/licenses/agpl-3.0.html
'''
import subprocess, asyncio, random, ephem, pytz, json, time, sys, os, re 
from string import punctuation
from datetime import datetime as DT

try:
    import discord
except ImportError:
    print("The Discord Module could not be found, please run:\npip install -U discord.py\nThen try again.")
try:
	from discord.ext import commands, tasks
except ImportError:
	print("The Discord Module could not be accessed.")
try:
    from dotenv import load_dotenv
    load_dotenv('/home/one-to-rule-them-all/VIRTUAL/Code_File/BOT_STUFF/SENSITIVE/.env')
except ImportError:
    print("The Dotenv Module was not found, so please run:\npip install -U python-dotenv\nThen try again")

#BOT ACCESS TOKEN
TOKEN = os.getenv('DISCORD_TOKEN')

#BOT INTENT PERMISSIONS
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='~', intents=intents, help_command=None)

#NODE SELECTION
serverNode = os.getlogin()
if serverNode == 'one-to-rule-them-all':
	serverNode = "Master"

#SERVER INFO
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
GUILD1 			   = os.getenv('DISCORD_GUILD1')
GUILD_ID1          = os.getenv('DISCORD_GUILD_ID1')
channelId1         = os.getenv('MODERATION_CHANNEL_ID1')
moonChannelId1     = os.getenv('GEOGRAPHY_CHANNEL_ID1')
quoteChannelId1    = os.getenv('QUOTE_CHANNEL_ID1')
wordStatChannelId1 = os.getenv('WORDY_CHANNEL_ID1')
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
GUILD2          = os.getenv('DISCORD_GUILD2')
GUILD_ID2       = os.getenv('DISCORD_GUILD_ID2')
channelId2      = os.getenv('NOTIF_CHANNEL_ID2')
quoteChannelId2 = os.getenv('DAILYQUOTE_CHANNEL_ID2')
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
GUILD3 	   = os.getenv('DISCORD_GUILD3')
GUILD_ID3  = os.getenv('DISCORD_GUILD_ID3')
channelId3 = os.getenv('NOTIF_CHANNEL_ID3')
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
GUILD4 	   = os.getenv('DISCORD_GUILD4')
GUILD_ID4  = os.getenv('DISCORD_GUILD_ID4')
channelId4 = os.getenv('NOTIF_CHANNEL_ID4')
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
GUILD5 	   = os.getenv('DISCORD_GUILD5')
GUILD_ID5  = os.getenv('DISCORD_GUILD_ID5')
channelId5 = os.getenv('PLATOBOT_CHANNEL_ID5')
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
GUILD6 	      = os.getenv('DISCORD_GUILD6')
GUILD_ID6     = os.getenv('DISCORD_GUILD_ID6')
channelID6    = os.getenv('GUITAR_CHANNEL_ID6')
botChannelID6 = os.getenv('NOTIF_CHANNEL_ID6')
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
GUILD7 	   = os.getenv('DISCORD_GUILD7')
GUILD_ID7  = os.getenv('DISCORD_GUILD_ID7')
channelId7 = os.getenv('GENERAL_CHANNEL_ID7')
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
GUILD8 	   	= os.getenv('DISCORD_GUILD')
GUILD_ID8   = os.getenv('DISCORD_GUILD_ID8')
channelId8 	= os.getenv('PLATO_NOTIF_CHANNEL_ID8')
boosterRole = os.getenv('ROLE_NAME')
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
notificationChannelIDs = [channelId1, channelId2, channelId3, channelId4, channelId5, botChannelID6, channelId7, channelId8]
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###
GUILDS = f'\n~ {GUILD1}\n~ {GUILD2}\n~ {GUILD3}\n~ {GUILD4}\n~ {GUILD5}\n~ {GUILD6}\n~ {GUILD7}\n~ {GUILD8}'
guildCount = len(GUILDS.split('\n')) - 1

#TIME
startTime = DT.now(pytz.timezone("US/Mountain"))
startTime = startTime.strftime("%b %d, %Y @ %I:%M:%S %Z")
#COMMAND RESPONSES
pingTest = ["Pong", "Pong was busy so a Ding Dong has been sent", "Pong... Ding... Dong... Ching... Chong"]

def author_check(author):
    return lambda message: message.author == author

async def send_message(channel_id, message_content):
    channel = bot.get_channel(channel_id)
    if channel is None:
        log_entry(f'Message was unable to be sent due to:\n\t\tAttempted Message: {message_content}\n\t\tInvalid Channel Id: {channel_id}')
    await channel.send(message_content)

async def ready_message(ID, guild):
	await send_message(ID, f"Hello I am {bot.user}.\nI have successfully connected to this server and am ready to use.")
	print(f"{bot.user} has successfully connected to the following guild: {guild.name}")

#LOGGING
if serverNode == "Master":
	log = '/home/one-to-rule-them-all/VIRTUAL/Code_File/BOT_STUFF/LOGS/systemLog.txt'
def log_entry(message):
	logEntryTime = DT.now(pytz.timezone("US/Mountain"))
	logEntryTime = logEntryTime.strftime("%b %d, %Y @ %I:%M:%S %Z")
	with open(log, 'a') as logFile:
		entry = f'\n\n{logEntryTime}\n\t{message}'
		logFile.write(entry)
	logFile.close()
     
#WORD TRACKING
class WordTracker():
	def __init__(self):
		self.trackedWords = ['roy', ':3', 'fuck', 'fucking', 'fuckery']
		if serverNode == "Master":
			self.logFile = '/home/one-to-rule-them-all/VIRTUAL/Code_File/BOT_STUFF/LOGS/wordLog.json'
		self.currentLog = None
	def read_logs(self):
		with open(self.logFile, 'r', encoding='UTF-8') as log:
			try:
				self.currentLog = json.load(log)
				for x in self.currentLog.keys():
					for word in self.currentLog[x]['Words']:
						self.currentLog[x]['Words'][word] = int(self.currentLog[x]['Words'][word])
			except json.decoder.JSONDecodeError:
				pass
		log.close()
	def save_logs(self, data):
			with open(self.logFile, 'w', encoding='UTF-8') as log:
				json.dump(data, log, ensure_ascii=False, indent=2)
			log.close()
	def was_word_said(self, text, word):
		pattern = f'(?<!\w){re.escape(word)}(?!\w)'
		matches = re.findall(pattern, text, re.IGNORECASE)
		return len(matches)
	def word_occurance(self, user, text, *words):
		self.read_logs()
		for word in words:
			occurances = self.was_word_said(text, word)
			self.currentLog['Total']['Words']['all'] += occurances
			self.currentLog['Total']['Words'][word] += occurances
			if self.currentLog != None and str(user.id) != None:
				if str(user.id) in self.currentLog.keys():
					self.currentLog[str(user.id)]['Words'][word] += occurances
				if str(user.id) not in self.currentLog.keys():
					self.currentLog[str(user.id)] = {
						"Name" : user.global_name,
						"Words" : {
							"roy": 0,
					        ":3": 0,
					        "fuck": 0,
					        "fucking": 0,
					        "fuckery": 0
						}
					}
					self.currentLog[str(user.id)]['Words'][word] += occurances
		self.save_logs(self.currentLog)
		if occurances < 0:
			return occurances
	def results(self):
		self.read_logs()
		data = f"Memebers have said the following words a total of {self.currentLog['Total']['Words']['all']} times.\nRoy = {self.currentLog['Total']['Words']['roy']} times\n:3 = {self.currentLog['Total']['Words'][':3']} times\nFuck = {self.currentLog['Total']['Words']['fuck']} times\nFucking = {self.currentLog['Total']['Words']['fucking']} times\nFuckery = {self.currentLog['Total']['Words']['fuckery']} times"
		return f"This is still under construction, but for now:\n{data}"
track = WordTracker()

class MoonPhase():
	def __init__(self):
		self.lunation = {
			'Jan 6'  : 'First Quarter (Wanning)','Jan 13' : 'Full Moon','Jan 21' : 'Third Quarter (Waxing)','Jan 29' : 'New Moon',
    		'Feb 5'  : 'First Quarter (Wanning)','Feb 12' : 'Full Moon','Feb 20' : 'Third Quarter (Waxing)','Feb 27' : 'New Moon',
    		'Mar 6'  : 'First Quarter (Wanning)','Mar 14' : 'Full Moon','Mar 22' : 'Third Quarter (Waxing)','Mar 29' : 'New Moon',
    		'Apr 4'  : 'First Quarter (Wanning)','Apr 12' : 'Full Moon','Apr 20' : 'Third Quarter (Waxing)','Apr 27' : 'New Moon',
    		'May 4'  : 'First Quarter (Wanning)','May 12' : 'Full Moon','May 20' : 'Third Quarter (Waxing)','May 26' : 'New Moon',
    		'Jun 2'  : 'First Quarter (Wanning)','Jun 11' : 'Full Moon','Jun 18' : 'Third Quarter (Waxing)','Jun 25' : 'New Moon',
    		'Jul 2'  : 'First Quarter (Wanning)','Jul 10' : 'Full Moon','Jul 17' : 'Third Quarter (Waxing)','Jul 24' : 'New Moon',
    		'Aug 1'  : 'First Quarter (Wanning)','Aug 9'  : 'Full Moon','Aug 15' : 'Third Quarter (Waxing)','Aug 23' : 'New Moon','Aug 31' : 'First Quarter (Wanning)',
    		'Sep 7'  : 'Full Moon','Sep 14' : 'Third Quarter (Waxing)','Sep 21' : 'New Moon','Sep 29' : 'First Quarter (Wanning)',
    		'Oct 6'  : 'Full Moon','Oct 13' : 'Third Quarter (Waxing)','Oct 21' : 'New Moon','Oct 29' : 'First Quarter (Wanning)',
    		'Nov 5'  : 'Full Moon','Nov 11' : 'Third Quarter (Waxing)','Nov 19' : 'New Moon','Nov 27' : 'First Quarter (Wanning)',
    		'Dec 4'  : 'Full Moon','Dec 11' : 'Third Quarter (Waxing)','Dec 19' : 'New Moon','Dec 27' : 'First Quarter (Wanning)'}
	def phase(self):
		moonDate = DT.now(pytz.timezone("US/Mountain"))
		moonDate = moonDate.strftime("%b %d")
		for date in self.lunation.keys():
			if date == moonDate:
				return f"It is {moonDate} & the moon phase is: {self.lunation[date]}"
lunar = MoonPhase()