import requests
from bs4 import BeautifulSoup as bs
import difflib
from random import choice

def scrape(loc=''):
  "Scrape first"
  x = requests.get('https://avali.fandom.com/wiki/'+loc)
  s = bs(x.content, 'html.parser')
  test = s.find(id='mw-content-text').find_all("p")
  y = ''
  for x in test:
    y+='\n'+x.text
  return y

def image(loc=''):
  x = requests.get('https://avali.fandom.com/wiki/'+loc)
  s = bs(x.content, 'html.parser')
  links = []
  for link in s.find(id='mw-content-text').select("img[src^=http]"):
    lnk = link.get('src').split('/revision/')[0]
    links.append(lnk)
  return choice(links)
  

"Asking the bot; Who is avali?"
# Define out engine
class engine:
  def __init__(self,data):
    self.cur_line = ''
    self.keys = []
    self.location = None
    self.out = ''
    self.text = ''
    self.json = {}
    self.data = data.split('\n')
  
  def load(self,text,page=[]):
    self.page = page
    self.text = text
    self.keys = text.split(' ')
    self.proc()
    return self.get()

  def proc(self):
    json = {
      'keys':{
      },
    }
    for line in self.data:
      print('+++',line)
      for word in line.split(' '):
        print('---',word)
        if word in json['keys']:
          json['keys'][word]['locations'].append(self.data.index(line))
          json['keys'][word]['pages'].append(self.page)
        else:
          json['keys'][word] = {}
          json['keys'][word]['locations'] = [self.data.index(line)]
          json['keys'][word]['pages'] = [self.page]
    del json['keys']['']
    self.json = json

  def get(self):
    print(self.json)
    for key in self.text.split(' '):
      if key in self.json['keys']:
        print('===',self.json['keys'][key])
        return self.data[self.json['keys'][key]['locations'][0]]
    return 'Nothing found ¯\_(ツ)_/¯'

def remove_empty_from_dict(d):
    if type(d) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in d.items() if v and remove_empty_from_dict(v))
    elif type(d) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return d

#data = scrape()
## Input
#inp = 'Starbound'
## Create an engine instance
#e = engine(data)
## Load data into engine
#print(e.data)
#match = e.load(inp)
#print(match)
#
#