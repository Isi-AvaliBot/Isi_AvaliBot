import discord
from discord.ext import commands
import time
from Cybernator import Paginator as page
import random

from config import settings
import json
import requests

import enc_dec
import wiki
import pain

bot = commands.Bot(command_prefix = settings['prefix'])
bot.remove_command('help')


@commands.cooldown(rate=1, per=7, type=commands.BucketType.user)
@bot.command()
async def help(ctx):
    await ctx.send(embed= discord.Embed(description = '**enc <text>** - this function allows you to translate English into aval\n**dec <text>** - this function allows you to translate avalyn into english\n**awiki <text>** - this function allows you to find information by keyword or phrase\n**awikihelp** - list of requests for **awiki**\n**avali** - get a random picture of avali from the 1,500 library\n**team** - here you can find information about everyone who took part in the development of the bot'))
@commands.cooldown(rate=1, per=7, type=commands.BucketType.user)
@bot.command()
async def team(ctx):
    await ctx.send(embed= discord.Embed(title="coconut team", description = "<@385504411763605505> - discord bot | report an issue\n<@528586514213371915> - $encoder-decoder\n<@290350813828874241> - $avali"))
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
@commands.cooldown(rate=1, per=1, type=commands.BucketType.user)    
@bot.command()
async def coconut(ctx):
 await ctx.send(embed= discord.Embed(title=
    'кокос:coconut:кокоскокcoconut:coconut:кокосcoconutcockкокосcoconutcoconutкокос:coconut: 0.6.3'))
@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)    
@bot.command()
async def awiki(ctx):
    wik = wiki.serch(ctx.message.content)
    await ctx.send(embed= discord.Embed(title='maybe the answer is here ', description = wik) )
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@bot.command()
async def avali(ctx):
     imag = pain.ava()
     await ctx.send(embed=imag) 


@commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
@bot.command()    
async def awikihelp(ctx):
    embed1 = discord.Embed(title='page 1', description='A\nammonia\narmor\naugmentation\nC\nculture\nD\ndifferences\ndomestic technology\ndrone\nF\nfactions\nflight\nG\ngovernance\ngrowth')
    embed2 = discord.Embed(title='page 2', description='H\nheight\nhousehold\nhow many live\nI\nIlluminate\nindependent worlds\nK\nknown worlds\nL\nlength\nM\nmedicine\nN\nnexus')
    embed3 = discord.Embed(title='page 3', description='P\npack\nR\nreproduction\nS\nscientific\nsize\nspace\nspace discovery\nsurvival\nT\ntechnology\ntribe\nW\nweaponry\nwings')
    em = [embed1, embed2, embed3]
    message = await ctx.send(embed=embed1)
    pag = page(bot, message, only=ctx.author, use_more=False, embeds=em)
    await pag.start()





#0/6/2










#буква+
bot.run('ODc2NTE1MDE2MTQzMTQ3MTEw.YRlMOA.q7Cq8x9ncI2tWrjVhyPxFK57RqM')