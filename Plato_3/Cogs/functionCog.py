'''
Plato Bot
Copyright © 2025, Quira Walker. All Rights Reserved.
This Code is licensed under the "GNU AGPL" License, a copy of this license is contained in this Folder.
If you did not receive a copy, you may find it at: https://www.gnu.org/licenses/agpl-3.0.html
'''
from Settings.poemSettings import poemPoet, poemList
from Settings.guitarSettings import *
from Settings.quoteSettings import *
from Settings.gameSettings import *
from Settings.botSettings import *

class FuncCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

### POEM
    @commands.command()
    async def poem(self, ctx):
        '''Displays a poem written by my creator'''
        log_entry(f'{ctx.message.author.global_name} requested a poem')
        response = random.choice(poemList)
        await ctx.channel.send(poemPoet + response)
        log_entry('Poem Sent')

### Quote
    @commands.command()
    async def quote(self, ctx):
        '''Displays a Quote Menu'''
        log_entry(f'{ctx.message.author.global_name} requested a quote')
        await ctx.channel.send("**What kind of quote would you like?**\n*(Please type the category as shown)*\n\n* Leadership\n* Short\n* Change\n* Learning\n* Happiness\n* Work\n* Hope\n* Success\n* Love\n* Life")
        while True:
            try:
                requestedQuote = await bot.wait_for('message', check=author_check(ctx.author), timeout=60.0)
            except TimeoutError:
                await ctx.channel.send(f'{ctx.author} did not make a selection in time, so a quote will be chosen at random.')
                log_entry(f'{ctx.message.author.global_name} timed out on Quote Selection')
###Random
                response = random.choice(allQuotes)
                await ctx.channel.send(response)
                log_entry('Quote Sent')
                break
            requestedQuote = requestedQuote.content.lower()
            log_entry(f'Sending: {requestedQuote}\t@ random')
###Requested
            if requestedQuote in quoteCategories:
                response = random.choice(quotes[requestedQuote])
                await ctx.channel.send(response)
                log_entry('Quote Sent')
            break

### WORD TRACKER RESULTS
    @commands.command()
    async def wordy(self, ctx):
        '''Special feature to Nerdy Mode Server only'''
        if ctx.guild.id != GUILD_ID1 and ctx.guild.name != GUILD1:
            await ctx.channel.send("This command is only available in the `Nerdy Mode` Server")
            log_entry(f'{ctx.message.author.global_name} from {ctx.guild.name} tried to use the word tracker command')
            return
        elif ctx.guild.id == GUILD_ID1 and ctx.guild.name == GUILD1:
            log_entry(f'{ctx.message.author.global_name} requested to see the tracked word results.')
            results = track.results()
            await send_message(wordStatChannelId1, results)

