from app import create_app
import os
from threading import Thread

application = create_app('config.BaseConfig')

def run():
  application.run(port=int(os.environ.get('PORT', 33507)))

def keep_alive():
    server = Thread(target=run)
    server.start()