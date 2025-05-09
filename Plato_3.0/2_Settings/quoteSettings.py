from Settings.botSettings import serverNode

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
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/short.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			shortQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/leadership.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			leadershipQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/change.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			changeQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/learning.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			learningQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/happiness.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			happinessQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/work.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			workQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/hope.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			hopeQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/success.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			successQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/love.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			loveQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/life.txt', 'r') as data:
		for line in data:
			line = line.replace('(', '"\n\t~')
			lifeQuotes.append(line.replace(')",', ''))
		data.close()
	with open('/home/one-to-rule-them-all/VIRTUAL/Code_File/Workroom/Discord_Bots/Plato_2.0/Quote_Files/allQuotes.txt', 'r') as data:
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

