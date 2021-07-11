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
  await ctx.send("Hey user i am online and working")
