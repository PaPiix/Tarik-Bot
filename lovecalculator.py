import discord
from discord.ext import commands
try:
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
import aiohttp

class LoveCalculator:
    """Calculate the love percentage for two users!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lovecalc'])
    async def lovecalculator(self, lover: discord.Member, loved: discord.Member):
        """Calculate the love percentage!"""

        x = lover.display_name
        y = loved.display_name

        url = 'https://www.lovecalculator.com/love.php?name1={}&name2={}'.format(x.replace(" ", "+"), y.replace(" ", "+"))
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
            try:
                description = soupObject.find('div', attrs={'class': 'result score'}).get_text().strip()
            except:
                description = 'Dr. Love is busy right now'

        try:
            z = description[:2]
            z = int(z)
            if z > 50:
                emoji = '❤'
            else:
                emoji = '💔'
            title = 'Dr. Love says that the love percentage for {} and {} is:'.format(x, y)
        except:
            emoji = ''
            title = 'Dr. Love has left a note for you.'
            
        description = emoji + ' ' + description + ' ' + emoji
        em = discord.Embed(title=title, description=description, color=discord.Color.red())
        await self.bot.say(embed=em)

def setup(bot):
    if soupAvailable:
        bot.add_cog(LoveCalculator(bot))
    else:
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")
