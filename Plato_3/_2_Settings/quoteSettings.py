'''
Plato Bot
Copyright © 2025, Quira Walker. All Rights Reserved.
This Code is licensed under the "GNU AGPL" License, a copy of this license is contained in this Folder.
If you did not receive a copy, you may find it at: https://www.gnu.org/licenses/agpl-3.0.html
'''
from _2_Settings.botSettings import serverNode

#Quotes    
shortQuotes      = []
leadershipQuotes = []
changeQuotes     = []
learningQuotes   = []
happinessQuotes  = []
workQuotes       = []
hopeQuotes       = []
successQuotes    = []
loveQuotes       = []
lifeQuotes       = []
allQuotes        = []
quoteCategories  = ['leadership','short','change','learning','happiness','work','hope','success','love','life','all']

if serverNode == "Master":
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/short.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			shortQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/leadership.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			leadershipQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/change.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			changeQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/learning.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			learningQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/happiness.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			happinessQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/work.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			workQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/hope.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			hopeQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/success.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			successQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/love.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			loveQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/life.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			lifeQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Discord_Bots/Plato_3/_4_Supplement_Data/Quotes/allQuotes.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			allQuotes.append(line.replace(')",', ''))
		data.close()

quotes = {
	'short'      : shortQuotes,
	'leadership' : leadershipQuotes,
	'change'     : changeQuotes,
	'learning'   : learningQuotes,
	'happiness'  : happinessQuotes,
	'work'       : workQuotes,
	'hope'       : hopeQuotes,
	'success'    : successQuotes,
	'love'       : loveQuotes,
	'life'       : lifeQuotes,
	'all'		 : allQuotes
}

