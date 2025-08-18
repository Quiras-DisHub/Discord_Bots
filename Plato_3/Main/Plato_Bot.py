'''
Plato Bot
Copyright © 2025, Quira Walker. All Rights Reserved.
This Code is licensed under the "GNU AGPL" License, a copy of this license is contained in this Folder.
If you did not receive a copy, you may find it at: https://www.gnu.org/licenses/agpl-3.0.html
'''
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Settings.botSettings import *
from Settings.gameSettings import *

def time_in_range(start, end, current):
    return start <= current <= end

@bot.event
async def on_ready():
    print(f'{bot.user} is connected to the following server(s):')
    counter1 = 0
    for guild in bot.guilds:
        counter1 += 1
        print(f'\t{counter1}: {guild.name}')
    print("\n\n")
    log_entry(f'Plato should be connected to ({guildCount}) servers: {GUILDS}\n\tAnd is connected to: {counter1} servers.')
    cogLoad = await load_cogs()
    if cogLoad:
        log_entry(f'Plato successfully loaded all cogs.')

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
        log_entry(f'{message.author.global_name} requested Plato to reload.')
        cogReload = await reload_cogs()
        embed = discord.Embed(
            title="Reload Confirmation",
            description=f"{message.author.global_name} requested Plato to reload.",
            color=0xaf7ac5)
        embed.add_field(name="System Reload:", value="Successful", inline=True)
        embed.add_field(name="Function Reload:", value="Successful", inline=True)
        embed.add_field(name="Daily Reload:", value="Successful", inline=True)
        embed.set_footer(text=DT.now(pytz.timezone("US/Mountain")).strftime("%b %d, %Y @ %I:%M:%S %Z"))
        await message.channel.send(embed=embed)

if __name__ == '__main__':
    bot.run(TOKEN, reconnect=True)