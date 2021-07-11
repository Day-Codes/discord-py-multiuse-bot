import discord
import os
from discord.ext import commands
import keep_alive  
import random 

client = commands.Bot(command_prefix = commands.when_mentioned_or("#"),case_insensitive=True, help_command=None)

@client.event
async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Senko | #help"))
        print('Hello!')
        print('The bot has been turn on ;)')
        print(f'I have successfully logged in as {client.user.name}#{client.user.discriminator}!')
        print(f'My prefix is #')

@client.command()
async def help(ctx): 
        embed = discord.Embed(title="Help command!", description="prefix is `#`", color=0x00FFFF)
        embed.add_field(name=f"help", value="Show this embed", inline=False)
        embed.add_field(name=f"ping", value="Tells you the latency of senko", inline=False)
        embed.add_field(name=f"setdelay", value=f"Channel slowmode", inline=False)
        embed.add_field(name=f"warn", value="Warns user", inline=False)
        embed.add_field(name=f"kick", value="kick user", inline=False)
        embed.add_field(name=f"ban", value="ban user", inline=False)
        embed.add_field(name=f"test", value="Test command", inline=False)
        embed.add_field(name=f"pog", value="Say pog", inline=False)
        embed.add_field(name=f"water", value="joke cmds", inline=False)
        embed.add_field(name=f"deadchat", value="send a dead chat gif", inline=False)
        embed.add_field(name=f"devinfo", value="about dev", inline=False)
        embed.add_field(name=f"members", value="tell server members", inline=False)
        embed.add_field(name=f"kill", value="fun kill cmds", inline=False)
        embed.add_field(name=f"top_gg", value="Dev top.gg profile", inline=False)
        embed.add_field(name=f"simp", value="simp xD", inline=False)
        embed.add_field(name=f"drama", value="lol!", inline=False)
        embed.add_field(name=f"music", value="Spotify playlist", inline=False)
        embed.add_field(name=f"coinflip", value="flip da coin", inline=False)
        embed.add_field(name=f"COMMAND BROKE", value="CMDS", inline=False)
        embed.add_field(name=f"cool", value="tell someone there cool", inline=False)
        embed.add_field(name=f"welcome", value="welcome a user in main chat", inline=False)
        embed.add_field(name=f"jokes", value="tell jokes", inline=False)
        embed.add_field(name=f"invite", value="bot invite", inline=False)
        embed.add_field(name=f"prefix", value="prefix", inline=False)
        embed.add_field(name=f"senko", value="got to look", inline=False)
        embed.add_field(name=f"cool", value="tell someone there cool", inline=False)
        
        await ctx.message.delete()
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator = True)
async def setdelay(ctx, seconds: int):
    await ctx.message.delete()
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

@client.command()
@commands.has_permissions(manage_messages = True)
async def warn(ctx,user: discord.Member,*,reason):
  embed = discord.Embed(title="Warning!", description=f"{user.mention} has been warned by {ctx.author.mention} | Reason: {reason}",color=0x00FFFF)
  await ctx.message.delete()
  await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'User {member} has been kicked.')

@client.command(description='Bans a Member: Admin Perms Only')
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
	if reason == None:
		await user.ban(reason=reason)
		await ctx.send(f'{user} was banned by {ctx.author.mention} | Reason: **NO REASON PROVIDED**')
	else:
		await user.ban(reason=reason)
		await ctx.send(
		    f'{user} was banned by {ctx.author.mention} | Reason: **{reason}**')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def test(ctx):
  await ctx.send("Hey user i am online and working if found a bug please email daylndevbotv@gmail.com for bug reporting!")


@client.command()
async def pog(ctx):
  await ctx.send("POOOOOOOOOOOG")
 

@client.command()
async def water(ctx):
 await ctx.send('Water is yummy :D I order everyone to drink water RIGHT NOW! xD')

@client.command()
async def deadchat(ctx):
 await ctx.message.delete()
 await ctx.send('https://tenor.com/view/chat-dead-text-death-gif-19179369')



