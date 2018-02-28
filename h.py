import discord
from discord.ext import commands

class Help:
	"""Shows the commands of SuperBot"""
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def h(self):
		"""Shows the commands of Tarik Bot"""
		server = "http://discord.gg/tarik"

		boi = (
			"This is the list of commands which most of the users use on regular\n"
			"basis Do `!help <command>` for more information on the command.")
		
		help = (
			"!h\n"
			"!help")
		help2 = (
			"Shows this message\n"
			"Shows more commands with more stuff! ")
		audio = (
			"!play\n"
			"!pause\n"
			"!skip\n"
			"!prev\n"
			"!stop\n"
			"!song\n"
			"!queue\n"
			"!yt")
		audio2 = (
			"Plays a song / link\n"
			"Pauses the playing song\n"
			"Votes to skip song.\n"
			"Goes back to previous song\n"
			"Stops song\n"
			"Shows information about current song\n"
			"Shows song queue\n"
			"Searches and plays song from YouTube")
		fun = (
			"!c\n"
			"!kill\n"
			"!insult\n"
			"!flip\n"
			"!8\n"
			"!rps\n"
			"!throw\n"
			"!lmgtfy\n"
			"!calc\n"
			"!choose\n")
		fun2 = (
			"Talk with Cleverbot. Mention also works.\n"
			"Kill anyone\n"
			"Insult anyone\n"
			"Flip table (or user)\n"
			"Ask 8 ball a question\n"
			"Play Rock Paper Scissors\n"
			"Throw stuff at user\n"
			"Generates LMGTFY Link\n"
			"Calculate stuff\n"
			"Choose between several items\n")
		leveler = (
			"!profile\n"
			"!rank\n"
			"!lvlset\n"
			"!profileinfo\n")
		leveler2 = (
			"Shows user profile.\n"
			"Shows user rank.\n"
			"Change your leveler settins (Global One)\n"
			"Shows more detailed info about any user.")

		econ = (
			"!bank register\n"
			"!payday\n"
			"!bank balance\n"
			"!bank transfer\n"
			"!slot")
		econ2 = (
			"Creates account at SuperBot Bank\n"
			"Gives you some $$$\n"
			"Shows your bank balance lmao\n"
			"Transfers your $$$ to another user\n"
			"Play slot with your money(Gambling). . .")
		bot = (
			"!info\n"
			"!stats\n"
			"!userinfo\n"
			"!uptime\n"
			"!updates\n"
			"!modhelp\n")
		bot2 = (
			"Shows bot information.\n"
			"Shows bot's statistics.\n"
			"Shows information related to user\n"
			"Shows for how long the bot was online for\n"
			"Shows the latest updates of SuperBot\n"
			"Shows the mod and owner commands.\n"
			"(^ONLY WORKS FOR USERS WITH \n"
			"`KICK MEMBERS` PERMISSION)")
		ot = (
			"Join the [SuperBot Community]({}) for more news and support!"
			"".format(server))

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Bot Commands", value=str(boi), inline=False)
		embed.add_field(name="Help", value=help)
		embed.add_field(name="Description", value=help2, inline=True)
		embed.add_field(name="Audio", value=audio)
		embed.add_field(name="Description", value=audio2)
		embed.add_field(name="Fun", value=fun, inline=True)
		embed.add_field(name="Description", value=fun2)
		embed.add_field(name="Economy", value=econ, inline=True)
		embed.add_field(name="Description", value=econ2, inline=True)
		embed.add_field(name="Leveler", value=leveler, inline=True)
		embed.add_field(name="Description", value=leveler2, inline=True)
		embed.add_field(name="Bot", value=bot, inline=True)
		embed.add_field(name="Description", value=bot2, inline=True)
		embed.add_field(name="Others", value=ot, inline=False)

		try:	
			await self.bot.say(":page_facing_up: **Check your private messages!**")
			await self.bot.whisper(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")
		
def setup(bot):
	bot.add_cog(Help(bot))
