import discord
from discord.ext import commands
from Cybernator import Paginator as page
import random

from config import settings
import json
import requests


import enc_dec
import wiki

from casher import cash
import threading
cash = cash()
cash.sync()

i_thread = threading.Thread(target=cash._check)
i_thread.start()

bot = commands.Bot(command_prefix = settings['prefix'])
bot.remove_command('help')


@commands.cooldown(rate=1, per=7, type=commands.BucketType.user)
@bot.command()
async def help(ctx):
    x=0
    for server in bot.guilds:
      x+=1
      print(server.name)
    activeServers = bot.guilds
    summ = 0
    for s in activeServers:
      summ += len(s.members)
    summ = str(summ)
    await ctx.send(embed= discord.Embed(description = 'use $ prefix before commands\n**enc <text>** - this function allows you to translate English into avali\n**dec <text>** - this function allows you to translate avalyn into english\n**awiki <text>** - allows you to search for information about avali on wikipedia\n**stbAwiki** - With this command you can access crafts, object appearances and quick references to the official wiki for a number of topics. \n**avali** - get a random picture of avali from the 1,500 library\n**team** - here you can find information about everyone who took part in the development of the bot\n**invite** - link to add a bot\n\n\n now the bot is on '+ summ +' servers\nDiscord server\nhttps://discord.gg/43NJF983jZ'))
@commands.cooldown(rate=1, per=7, type=commands.BucketType.user)
@bot.command()
async def team(ctx):
    await ctx.send(embed= discord.Embed(title="coconut team", description = "<@385504411763605505> - discord bot | report an issue\n<@528586514213371915> - $encoder-decoder\n<@290350813828874241> - $avali\n<@351404235578933249> - new $awiki, $stbAwiki, cash system for $avali"))
@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)    
@bot.command()   
async def enc(ctx):
    enc = enc_dec.encoder(ctx.message.content.replace('$enc ', ''))
    await ctx.send(enc)
@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)    
@bot.command()    
async def dec(ctx):
    dec = enc_dec.decoder(ctx.message.content.replace('$dec ', ''))
    await ctx.send(dec)
@commands.cooldown(rate=1, per=30, type=commands.BucketType.user)    
@bot.command()
async def invite(ctx):
  await ctx.send(embed= discord.Embed(title='https://discord.com/api/oauth2/authorize?client_id=876515016143147110&permissions=534723820608&scope=bot'))


@commands.cooldown(rate=1, per=120, type=commands.BucketType.user)    
@bot.command()
async def coconut(ctx):
 await ctx.send(embed= discord.Embed(title=
    'кокос:coconut:кокоскокcoconut:coconut:кокосcoconutcockкокосcoconutcoconutкокос:coconut: 0.7.3\n - new wiki'))
@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)    
@bot.command()

async def avali(ctx):
    url = cash.request()
    embed=discord.Embed(title='Art by'+url.author)
    embed.set_image(url=url.uri)
    #imag = pain.ava()
    await ctx.send(embed=embed)






#0/7.2










#буква+
bot.run('ODc2NTE1MDE2MTQzMTQ3MTEw.YRlMOA.q7Cq8x9ncI2tWrjVhyPxFK57RqM')