@client.command()
async def devinfo(ctx):
 await ctx.message.delete()
 await ctx.send('Bot Dev: `Dayln#1506` About dev: ` I been an bot dev for over 3 months and an Top.gg bot dev!`')

 @client.command()
 async def members(ctx):
        embed = discord.Embed(title="", description="", color=0x00FFFF)
        embed.add_field(name="Member Count:", value=f"There are currently **{ctx.guild.member_count}** in **{ctx.guild.name}**!", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

@client.command(pass_context = True)
async def kill(ctx, member: discord.Member):
    kill_messages = [
        f'{ctx.message.author.mention} killed {member.mention} with a baseball bat!', 
        f'{ctx.message.author.mention} killed {member.mention} with a frying pan!',
        f'{ctx.message.author.mention} tried to kill {member.mention} by burning his hands off, but {member.mention} pulled a tricky-trick and burnt {ctx.author.mention}\'s hands off instead ;)',
        f'{ctx.message.author.mention} attempted to murder {member.mention} but .. NAH!'
    ]  # This is where you will have your kill messages. Make sure to add the mentioning of the author (ctx.message.author.mention) and the member mentioning (member.mention) to it
    await ctx.send(random.choice(kill_messages))
    await ctx.message.delete()


@client.command()
async def top_gg(ctx):
  await ctx.message.delete()
  await ctx.send('Bot dev top.gg profile: `https://top.gg/user/673011572225998856`!')

@client.command()
async def simp(ctx):
  await ctx.message.delete()
  await ctx.send('SIMP!! WE FOUND AN SIMP LMAO xD')


@client.command()
async def drama(ctx):
  await ctx.message.delete()
  await ctx.send('*Grabs popcorn and pop* Nice Drama! I like watching drama! :D')


@client.command()
async def music(ctx):
 await ctx.message.delete()
 await ctx.send('An spotify playlist: https://spoti.fi/3qLa4hy')


 @client.command(pass_context = True)
 async def coinflip(ctx):
    coin = [
        f'Head', 
        f'Tails',f'oops it fell']
        
   
    await ctx.send(random.choice(coin))
    await ctx.message.delete()



 @client.command(pass_context = True)
 async def gifs(ctx):
    gif = [
        f'https://tenor.com/view/excited-dance-funny-monkey-gif-12662007', 
        f'https://tenor.com/view/fat-guy-dancing-moves-gif-14156580',f'https://tenor.com/view/cat-computer-gif-5368357','https://tenor.com/view/code-monkey-checkmate-digital-monkey-business-working-monkey-coding-monkey-gif-13322953','https://tenor.com/view/code-monkey-z-gif-19267489','https://tenor.com/view/code-monkey-z-gif-19267489','https://tenor.com/view/monkey-bnoc-gif-19296594',]
        
   
    await ctx.send(random.choice(gif))
    await ctx.message.delete()


@client.command()
async def cool(ctx, member: discord.Member):
  await ctx.send(f'{member.mention} {ctx.author.mention} thinks your cool')
  await ctx.message.delete()


@client.command()
async def welcome(ctx, member: discord.Member):
  await ctx.send(f'{member.mention} {ctx.author.mention} welcomes you!')
  await ctx.message.delete()

@client.command()
async def invite(ctx):
  await ctx.send("here! https://bit.ly/3x8CKEA")
  await ctx.message.delete()

@client.command(pass_context = True)
async def jokes(ctx):
    joke = [
        f'What do dentists call their x-rays? Tooth pics!', 
        f'Did you hear about the first restaurant to open on the moon? It had great food, but no atmosphere.',f'What did one ocean say to the other ocean? Nothing, it just waved.','Do you want to hear a construction joke? Sorry, I’m still working on it.','Did you hear about the fire at the circus? It was in tents','What does a nosey pepper do? It gets jalapeño business. ']
        
   
    await ctx.send(random.choice(joke))
    await ctx.message.delete()

@client.command()
async def prefix(ctx, member: discord.Member):
  await ctx.send(f'{member.mention} the prefix is: #')
  await ctx.message.delete()

@client.command()
async def senko(ctx, member: discord.Member):
  await ctx.send(f'{member.mention} SENNNNNNNNNKO')
  await ctx.message.delete()

@client.command()
async def cool(ctx, member: discord.Member):
  await ctx.send(f'{member.mention} {ctx.author.mention} thinks your cool')
  await ctx.message.delete()
    
    
keep_alive.keep_alive()
token = os.environ.get("TOKEN")
client.run(token)