### GAME
    @commands.command()
    async def game(self, ctx):
        log_entry(f'{ctx.message.author.global_name} started a game.')
        await ctx.message.channel.send("Please wait while I load: **Word Unscramble**")
        await asyncio.sleep(2)
        await ctx.message.channel.send("***NOTE:*** *The menus have changed please read them carefully*")
        await asyncio.sleep(3)
        while True:
            await ctx.message.channel.send(G1_Intro)
            try:
                gameMenu = await bot.wait_for('message', check=author_check(ctx.message.author), timeout=menuTimer*60)
            except TimeoutError:
                log_entry(f'{ctx.message.author.global_name} Timed out on Game Main-menu')
                await ctx.message.channel.send(f"Ressetting due to player choice time out: there is a {menuTimer} Minute timer to make selections.")
                log_entry('Game was reset')
                break
            gameMenu = gameMenu.content.lower()
            while True:
                if gameMenu == 'info':
                    await ctx.message.channel.send(Info)
                    await asyncio.sleep(5)
                    break
                elif gameMenu == 'rules':
                    await ctx.message.channel.send(Rules)
                    await asyncio.sleep(5)
                    break
                elif gameMenu == 'contact':
                    await ctx.message.channel.send(Contact)
                    await asyncio.sleep(5)
                    break
                elif gameMenu == 'play':
                    await ctx.message.channel.send(Dictionary_Selection)
                    try:
                        dictSelection = await bot.wait_for('message', check=author_check(ctx.message.author), timeout=menuTimer*60)
                    except TimeoutError:
                        log_entry(f'{ctx.message.author.global_name} Timed out on Game Dict-Selection')
                        await ctx.message.channel.send(f"Ressetting due to player choice time out: there is a {menuTimer} Minute timer to make selections.")
                        log_entry('Game was reset')
                        break
                    dictSelection = dictSelection.content.lower()
                    if dictSelection not in dictOptions:
                        await ctx.message.channel.send("Please enter a valid dictionary selections")
                        await asyncio.sleep(1)
                        break
                    elif dictSelection in dictOptions:
                        if dictSelection == 'full':
                            ready_chosen_dict(fullDict)
                        elif dictSelection == 'cmu':
                            ready_chosen_dict(olderDict)
                        elif dictSelection == 'mit':
                            ready_chosen_dict(newerDict)
                        elif dictSelection == 'first':
                            ready_chosen_dict(firstNameDict)
                        elif dictSelection == 'last':
                            ready_chosen_dict(lastNameDict)
                    
                    while True:
                        trackGame  = {'Dict' : dictSelection, 'Letter Count' : None, 'Capitalized' : None, 'Word' : None}
                        guesses    = 0
                        maxGuesses = 4 # Starts @ 0, so 0-4 is 5 guesses
                        letters    = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,29]
                        await ctx.message.channel.send("\n\nPlease enter the number of the letters you wish the word to contain: (1-25, 28, 29)")
                        try:
                            letterCount = await bot.wait_for('message', check=author_check(ctx.message.author), timeout=menuTimer*60)
                        except TimeoutError:
                            log_entry(f'{ctx.message.author.global_name} Timed out on Game Sub-menu: 1')
                            await ctx.message.channel.send(f"Timed Out: Please respond within {menuTimer} Minute")
                            break
                        number = int(letterCount.content)
                        if number not in letters:
                            await ctx.message.channel.send("Please enter a number 1-25, 28, 29")
                            break
                        trackGame['Letter Count'] = number
                        keyWord = random.choice(wordLength[number])
                        trackGame['Word'] = keyWord
                        
                        await ctx.message.channel.send("\n\n Do you wish to have the first letter capitalized: *Y* or *N*")
                        try:
                            answer = await bot.wait_for('message', check=author_check(ctx.message.author), timeout=menuTimer*60)
                        except TimeoutError:
                            log_entry(f'{ctx.message.author.global_name} Timed out on Game Sub-menu: 2')
                            await ctx.message.channel.send(f"Timed Out: Please respond within {menuTimer} Minute")
                            break
                        answer = answer.content.lower()
                        if answer == 'y':
                            trackGame['Capitalized'] = 'Yes'
                            scrambledWord = shuffle_word(keyWord.title())
                        elif answer == 'n':
                            trackGame['Capitalized'] = 'No'
                            scrambledWord = shuffle_word(keyWord)
                        log_entry(trackGame)
                        while True:
                            await ctx.message.channel.send(f"\nPlease try to unscramble the word below.\nYou have 2 minutes & {guesses}/{maxGuesses} guesses left\nYour word is: {scrambledWord} >>> ")
                            try:
                                Guess = await bot.wait_for('message', check=author_check(ctx.message.author), timeout=guessTimer*60)
                            except TimeoutError:
                                await ctx.message.channel.send(f"Sorry, your {guessTimer} Minutes are up.\n\nThe correct word was: {keyWord}")
                                log_entry(f'{ctx.message.author.global_name} ran out of time')
                                break
                            guess = str(Guess.content)
                            guess = guess.lower()
                            if	guess.isalpha():
                                if sorted(guess) == sorted(keyWord):
                                    if guess == keyWord:
                                        await ctx.message.channel.send(f"'{guess}' was the correct answer!")
                                        guesses = 0
                                        await ctx.message.channel.send("Thank you for playing!")
                                        break
                                    elif guess != keyWord:
                                        if guesses < maxGuesses:
                                            await ctx.message.channel.send(f"'{guess}' is incorrect, try again!\n")
                                            guesses += 1
                                        elif guesses == maxGuesses:
                                            await ctx.message.channel.send(f"'{guess}' is incorrect\nThe correct word was '{keyWord}'")
                                            guesses = 0
                                            await ctx.message.channel.send("Thank you for playing")
                                            break
                                elif guess.lower() == "giveup":
                                    await ctx.message.channel.send(f"You have gave up, '{keyWord}' was the word you were looking for.\n\nGood luck next time.")
                                    log_entry(f'{ctx.message.author.global_name} gave up')
                                    break
                        break
                    break
                break
            ctx.message.channel.send("Do you wish to play again: *(**Y**)es* or *(**N**)o*?")
            try:
                contin = await bot.wait_for('message', check=author_check(ctx.message.author), timeout=menuTimer*60)
                contin = contin.content.lower()
            except TimeoutError:
                if contin == 'y' or 'yes':
                    log_entry(f'{ctx.message.author.global_name} chose to play again')
                    continue
                elif contin == 'n' or 'no':
                    log_entry(f'{ctx.message.author.global_name} chose to end the game')
                    await ctx.message.channel.send("Thanks for playing!")
                    break
                else:
                    await ctx.message.channel.send('Ending game due to invalid input')
                    break

