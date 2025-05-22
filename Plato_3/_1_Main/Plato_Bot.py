'''
Plato Bot
Copyright © 2025, Quira Walker. All Rights Reserved.
This Code is licensed under the "GNU AGPL" License, a copy of this license is contained in this Folder.
If you did not receive a copy, you may find it at: https://www.gnu.org/licenses/agpl-3.0.html
'''

from Plato_3._2_Settings.botSettings import *
from _2_Settings.gameSettings import *

def time_in_range(start, end, current):
    return start <= current <= end

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(f'{bot.user} is connected to server: {guild.name}')
    print("\n\n")
    log_entry(f'Plato should be connected to: {GUILDS}\nAnd is connected to: {guildCount} servers')
    await asyncio.sleep(0.25)
    await bot.load_extension('Settings.Command_Cogs.systemCog')
    await asyncio.sleep(0.25)
    await bot.load_extension('Settings.Command_Cogs.functionCog')
    await asyncio.sleep(0.25)
    await bot.load_extension('Settings.Command_Cogs.dailyCog')

@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return
### Message & Author ###
    messages = message.content.lower()
    author   = message.author.global_name
#WORD TRACKER    
    data = track.word_occurance(message.author, messages, *track.trackedWords)
    if data != None:
        log_entry(f'{data} occurances found in message from {author}.')

    if message.content.lower() == 'help':
        await message.channel.send("Did you mean: `~help`?")

    if message.content.lower() == 'reload':
        await message.channel.send("Reloading Plato's System")
        await bot.reload_extension('Settings.Command_Cogs.systemCog')
        await message.channel.send("Reloading Plato's Functions")
        await bot.reload_extension('Settings.Command_Cogs.functionCog')
        await message.channel.send("Reloading Plato's Daily Tasks")
        await bot.reload_extension('Settings.Command_Cogs.dailyCog')


bot.run(TOKEN, reconnect=True)