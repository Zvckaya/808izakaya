import asyncio,discord
from discord.ext import commands

token= "ODEzMjMzNzE2Nzg4NDYxNTgw.YDMU6w.8gwyq7JZz_6wfjpLccrdqVcN7dc"
game = discord.Game("BIGBROTHER")

bot = commands.Bot(command_prefix='!',status=discord.Status.online,activity=game)

@bot.event
async def on_ready():
    print("봇시작")

@bot.command()
async def 도움(ctx):
    await ctx.send("무엇을 도와드릴까요")

@bot.command()
async def 인사말(ctx):
    embed = discord.Embed(title="808IZAKAYA",description="808 SOUND",color=0xf3bb76)
    embed.add_field(name="about us",value="808DEB")
    await ctx.send(embed=embed)
    



bot.run(token)