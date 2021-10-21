import requests 

class hook:
  def __init__(self):
    self.url = "https://discord.com/api/webhooks/900695112168910869/rrFLDxnz-zHKCh5qeOW2OXJEMgnNMBXMj7MLncpayYRB5laLOL2J1XdhdzPShDep5CMu"
    
    
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

