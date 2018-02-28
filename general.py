import discord
from discord.ext import commands
from .utils.chat_formatting import *
from random import randint
from random import choice
from enum import Enum
from random import randint
from random import choice as randchoice
import datetime
import time
import aiohttp
import asyncio
import heapq


settings = {"POLL_DURATION" : 60}


class RPS(Enum):
    rock     = "\N{MOYAI}"
    paper    = "\N{PAGE FACING UP}"
    scissors = "\N{BLACK SCISSORS}"


class RPSParser:
    def __init__(self, argument):
        argument = argument.lower()
        if argument == "rock":
            self.choice = RPS.rock
        elif argument == "paper":
            self.choice = RPS.paper
        elif argument == "scissors":
            self.choice = RPS.scissors
        else:
            raise


class General:
    """General commands."""

    def __init__(self, bot):
        self.bot = bot
        self.stopwatches = {}
        self.ball = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                     "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                     "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
        self.poll_sessions = []

    @commands.command(pass_context=True)
    async def ping(self,ctx):
        """time-ping time"""
        channel = ctx.message.channel
        colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)        
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        em = discord.Embed(description="**Ping result:** {}ms".format(round((t2-t1)*1000)), colour=discord.Colour(value=colour))

        await self.bot.say(embed=em)

    @commands.command()
    async def choose(self, *choices):
        """Chooses between multiple choices.

        To denote multiple choices, you should use double quotes.
        """
        choices = [escape_mass_mentions(c) for c in choices]
        if len(choices) < 2:
            await self.bot.say('Not enough choices to pick from.')
        else:
            await self.bot.say(choice(choices))

    @commands.command(pass_context=True)
    async def roll(self, ctx, number : int = 100):
        """Rolls random number (between 1 and user choice)

        Defaults to 100.
        """
        author = ctx.message.author
        if number > 1:
            n = randint(1, number)
            await self.bot.say("{} :game_die: {} :game_die:".format(author.mention, n))
        else:
            await self.bot.say("{} Maybe higher than 1? ;P".format(author.mention))

    @commands.command(pass_context=True)
    async def flip(self, ctx, user : discord.Member=None):
        """Flips a coin... or a user.

        Defaults to coin.
        """
        if user != None:
            msg = ""
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = "Nice try. You think this is funny? How about *this* instead:\n\n"
            char = "abcdefghijklmnopqrstuvwxyz"
            tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
            table = str.maketrans(char, tran)
            name = user.display_name.translate(table)
            char = char.upper()
            tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z"
            table = str.maketrans(char, tran)
            name = name.translate(table)
            await self.bot.say(msg + "(╯°□°）╯︵ " + name[::-1])
        else:
            await self.bot.say("*flips a coin and... " + choice(["HEADS!*", "TAILS!*"]))

    @commands.command(pass_context=True)
    async def rps(self, ctx, your_choice : RPSParser):
        """Play rock paper scissors"""
        author = ctx.message.author
        player_choice = your_choice.choice
        red_choice = choice((RPS.rock, RPS.paper, RPS.scissors))
        cond = {
                (RPS.rock,     RPS.paper)    : False,
                (RPS.rock,     RPS.scissors) : True,
                (RPS.paper,    RPS.rock)     : True,
                (RPS.paper,    RPS.scissors) : False,
                (RPS.scissors, RPS.rock)     : False,
                (RPS.scissors, RPS.paper)    : True
               }

        if red_choice == player_choice:
            outcome = None # Tie
        else:
            outcome = cond[(player_choice, red_choice)]

        if outcome is True:
            await self.bot.say("{} You win {}!"
                               "".format(red_choice.value, author.mention))
        elif outcome is False:
            await self.bot.say("{} You lose {}!"
                               "".format(red_choice.value, author.mention))
        else:
            await self.bot.say("{} We're square {}!"
                               "".format(red_choice.value, author.mention))

    @commands.command(name="8", aliases=["8ball"])
    async def _8ball(self, *, question : str):
        """Ask 8 ball a question

        Question must end with a question mark.
        """
        if question.endswith("?") and question != "?":
            await self.bot.say("`" + choice(self.ball) + "`")
        else:
            await self.bot.say("That doesn't look like a question.")

    @commands.command(aliases=["sw"], pass_context=True)
    async def stopwatch(self, ctx):
        """Starts/stops stopwatch"""
        author = ctx.message.author
        if not author.id in self.stopwatches:
            self.stopwatches[author.id] = int(time.perf_counter())
            await self.bot.say(author.mention + " Stopwatch started!")
        else:
            tmp = abs(self.stopwatches[author.id] - int(time.perf_counter()))
            tmp = str(datetime.timedelta(seconds=tmp))
            await self.bot.say(author.mention + " Stopwatch stopped! Time: **" + tmp + "**")
            self.stopwatches.pop(author.id, None)

    @commands.command()
    async def lmgtfy(self, *, search_terms : str):
        """Creates a lmgtfy link"""
        search_terms = escape_mass_mentions(search_terms.replace(" ", "+"))
        await self.bot.say("http://lmgtfy.com/?q={}".format(search_terms))

    @commands.command(no_pm=True, hidden=True)
    async def hug(self, user : discord.Member, intensity : int=1):
        """Because everyone likes hugs

        Up to 10 intensity levels."""
        name = " *" + user.name + "*"
        if intensity <= 0:
            msg = "(っ˘̩╭╮˘̩)っ" + name
        elif intensity <= 3:
            msg = "(っ´▽｀)っ" + name
        elif intensity <= 6:
            msg = "╰(*´︶`*)╯" + name
        elif intensity <= 9:
            msg = "(つ≧▽≦)つ" + name
        elif intensity >= 10:
            msg = "(づ￣ ³￣)づ" + name + " ⊂(´・ω・｀⊂)"
        await self.bot.say(msg)

    @commands.command(pass_context=True, no_pm=True, aliases=["uinfo"])
    async def userinfo(self, ctx, *, user: discord.Member=None):
        """Check your userinfo or someone elses :P"""
        author = ctx.message.author
        server = ctx.message.server
    
        colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        if not user:
            user = author

        roles = [x.name for x in user.roles if x.name != "@everyone"]

        if user.status == discord.Status.dnd:
            m = "<:vpDnD:236744731088912384>DND"
        if user.status == discord.Status.offline:
            m = "<:vpOffline:212790005943369728>Offline/Invisible"
        if user.status == discord.Status.online:
            m = "<:vpOnline:212789758110334977>Online"
        if user.status == discord.Status.idle:
            m = "<:vpAway:212789859071426561>Idle"
        elif user.game is not None and user.game.url is True:
            m = "<:vpStreaming:212789640799846400> {} Is streaming !!".format(user.name)
        joined_at = self.fetch_joined_at(user, server)
        since_created = (ctx.message.timestamp - user.created_at).days
        since_joined = (ctx.message.timestamp - joined_at).days
        user_joined = joined_at.strftime("%d %b %Y %H:%M")
        user_created = user.created_at.strftime("%d %b %Y %H:%M")

        created_on = "{}\n({} days ago)".format(user_created, since_created)
        joined_on = "{}\n({} days ago)".format(user_joined, since_joined)

        if user.game is None:
            game = "Playing ⇒ Nothing at all ¯\_(ツ)_/¯".format(user.name)
        elif user.game.url is None:
            game = ":video_game: Playing ⇒ {}".format(user.game)
        else:
            game = "<:vpStreaming:212789640799846400> Streaming ⇒  [{}]({})".format(user.game, user.game.url)

        if roles:
            roles = sorted(roles, key=[x.name for x in server.role_hierarchy
                                       if x.name != "@everyone"].index)
            roles = ", ".join(roles)
        else:
            roles = ":walking: Nothing to see here ¯\_(ツ)_/¯\n\n"
        if user.nick is not None:
            ggez = "{}".format(user.nick)
        if user.nick is None:
            ggez = "None."

        if roles is None:
            user.colour = discord.Colour(value=colour)

        data = discord.Embed(description=game, colour=user.colour)
        data.add_field(name="Status", value=m)
        data.add_field(name="Joined Discord on", value=created_on)
        data.add_field(name="Nickname", value=ggez)
        data.add_field(name="Discriminator", value="#{}".format(user.discriminator))
        data.add_field(name="Highest role Colour", value="{}".format(user.colour))
        data.add_field(name="Joined this server on", value=joined_on)
        data.add_field(name="Roles", value=roles, inline=False)
        data.add_field(name="User ID", value=user.id)
        data.set_footer(text="{}".format(user.name), icon_url=user.avatar_url)


        if user.avatar_url:
            name = str(user)
            name = (name) if user.nick else name
            data.set_author(name=user.name, url=user.avatar_url)
            #data.set_thumbnail(url=user.avatar_url)
            data.set_image(url=user.avatar_url)

        else:
            data.set_author(name=user.name)

        try:
            await self.bot.say(embed=data)
        except discord.HTTPException:
            await self.bot.say("I need the `Embed links` permission "
                               "to send this")

    @commands.command(pass_context=True, no_pm=True, aliases=["sinfo"])
    async def serverinfo(self, ctx):
        """Shows server's info"""
        server = ctx.message.server
        invite = await self.bot.create_invite(ctx.message.server, unique=False)       
        online = len([m.status for m in server.members
                      if m.status == discord.Status.online])
        idle = len([m.status for m in server.members
                      if m.status == m.status == discord.Status.idle])
        dnd = len([m.status for m in server.members
                      if m.status == discord.Status.dnd])
        total_users = len(server.members)
        text_channels = len([x for x in server.channels
                             if x.type == discord.ChannelType.text])
        voice_channels = len(server.channels) - text_channels
        voice_channels = len(server.channels) - text_channels
        passed = (ctx.message.timestamp - server.created_at).days
        created_at = ("***Since***  ***`{}.`*** ***That's over***  ***`{}`***  ***days ago!***"
                      "".format(server.created_at.strftime("%d %b %Y %H:%M"),
                                passed))

        colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        x = -1
        emojis =  []
        while x < len([r for r in ctx.message.server.emojis]) -1:
            x = x + 1
            emojis.append("<:{}:{}>".format([r.name for r in ctx.message.server.emojis][x], [r.id for r in ctx.message.server.emojis][x]))

        online = len([e.name for e in server.members if e.status == discord.Status.online])
        offline = len([e.name for e in server.members if e.status == discord.Status.offline])
        idle = len([e.name for e in server.members if e.status == discord.Status.idle])
        dnd = len([e.name for e in server.members if e.status == discord.Status.dnd])
        total_users = str(len(server.members))
        total_bots = len([e.name for e in server.members if e.bot])
        text_channels = len([x for x in server.channels if str(x.type) == "text"])
        voice_channels = len(server.channels) - text_channels
        
        data = discord.Embed(
            description=created_at,
            colour=discord.Colour(value=colour))
        data.add_field(name="Region", value=str(server.region).upper())
        data.add_field(name="Total Users", value="{}".format(total_users))
        data.add_field(name="Total Bots", value=total_bots)
        data.add_field(name="Text Channels", value=text_channels)
        data.add_field(name="Voice Channels", value=voice_channels)
        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="Owner", value=str(server.owner.mention))
        data.add_field(name="Verification Level", value= str(server.verification_level))
        data.add_field(name="AFK Channel", value=str(server.afk_channel).upper())
        data.add_field(name="Afk Timeout", value="{}M".format(server.afk_timeout/60))
        data.add_field(name="Total emojis", value="{} ".format(len(server.emojis)))
        data.add_field(name="Users Status", value="{}{} Online Users.\n{}{} Offline Users.\n{}{} Idle Users\n{}{} Dnd Users\n\n{}__**Total users currently online:**__ __{}__".format("<:online:313956277808005120>", online, "<:offline:313956277237710868>",offline, "<:away:313956277220802560>", idle, "<:dnd:313956276893646850>", dnd,"<:online:313956277808005120><:away:313956277220802560><:dnd:313956276893646850>", online + idle + dnd))
        data.add_field(name="Server ID", value="{}".format(server.id))
        data.add_field(name="Server Invite", value="[Click Here]({})".format(invite))    
        data.set_image(url=server.icon_url) 
         
        data.set_footer(text="Tarik. Currently supporting {} servers.".format(len(self.bot.servers)), icon_url=self.bot.user.avatar_url)
        if server.icon_url:
            data.set_author(name="{}".format(server.name), url=server.icon_url)
            data.set_thumbnail(url=server.icon_url)
        else:
            data.set_author(name=server.name)
        if server.emojis:
            emotes = discord.Embed(title="Emotes", description=" ".join(emojis), colour=discord.Colour(value=colour))
        else:
            emotes = discord.Embed(title="Emotes", description=":no_good: ", colour=discord.Colour(value=colour))

        try:
            await self.bot.say(embed=data)
            await self.bot.say(embed=emotes)
        except discord.HTTPException:
            server = ctx.message.server
            x = -1
            emojis =  []
            while x < len([r for r in ctx.message.server.emojis]) -1:
                x = x + 1
                emojis.append("<:{}:{}>".format([r.name for r in ctx.message.server.emojis][x], [r.id for r in ctx.message.server.emojis][x]))
            online = len([e.name for e in server.members if e.status == discord.Status.online])
            offline = len([e.name for e in server.members if e.status == discord.Status.offline])
            idle = len([e.name for e in server.members if e.status == discord.Status.idle])
            dnd = len([e.name for e in server.members if e.status == discord.Status.dnd])
            total_users = str(len(server.members))
            text_channels = len([x for x in server.channels if str(x.type) == "text"])
            voice_channels = len(server.channels) - text_channels

            data = "```python\n"
            data += "Server Name: {}\n".format(server.name)
            data += "ID: {}\n".format(server.id)
            data += "Region: {}\n".format(server.region)
            data += "Users: {}\n".format(total_users)
            data += "Text channels: {}\n".format(text_channels)
            data += "Voice channels: {}\n".format(voice_channels)
            data += "Roles: {}\n".format(len(server.roles))
            data += "Verification Level: {}\n".format(str(server.verification_level))
            data += "Total emojis: {}\n".format(len(server.emojis))
            passed = (ctx.message.timestamp - server.created_at).days
            data += "Created: {} ({} days ago)\n".format(server.created_at, passed)
            data += "Owner: {}\n".format(server.owner)

            if server.icon_url != "":
                data += "Icon&Emojis:"
                data += "```"
                data += "{}\n".format(server.icon_url)
            if len(str(server.emojis)) < 6024 and server.emojis:
                data += " ".join([str(emoji) for emoji in server.emojis])
            else:
                data += "```"
            await self.bot.say(data)
            await self.bot.say("***ATTENTION*** **I am sending in This format because embed_links are not apart of my permissions Please enable all permissions including admininstrator to witness the bots full potential.**\n***(Btw info is missing lul)***")


    @commands.command(aliases=["ud"])
    async def urban(self, *, search_terms: str, definition_number: int = 1):
        """Urban Dictionary search
        Definition number must be between 1 and 10"""
        # definition_number is just there to show up in the help
        # all this mess is to avoid forcing double quotes on the user
        search_terms = search_terms.split(" ")
        colour = ''.join([randchoice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        try:
            if len(search_terms) > 1:
                pos = int(search_terms[-1]) - 1
                search_terms = search_terms[:-1]
            else:
                pos = 0
            if pos not in range(0, 11):  # API only provides the
                pos = 0  # top 10 definitions
        except ValueError:
            pos = 0
        search_terms = "+".join(search_terms)
        url = "http://api.urbandictionary.com/v0/define?term=" + search_terms
        try:
            async with aiohttp.get(url) as r:
                result = await r.json()
            if result["list"]:
                definition = result['list'][pos]['definition']
                likes = result['list'][pos]['thumbs_up']
                da_link = result['list'][pos]['permalink']
                example = result['list'][pos]['example']
                dislikes = result['list'][pos]['thumbs_down']
                author = result['list'][pos]['author']

                defs = len(result['list'])
                msg = ("***Definition #{} out of {}:\n***{}\n\n"
                       "**Example:\n**{}".format(pos + 1, defs, definition, example))
                msg = pagify(msg, ["\n"])
                for page in msg:
                    em = discord.Embed(description=page, colour=discord.Colour(value=colour))
                    em.set_footer(text="Urban Dictionary | Likes 👍{} | Dislikes 👎{} | Creator {}".format(likes, dislikes, author),
                                  icon_url=self.bot.user.avatar_url)
                    em.set_author(name="Definition For {}".format(search_terms),
                                  icon_url='http://www.dimensionalbranding.com/userfiles/urban_dictionary.jpg', url=da_link)
                    em.set_thumbnail(
                        url=self.bot.user.avatar_url)
                    await self.bot.say(embed=em)

            else:
                await self.bot.say(":x: **Your** **search terms gave no results.** :no_good:")
        except IndexError:
            await self.bot.say("There is no definition #{}".format(pos + 1))
        except:
            await self.bot.say("Error.")

    @commands.command(pass_context=True, no_pm=True)
    async def poll(self, ctx, *text):
        """Starts/stops a poll

        Usage example:
        poll Is this a poll?;Yes;No;Maybe
        poll stop"""
        message = ctx.message
        if len(text) == 1:
            if text[0].lower() == "stop":
                await self.endpoll(message)
                return
        if not self.getPollByChannel(message):
            check = " ".join(text).lower()
            if "@everyone" in check or "@here" in check:
                await self.bot.say("Nice try.")
                return
            p = NewPoll(message, self)
            if p.valid:
                self.poll_sessions.append(p)
                await p.start()
            else:
                await self.bot.say("poll question;option1;option2 (...)")
        else:
            await self.bot.say("A poll is already ongoing in this channel.")

    async def endpoll(self, message):
        if self.getPollByChannel(message):
            p = self.getPollByChannel(message)
            if p.author == message.author.id: # or isMemberAdmin(message)
                await self.getPollByChannel(message).endPoll()
            else:
                await self.bot.say("Only admins and the author can stop the poll.")
        else:
            await self.bot.say("There's no poll ongoing in this channel.")

    def getPollByChannel(self, message):
        for poll in self.poll_sessions:
            if poll.channel == message.channel:
                return poll
        return False

    async def check_poll_votes(self, message):
        if message.author.id != self.bot.user.id:
            if self.getPollByChannel(message):
                    self.getPollByChannel(message).checkAnswer(message)

    def fetch_joined_at(self, user, server):
        """Just a special case for someone special :^)"""
        if user.id == "96130341705637888" and server.id == "133049272517001216":
            return datetime.datetime(2016, 1, 10, 6, 8, 4, 443000)
        else:
            return user.joined_at

    @commands.command(pass_context=True, no_pm=True)
    async def topservers(self, ctx):
        """Shows the top 10 servers Tarik is in"""

        server = ctx.message.server
        ServCount = [None] * len(self.bot.servers)
        ServerId = [None] * len(self.bot.servers)
        i = 0
        for s in self.bot.servers:
            ServCount[i] = len(s.members)
            ServerId[i] = s.id
            i += 1

        top10 = heapq.nlargest(10, ServCount)

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        embed = discord.Embed(colour=discord.Colour(value=colour), title="Top 10 Servers.",
                              description="Here are the top 10 most popular servers that Tarik is in.")

        for i in range(0, 10):
            server = discord.utils.get(self.bot.servers, id=ServerId[ServCount.index(top10[i])])
            embed.add_field(name=str(i + 1) + ") " + server.name, value=str(top10[i]) + " Members", inline=False)

        await self.bot.say(embed=embed)


class NewPoll():
    def __init__(self, message, main):
        self.channel = message.channel
        self.author = message.author.id
        self.client = main.bot
        self.poll_sessions = main.poll_sessions
        msg = message.content[6:]
        msg = msg.split(";")
        if len(msg) < 2: # Needs at least one question and 2 choices
            self.valid = False
            return None
        else:
            self.valid = True
        self.already_voted = []
        self.question = msg[0]
        msg.remove(self.question)
        self.answers = {}
        i = 1
        for answer in msg: # {id : {answer, votes}}
            self.answers[i] = {"ANSWER" : answer, "VOTES" : 0}
            i += 1

    async def start(self):
        msg = "**POLL STARTED!**\n\n{}\n\n".format(self.question)
        for id, data in self.answers.items():
            msg += "{}. *{}*\n".format(id, data["ANSWER"])
        msg += "\nType the number to vote!"
        await self.client.send_message(self.channel, msg)
        await asyncio.sleep(settings["POLL_DURATION"])
        if self.valid:
            await self.endPoll()

    async def endPoll(self):
        self.valid = False
        msg = "**POLL ENDED!**\n\n{}\n\n".format(self.question)
        for data in self.answers.values():
            msg += "*{}* - {} votes\n".format(data["ANSWER"], str(data["VOTES"]))
        await self.client.send_message(self.channel, msg)
        self.poll_sessions.remove(self)

    def checkAnswer(self, message):
        try:
            i = int(message.content)
            if i in self.answers.keys():
                if message.author.id not in self.already_voted:
                    data = self.answers[i]
                    data["VOTES"] += 1
                    self.answers[i] = data
                    self.already_voted.append(message.author.id)
        except ValueError:
            pass

def setup(bot):
    n = General(bot)
    bot.add_listener(n.check_poll_votes, "on_message")
    bot.add_cog(n)
