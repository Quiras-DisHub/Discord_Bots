from Settings.botSettings import *
from Plato_Bot import time_in_range
from Settings.quoteSettings import allQuotes

class DailyTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_task.start()
        self.timezone = pytz.timezone('US/Mountain')

    def cog_unload(self):
        self.daily_task.cancel()  # Cleanup when cog is unloaded

    @tasks.loop(minutes=1)  # Check every minute
    async def daily_task(self):
        now = DT.now(self.timezone)
        target_time = time(16, 23)
        
        current_time = now.time()
        start_time = time(target_time.hour, target_time.minute)
        end_time = time(target_time.hour, target_time.minute + 1)

        if time_in_range(start_time, end_time, current_time):
            '''Daily Features: Daily Quote, Moon Phase'''
            log_entry("Begining Daily Tasks")
### QUOTE
            dailyQuote = random.choice(allQuotes)
            message = f"Your daily quote has arrived:\n{dailyQuote}"
            channels = [quoteChannelId1, quoteChannelId2, channelId3]
            for channel in channels:
                await send_message(channel, message)
            log_entry('Daily Quote was sent')
### MOON
            luna = lunar.phase()
            if luna != None:
                await send_message(moonChannelId1, luna)
                log_entry('Moon Phase was identified and sent.')
            log_entry("Daily Tasks Completed")
    
    @daily_task.before_loop
    async def before_daily_task(self):
        await self.bot.wait_until_ready()