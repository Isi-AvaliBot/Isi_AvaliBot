import requests 

class hook:
  def __init__(self):
    self.url = "https://discord.com/api/webhooks/1038027338178379817/kmSpIdih2IxBFOjtHCos2iiSl4Mnkh1FnivTuNYa5FhwbUg5DLYqOfV1id_cqkMBDelo"
    
    
  def send(self,content="",description=""):
    data = {
    "content" : content,
    "username" : "Isi Status"
    }

    data["embeds"] = [
        {
            "description" : description,
            "title" : "Isi Status Notifier"
        }
    ]
    result = requests.post(self.url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

