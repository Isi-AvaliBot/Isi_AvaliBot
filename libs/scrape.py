import requests
import discord
from bs4 import BeautifulSoup as bs
import difflib
from random import choice


class scraper:

  def __init__(self):
    self.out=None
    self.loc=None

  def load(self, loc, context=None):
    x = requests.get(loc)
    s = bs(x.content, 'html.parser')
    test = s.find(id='mw-content-text').find_all("a")
    y = {}
    for x in test:
      y[x.text] = loc.split('/wiki')[0]+x['href']
    print(context,y)
    self.name = context
    if ' ' in context:
      if context.split(' ')[0] in y:
        self.load(y[context.split(' ')[0]],context=' '.join(context.split(' ')[1:]))
      elif context in y:
        self.out = y[context]
      else:
        self.out = "Couldn't locate the parent in the links :/" 
    elif context in y:
      self.out = y[context]
    else:
      self.out = y
  
  def get_craft(self,link):
    x = requests.get(link)
    s = bs(x.content, 'html.parser')
    try:
      description = s.find(id='mw-content-text').find_all("p")[0].text
      while not description.strip():
        description = s.find(id='mw-content-text').find_all("p")[1].text
    except:
      print('No desc!')
      description = ''
    try:
      links= []
      for link in s.find(id='mw-content-text').select("img[src^=http]"):
        lnk = link.get('src').split('/revision/')[0]
        links.append(lnk)
      img = choice(links)
    except:
      img=None
      print('failed to get images :/')
    test = s.find(id='mw-content-text').find_all("li")
    x = []
    for y in test:
      x.append(y.text)
    self.loc = link
    return self.create_embed(self.name,description,x,image=img)
  
  def create_embed(self,name,description,items=[],image=None):
    embed=discord.Embed(title=name.upper(), description=description)
    if image is not None:
      embed.set_thumbnail(url=image)
    try:
      for i in items:
        print('I===',i)
        embed.add_field(name=i.split(' x')[0].strip(), value=i.split(' x')[1].strip(), inline=True)
    except:
      x = requests.get(self.loc)
      s = bs(x.content, 'html.parser')
      test = s.find(id='mw-content-text').find_all("a")
      y = {}
      for x in test:
        l = self.loc.split('/wiki')[0]+x['href']
        embed.add_field(name=x.text, value = f"{l} for more", inline=False)
    return embed
  
  def map(self,loc,context=None):
    if context is not None:
      x = requests.get(loc.split('/Items')[0]+'/'+context)
      print('URL===',loc.split('/Items')[0]+'/'+context)
    else:
      x = requests.get(loc)
    s = bs(x.content, 'html.parser')
    test = s.find(id='mw-content-text').find_all("a")
    y = {}
    for x in test:
      print(x)
      if 'create this page' in x.text:
        embed=discord.Embed(title="Category doesn't exist")
        return embed
      if x.text != context:
        y[x.text] = loc.split('/wiki')[0]+x['href']
    #embed.set_thumbnail(url=)
    if context is not None:
      embed=discord.Embed(title=context.upper())
      for i in y:
        embed.add_field(name=i, value = f"`scrape {context} {i}` for more", inline=False)
      return embed
    else:
      embed=discord.Embed(title="CATEGORIES")
      for i in y:
        embed.add_field(name=i, value = f"`scrape {i}` for more", inline=False)
      return embed