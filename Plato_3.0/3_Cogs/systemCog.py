from Settings.quoteSettings import *
from Settings.botSettings import *

class BotSysCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dailyTask = False

### HELP
    @commands.command()
    async def help(self, ctx):
        '''Displays the command Help Menu'''
        log_entry(f'{ctx.message.author.global_name} requested the help menu')
        
        embed = discord.Embed(
            title= "Plato Help Menu",
            description= "All initial commands are lower case and preceeded by the tidal mark `~`. Commands that result in a follow-up response will indicate Case Sensitivity.",
            color= 0xaf7ac5
        )
        embed.add_field(name="ping", value="Pings this bot's status", inline=False)
        embed.add_field(name="poem", value="Displays a poem at random that was written by my creator", inline=False)
        embed.add_field(name="quote", value="Lets you choose from one of 10 quote categories", inline=False)
        embed.add_field(name="wordy", value="# *Only works in the `Nerdy Mode` server* #\nWill display the word tracker results in the appropriate channel", inline=False)
        embed.add_field(name="game", value="Will start a Word Scramble game made by my creator", inline=False)
        embed.add_field(name="guitar_practice", value="Will start a guitar chord practice, that has options to practice chords with & without image assist", inline=False)
        
        await ctx.send(embed=embed)

### PING
    @commands.command()
    async def ping(self, ctx):
        '''Pings this bot for system status'''
        currentTime = DT.now(pytz.timezone("US/Mountain"))
        currentTime = currentTime.strftime("%b %d, %Y @ %I:%M:%S %Z")
        log_entry(f'{ctx.message.author.global_name} Pinged Plato @ {currentTime}')
        response = random.choice(pingTest)

        embed = discord.Embed(
            title="Plato Status",
            description=response,
            color=0xaf7ac5
        )
        embed.add_field(name="Current Time", value=currentTime, inline=False)
        embed.add_field(name="Start Time", value=startTime, inline=False)
        embed.add_field(name="Server Count", value=f"Deployed across {guildCount} servers", inline=False)

        await ctx.send(embed=embed)

### SYS-TEMP
    @commands.command()
    async def temp(self, ctx):
        '''Displays the current system temperature'''
        log_entry(f'{ctx.message.author.global_name} requested the system temperature')
        temp_command = subprocess.run(['cat', '/sys/class/thermal/thermal_zone0/temp'], capture_output=True, text=True)
        try:
            if temp_command.returncode == 0:
                temp = float(temp_command.stdout.strip()) / 1000
                embed = discord.Embed(
                    title="System Temperature",
                    description=f"Current CPU Temperature: {temp:.1f}°C",
                    color=0xaf7ac5
                )
        except Exception as e:
            embed = discord.Embed(
                title="System Temperature",
                description=f"An Error has occured: {str(e)}",
                color=0xaf7ac5
            )        
        await ctx.send(embed=embed)
        
### SHUTDOWN
    @commands.command()
    async def execute_shutdown_protocol(self, ctx):
        '''Quira gets pinged if I am offline'''
        log_entry(f'Plato was shutdown by {ctx.message.author.global_name}')
        for channel in notificationChannelIDs:
            await send_message(channel, "I am going offline either due to maintenance or an error has occurred. You can check with <@1249781579383963682> for more information.")
            await asyncio.sleep(0.25)
            await send_message(channel, "https://tenor.com/view/yoda-star-wars-learning-am-i-gif-7797622749241998825")
        sys.exit()

### PRINT SERVER DATA
    @commands.command()
    async def print_server_data(self, ctx):
        '''Prints the server data to the console'''
        log_entry(f'{ctx.message.author.global_name} requested server data')
        for guild in self.bot.guilds:
            print("--------------------------------------------------")
            print(f"Server Name: {guild.name}")
            print(f"Server ID: {guild.id}")
            print(f"Member Count: {guild.member_count}")
            print("--------------------------------------------------")
        await ctx.send("Server data printed to console.")

async def setup(bot):
    await bot.add_cog(BotSysCommands(bot))
    log_entry("BotSysCommands Cog loaded into sys")

async def teardown(bot):
    await bot.remove_cog(BotSysCommands(bot))
    log_entry("BotSysCommands Cog unloaded from sys")