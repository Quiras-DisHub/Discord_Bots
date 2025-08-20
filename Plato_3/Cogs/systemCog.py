'''
Plato Bot
Copyright © 2025, Quira Walker. All Rights Reserved.
This Code is licensed under the "GNU AGPL" License, a copy of this license is contained in this Folder.
If you did not receive a copy, you may find it at: https://www.gnu.org/licenses/agpl-3.0.html
'''
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
        currentTime = DT.now(pytz.timezone("US/Mountain")).strftime("%b %d, %Y @ %I:%M:%S %Z")
        embed = discord.Embed(
            title= "Plato Help Menu",
            description= "All initial commands are lower case and preceeded by the tidal mark `~`. Commands that result in a follow-up response will indicate Case Sensitivity.",
            color= 0xaf7ac5)
        embed.add_field(name="help", value="Brings up this help menu.", inline=False)
        embed.add_field(name="ping", value="Pings this bot's status.", inline=False)
        embed.add_field(name="poem", value="Displays a poem at random that was written by my creator.", inline=False)
        embed.add_field(name="quote", value="Lets you choose from one of 10 quote categories.", inline=False)
        embed.add_field(name="wordy", value="# *Only works in the `Nerdy Mode` server.* #\nWill display the word tracker results in the appropriate channel.", inline=False)
        embed.add_field(name="game", value="Will start a Word Scramble game made by my creator.", inline=False)
        embed.add_field(name="guitar", value="Will start a guitar chord practice, that has options to practice chords with & without image assist.", inline=False)
        embed.set_footer(text=f"Some Commands are only available to the server owners, bot owner, or those with admin permissions.\nThis means they are not displayed in this menu.\nThey can be brought up by using thee ~admin_help command and they will be sent to a designated admin channel.\n\n{currentTime}")
        await ctx.message.add_reaction("✅")
        await ctx.send(embed=embed, delete_after=60.0)

### ADMIN HELP
    @commands.check_any(commands.is_owner(), commands.has_permissions(administrator=True))
    @commands.command()
    async def admin_help(self, ctx):
        log_entry(f'{ctx.message.author.global_name} requested the admin help menu')
        embed = discord.Embed(
            title= "Plato Admin Help Menu",
            description= "All initial commands are lower case and preceeded by the tidal mark '~'. These commands are only available to the server owners, bot owner, or those with admin permissions.",
            color= 0xaf7ac5)
        embed.add_field(name="admin_help", value="Brings up this admin help menu. (Bot Owner:Y / Server Owner:Y / Admin:Y)", inline=False)
        embed.add_field(name="execute_shutdown_protocol", value="Shuts down the bot and sends a message to the designated admin channels. (Bot Owner:Y / Server Owner:Y / Admin:Y)", inline=False)
        embed.add_field(name="temp", value="Displays the current CPU Temp of the Bot Owner's Computer. (Bot Owner:Y / Server Owner:N / Admin:N)", inline=False)
        embed.add_field(name="print_server_data", value="Prints the server data to the console. (Bot Owner:Y / Server Owner:N / Admin:N)", inline=False)
        embed.set_footer(text=DT.now(pytz.timezone("US/Mountain")).strftime("%b %d, %Y @ %I:%M:%S %Z"))
        if ctx.guild.id == GUILD_ID1 or ctx.guild.id == GUILD_ID8:
            await ctx.message.add_reaction("✅")
            await ctx.send(embed=embed, delete_after=60.0)
        else:
            await ctx.message.add_reaction("✅")
            await ctx.send(embed=embed, delete_after=60.0)
    @admin_help.error
    async def admin_help_error(self, ctx, error):
        currentTime = DT.now(pytz.timezone("US/Mountain")).strftime("%b %d, %Y @ %I:%M:%S %Z")
        if isinstance(error, commands.errors.CheckAnyFailure):
            embed = discord.Embed(
                title="Permission Denied",
                description=f"{ctx.message.author.global_name}, you do not have permission to use this command.",
                color=0xaf7ac5)
            embed.set_footer(text=f"If you need access to this command speak to my creator or Admin\n\n{currentTime}")
        await ctx.message.add_reaction("❌")
        await ctx.send(embed=embed, delete_after=10.0)

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
            color=0xaf7ac5)
        embed.add_field(name="Current Time", value=currentTime, inline=False)
        embed.add_field(name="Start Time", value=startTime, inline=False)
        embed.add_field(name="Server Count", value=f"Deployed across {guildCount} servers", inline=False)
        embed.set_footer(text=DT.now(pytz.timezone("US/Mountain")).strftime("%b %d, %Y @ %I:%M:%S %Z"))
        await ctx.message.add_reaction("✅")
        await ctx.send(embed=embed, delete_after=10.0)

