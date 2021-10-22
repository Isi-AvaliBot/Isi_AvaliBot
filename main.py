print('Loading...')
import discord
from discord.ext import commands

from libs.scrape import scraper
from run import keep_alive
import database as db

from config import settings
import json
import requests
import libs.enc_dec as enc_dec
from libs.twiki import *
from libs.hook import hook
import libs.pain as pain
################
from libs.casher import cash
from time import sleep
import threading
cash = cash()
#cash.sync()

# Create thread to fetch images asynchronously
i_thread = threading.Thread(target=cash._check)
i_thread.start()
#while True:
#  sleep(1)
#  print('Получил',cash.request())
#######################

bot = commands.Bot(command_prefix=settings['prefix'])
bot.remove_command('help')
####

##############
@commands.cooldown(rate=1, per=7, type=commands.BucketType.user)
@bot.command()
async def help(ctx):
    #db.message(ctx.guild,ctx.author.id)
    x=0
    for server in bot.guilds:
      x+=1
      print(server.name)
    activeServers = bot.guilds
    summ = 0
    for s in activeServers:
      summ += len(s.members)
    summ = str(summ)
    await ctx.send(embed=discord.Embed(
        description=
        'use $ prefix before commands\n**enc <text>** - this function allows you to translate English into avali\n**dec <text>** - this function allows you to translate avalyn into english\n**awiki <text>** - allows you to search for information about avali on wikipedia\n**stbAwiki** - With this command you can access crafts, object appearances and quick references to the official wiki for a number of topics. \n**avali** - get a random picture of avali from the 1,500 library\n**team** - here you can find information about everyone who took part in the development of the bot\n**invite** - link to add a bot\n\n\n now the bot is on '+ summ +' servers\nDiscord server\nhttps://discord.gg/43NJF983jZ'
    ))

@bot.command()
async def ping(ctx):
  await ctx.send('Pong! {0}ms'.format(round(bot.latency, 1)))

@bot.command()
async def eeval(ctx):
  e = ctx.message.content.replace('^eeval ','')
  c = eval(e)
  await ctx.send(f'''Eval:
```
{c}
```''')


@commands.cooldown(rate=1, per=7, type=commands.BucketType.user)
@bot.command()
async def team(ctx):
    await ctx.send(embed=discord.Embed(
        title="coconut team",
        description=
        "<@385504411763605505> - discord bot | report an issue\n<@528586514213371915> - $encoder-decoder\n<@290350813828874241> - $avali\n<@351404235578933249> - new $awiki, $stbAwiki, cash system for $avali"
    ))

@bot.command()
async def awiki(ctx):
  msg = ctx.message.content.split(' ')
  loc=''
  msg = msg[1:]
  omsg=msg
  if 'in' in msg:
    loc = msg[1]
    omsg = msg[2:]
  import libs.twiki as twiki
  data = twiki.scrape(loc=loc)
  engine = twiki.engine(data)
  msg = engine.load(' '.join(omsg))
  embed=discord.Embed()
  embed.set_thumbnail(url=twiki.image(loc=loc))
  embed.add_field(name=str(' '.join(omsg)).upper(), value=msg, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def dbwiki(ctx):
  s = scraper()
  msg = ctx.message.content.split(' ')[1:]
  print(msg)
  if len(msg) == 0:
    s = s.map(loc='https://avali.fandom.com/wiki/Items')
    await ctx.send(embed = s)
  if len(msg) == 1:
    context = ' '.join(msg)
    e = s.map(loc='https://avali.fandom.com/wiki/Items',context=context)
    try:
      await ctx.send(embed = e)
    except:
      await ctx.send("Failed, did you specify in which category I should look? <:blep00:897749326745456651>")
  else:
    context = ' '.join(msg)
    s.load(loc='https://avali.fandom.com/wiki/Items',context=context)
    craft = s.get_craft(s.out)
    await ctx.send(embed = craft)

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

@commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
@bot.command()
async def coconut(ctx):
    await ctx.send(embed=discord.Embed(
        title=
        'кокос:coconut:кокоскокcoconut:coconut:кокосcoconutcockкокосcoconutcoconutкокос:coconut:'
    ))

#@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
#@bot.command()
#async def awiki(ctx):
#    wik = wiki.search(ctx.message.content)
#    await ctx.send(
#        embed=discord.Embed(title='maybe the answer is here ', description=wik)
#    )

@commands.cooldown(rate=1, per=7, type=commands.BucketType.user)
@bot.command()
async def avali(ctx):
    url = cash.request()
    embed=discord.Embed(title='Art by'+url.author)
    embed.set_image(url=url.uri)
    #imag = pain.ava()
    await ctx.send(embed=embed)

@commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
@bot.command()
async def invite(ctx):
  await ctx.send(embed= discord.Embed(title='https://discord.com/api/oauth2/authorize?client_id=876515016143147110&permissions=534723820608&scope=bot'))
  

import os,sys
# Error reporter
@bot.command()
async def restart(ctx):
  restart_bot()

def restart_bot(): 
  os.execv(sys.executable, ['poetry run python3'] + sys.argv)

@bot.event
async def on_command_error(ctx, error):
  h = hook()
  h.send(description=f"Command failed!\n{error}") 

@bot.event
async def on_ready():
  print('Bot is live!')
  h = hook()
  h.send(description="Bot started! ✅") 

#keep_alive()
bot.run  ('ODc2NTE1MDE2MTQzMTQ3MTEw.YRlMOA.q7Cq8x9ncI2tWrjVhyPxFK57RqM')