### GUITAR
    @commands.command()
    async def guitar_practice(self, ctx):
            log_entry(f"{ctx.message.author.global_name} is Practicing. {bot.user} will create a log.")
            practicing = True
            practiceLog['Start'] = True
            while practicing:
                await ctx.channel.send("Please use the following menu to help make a selection:\n(*send the number of the category you want*)\n**Chords by name**\n\t* 1: Without image assist\n* 2: With image assist")
                while True:
                    try:
                        practiceSelection = await bot.wait_for('message', timeout=120)
                    except:
                        TimeoutError
                        await ctx.channel.send(f"{ctx.message.author.global_name} gave no Input before timeout was reached.")
                        practiceLog['Timeout'] = "Timed out on category selection."
                        log_entry(f"Practice Selection Timed out.")
                        log_entry(practiceLog)
                        break
                    practiceSelection = str(practiceSelection.content)
                    practiceLog['Category'] = practiceSelection
                    if practiceSelection not in practiceMenuOptions:
                        await ctx.channel.send(f"{ctx.message.author.global_name} your selection did not match a given option, please try again.")
                        break
    #(NO IMAGE)
                    elif practiceSelection == '1':
                        await ctx.channel.send("Please enter the number of chords you wish to practice.")
                        while True:
                            try:
                                chordCount = await bot.wait_for('message', timeout=120)
                            except:
                                TimeoutError
                                await ctx.channel.send(f"{ctx.message.author.global_name} gave no input before timeout was reached.")
                                practiceLog['Timeout'] = "Timed out on number of chords."
                                log_entry(f"Number of Chords Timed out.")
                                log_entry(practiceLog)
                                break
                            chordCount = int(chordCount.content)
                            practiceLog['Chord Count'] = chordCount
                            chords = []
                            ck = []
                            for chord in CHORDS.keys():
                                ck.append(chord)
                            for _ in range(chordCount):
                                chords.append(random.choice(ck))
                            chords.append('End')
                            practiceLog['Chords'] = chords
                            await ctx.channel.send("You have 30 seconds to get ready")
                            await ctx.channel.send("30")
                            await asyncio.sleep(delay)
                            await ctx.channel.send("20")
                            await asyncio.sleep(delay)
                            await ctx.channel.send("10")
                            await asyncio.sleep(delay)
                            for chord in chords:
                                if chord == 'End':
                                    practiceLog['End'] = True
                                    await ctx.channel.send(f'{chord}')
                                    break
                                else:
                                    await ctx.channel.send(f"**{chord}**")
                                    await asyncio.sleep(delay)
                                    await ctx.channel.send('.')
                                    await asyncio.sleep(delay)
                                    await ctx.channel.send('.')
                                    await asyncio.sleep(delay)
                            break
                        await ctx.channel.send("Do you wish to practice further: *(**Y**)es* or *(**N**)o*")
                        try:
                            contin = await bot.wait_for('message', timeout=120)
                        except:
                            TimeoutError
                            await ctx.channel.send(f"{ctx.message.author.global_name} gave no Input before timeout was reached.")
                            practiceLog['Timeout'] = "Timed out on continue."
                            log_entry(f"Continue Timed out.")
                            log_entry(practiceLog)
                            break
                        contin = contin.content.lower()
                        if contin == 'y':
                            practiceLog['Continue'] = 'Yes'
                            log_entry(practiceLog)
                            break
                        elif contin == 'n':
                            practiceLog['Continue'] = 'No'
                            practiceLog['Stop'] = True
                            log_entry(practiceLog)
                            practicing = False
                            break
    #(IMAGE)
                    elif practiceSelection == '2':
                        await ctx.channel.send("Please enter the number of chords you wish to practice.")
                        while True:
                            try:
                                chordCount = await bot.wait_for('message', timeout=120)
                            except:
                                TimeoutError
                                await ctx.channel.send(f"{ctx.message.author.global_name} gave no Input before timeout was reached.")
                                practiceLog['Timeout'] = "Timed out on number of chords."
                                log_entry(f"Number of Chords Timed out.")
                                log_entry(practiceLog)
                                break
                            chordCount = int(chordCount.content)
                            practiceLog['Chord Count'] = chordCount
                            chords = []
                            ck = []
                            for chord in CHORDS.keys():
                                ck.append(chord)
                            for _ in range(chordCount): 
                                chords.append(random.choice(ck))
                            chords.append('End')
                            practiceLog['Chords'] = chords
                            await ctx.channel.send("You have 30 seconds to get ready")
                            await ctx.channel.send("30")
                            await asyncio.sleep(delay)
                            await ctx.channel.send("20")
                            await asyncio.sleep(delay)
                            await ctx.channel.send("10")
                            await asyncio.sleep(delay)
                            for chord in chords:
                                if chord == 'End':
                                    practiceLog['End'] = True
                                    await ctx.channel.send(file=discord.File(CHORDS[chord]))
                                    break
                                else:
                                    await ctx.channel.send(file=discord.File(CHORDS[chord]))
                                    await asyncio.sleep(delay)
                                    await ctx.channel.send('.')
                                    await asyncio.sleep(delay)
                                    await ctx.channel.send('.')
                                    await asyncio.sleep(delay)
                            break
                        await ctx.channel.send("Do you wish to practice further: *(**Y**)es* or *(**N**)o*")
                        try:
                            contin = await bot.wait_for('message', timeout=120)
                        except:
                            TimeoutError
                            await ctx.channel.send(f"{ctx.message.author.global_name} gave no Input before timeout was reached.")
                            practiceLog['Timeout'] = "Timed out on continue."
                            log_entry(f"Continue Timed out.")
                            log_entry(practiceLog)
                            break
                        contin = contin.content.lower()
                        if contin == 'y':
                            practiceLog['Continue'] = 'Yes'
                            log_entry(practiceLog)
                            break
                        elif contin == 'n':
                            practiceLog['Continue'] = 'No'
                            practiceLog['Stop'] = True
                            log_entry(practiceLog)
                            practicing = False
                            break

async def setup(bot):
    await bot.add_cog(FuncCommands(bot))
    log_entry("FuncCommands Cog loaded into sys")

async def teardown(bot):
    await bot.remove_cog(FuncCommands(bot))
    log_entry("FuncCommands Cog unloaded from sys")