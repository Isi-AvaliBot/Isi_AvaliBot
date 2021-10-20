#import requests
import random
import discord

import requests, json, random
from time import sleep

class image:
  # If requester is none, then image was just cashed
  def __init__(self, uri, id, author, requester=None):
    self.uri = uri
    self.req = requester 
    try:
      self.author = author.split(':')[1]
    except:
      print('Image has no author, breaking!')
      return 'Fail'
    self.id = id
  
  def __repr__(self):
    return f"Image object, ID: {self.id} by: {self.author} source: {self.uri} requester: {self.req}"

class cash:

  _u = 'https://api.vk.com/method/wall.search?owner_id=-186164216&query=%23avali&count=1&offset={0}&access_token=6666aad56666aad56666aad5c7661fa343666666666aad50747f80b4d281fa82d834e5a&v=5.123'

  def __init__(self):
    self.db = []
    self.cache_seq = None
    self.requester = None
  
  # To start syncing the db
  def sync(self):
    for x in range(20):
      i = self._new_fetch(random.randint(0,1250))
      if i[0]:
        pass
      else:
        print('Failed ✗\n')
    print(f'\nDone ✔ {len(self.db)}\n')


  def _new_fetch(self,num):
    r = requests.get(cash._u.format(num)).json
    x = r()
    uri = None
    max = 0
    try:
      for i in x.get('response').get('items')[0].get('attachments')[0].get('photo').get('sizes'):
        if i['height'] > max:
          max = i['height']
          uri = i['url']
    except:
      return [False]
    author = x['response']['items'][0]['text']
    self.create_i(uri,num,author)
    return [True,uri]
  
  def create_i(self,uri,id,author):
    try:
      i = image(uri,id,author)
      self.db.append(i)
      return True
    except:
      print('No Author :(')
  
  def request(self):
    i = random.choice(self.db)
    self.db.pop(self.db.index(i))
    return i
  
  def _check(self):
    while True:
      sleep(0.1)
      if len(self.db) < 15:
        print('\033[96m'+'Fetching new images...'+'\033[0m')
        self.sync()



#def ava():
 #oval = requests.get('https://api.vk.com/method/wall.search?owner_id=-186164216&query=%23avali&count=1&offset='+str(random.randint(0, 1520))+'&access_token=6666aad56666aad56666aad5c7661fa343666666666aad50747f80b4d281fa82d834e5a&v=5.123').json()
 #oval2 = oval.get('response').get('items')[0].get('attachments')[0].get('photo').get('sizes')
 #text = oval.get('response').get('items')[0].get('text')
 #embed=discord.Embed(title=text.replace('#furry', ''))
 #embed.set_image(url=oval2[len(oval2)-1].get('url'))
 #return embed
 