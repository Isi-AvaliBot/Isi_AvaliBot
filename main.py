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
 await ctx.send(
    'кокоскокоскокcoconutкокосcoconutcockкокосcoconutcoconutкокос https://cdn.discordapp.com/attachments/845189247824822315/876813997905686558/cock.jpg'
    )
@bot.command()
async def awiki(ctx):
    wik = wiki.serch(ctx.message.content.replace('$wiki ', ''))
    await ctx.send(wik) 

@bot.command()
async def avali(ctx):
    avalik = pain.ava()
    await ctx.send(avalik) 
 

bot.run(settings['token'])