### SYS-TEMP
    @commands.is_owner()
    @commands.command()
    async def temp(self, ctx):
        '''Displays the current system temperature'''
        currentTime = DT.now(pytz.timezone("US/Mountain")).strftime("%b %d, %Y @ %I:%M:%S %Z")
        log_entry(f'{ctx.message.author.global_name} requested the system temperature')
        temp_command = subprocess.run(['cat', '/sys/class/thermal/thermal_zone0/temp'], capture_output=True, text=True)
        if temp_command.returncode == 0:
            temp = float(temp_command.stdout.strip()) / 1000
            embed = discord.Embed(
                title="System Temperature",
                description=f"Current CPU Temperature: {temp:.1f}°C",
                color=0xaf7ac5)
            embed.set_footer(text=currentTime)
        await ctx.message.add_reaction("✅")
        await ctx.send(embed=embed, delete_after=10.0)
    @temp.error
    async def temp_error(self, ctx, error):
        currentTime = DT.now(pytz.timezone("US/Mountain")).strftime("%b %d, %Y @ %I:%M:%S %Z")
        if isinstance(error, commands.errors.NotOwner):
            embed = discord.Embed(
                title="Permission Denied",
                description=f"{ctx.message.author.global_name}, you do not have permission to use this command.",
                color=0xaf7ac5)
            embed.set_footer(text=f"If you need access to this command speak to my creator or Admin\n\n{currentTime}")
        await ctx.message.add_reaction("❌")
        await ctx.send(embed=embed, delete_after=10.0)
        
### SHUTDOWN
    @commands.check_any(commands.is_owner(), commands.has_permissions(administrator=True))
    @commands.command()
    async def execute_shutdown_protocol(self, ctx):
        '''Quira gets pinged if I am offline'''
        log_entry(f'Plato was shutdown by {ctx.message.author.global_name}')
        for channel in notificationChannelIDs:
            print(channel)
            await send_message(channel, "I am going offline either due to maintenance or an error has occurred. You can check with <@1249781579383963682> for more information.")
            await asyncio.sleep(0.25)
            await send_message(channel, "https://tenor.com/view/yoda-star-wars-learning-am-i-gif-7797622749241998825")
        sys.exit()
    @execute_shutdown_protocol.error
    async def execute_shutdown_protocol_error(self, ctx, error):
        currentTime = DT.now(pytz.timezone("US/Mountain")).strftime("%b %d, %Y @ %I:%M:%S %Z")
        if isinstance(error, commands.errors.CheckAnyFailure):
            embed = discord.Embed(
                title="Permission Denied",
                description=f"{ctx.message.author.global_name}, you do not have permission to use this command.",
                color=0xaf7ac5)
            embed.set_footer(text=f"If you need access to this command speak to my creator or Admin\n\n{currentTime}")
        await ctx.message.add_reaction("❌")
        await ctx.send(embed=embed, delete_after=10.0)

### PRINT SERVER DATA
    @commands.is_owner()
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
        await ctx.message.add_reaction("✅")
        await ctx.send("Server data printed to console.")
    @print_server_data.error
    async def print_server_data_error(self, ctx, error):
        currentTime = DT.now(pytz.timezone("US/Mountain")).strftime("%b %d, %Y @ %I:%M:%S %Z")
        if isinstance(error, commands.errors.NotOwner):
            embed = discord.Embed(
                title="Permission Denied",
                description=f"{ctx.message.author.global_name}, you do not have permission to use this command.",
                color=0xaf7ac5)
            embed.set_footer(text=f"If you need access to this command speak to my creator or Admin\n\n{currentTime}")
        await ctx.message.add_reaction("❌")
        await ctx.send(embed=embed, delete_after=10.0)

async def setup(bot):
    await bot.add_cog(BotSysCommands(bot))

async def teardown(bot):
    await bot.remove_cog('BotSysCommands')