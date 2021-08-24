import requests
import random

def ava():
 oval = requests.get('https://api.vk.com/method/wall.search?owner_id=-186164216&query=%23avali&count=1&offset='+str(random.randint(0, 1494))+'&access_token=6666aad56666aad56666aad5c7661fa343666666666aad50747f80b4d281fa82d834e5a&v=5.123').json()
 oval2 = oval.get('response').get('items')[0].get('attachments')[0].get('photo').get('sizes')
 return oval2[len(oval2)-1].get('url')