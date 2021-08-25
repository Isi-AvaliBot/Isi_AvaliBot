import discord
from discord.ext import commands
import time

from config import settings
import json
import requests

import enc_dec
import wiki
import pain

bot = commands.Bot(command_prefix = settings['prefix'])
bot.remove_command('help')


@bot.command()
async def help(ctx):
    await ctx.send(embed= discord.Embed(description = '**enc <text>** - this function allows you to translate English into aval\n**dec <text>** - this function allows you to translate avalyn into english\n**awiki <text>** - this function allows you to find information by keyword or phrase\n**avali** - get a random picture of avali from the 1,500 library\n**team** - here you can find information about everyone who took part in the development of the bot'))
@bot.command()
async def team(ctx):
    await ctx.send(embed= discord.Embed(title="coconut team", description = "<@385504411763605505> - discord bot | report an issue\n<@528586514213371915> - $encoder-decoder\n<@290350813828874241> - $avali"))
@bot.command()   
async def enc(ctx):
    enc = enc_dec.encoder(ctx.message.content.replace('$enc ', ''))
    await ctx.send(enc)
@bot.command()    
async def dec(ctx):
    dec = enc_dec.decoder(ctx.message.content.replace('$dec ', ''))
    await ctx.send(dec)
@bot.command()
async def coconut(ctx):
 await ctx.send(embed= discord.Embed(title=
    'кокос:coconut:кокоскокcoconut:coconut:кокосcoconutcockкокосcoconutcoconutкокос:coconut:'))
@bot.command()
async def awiki(ctx):
    wik = wiki.serch(ctx.message.content.replace('$wiki ', ''))
    await ctx.send(embed= discord.Embed(title='maybe the answer is here ', description = wik) )

@bot.command()
async def avali(ctx):
    avalik = pain.ava()
    await ctx.send(avalik) 

bot.run('ODc2NTE1MDE2MTQzMTQ3MTEw.YRlMOA.q7Cq8x9ncI2tWrjVhyPxFK57RqM')