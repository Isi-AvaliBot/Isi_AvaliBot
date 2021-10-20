from app import create_app
from threading import Thread

application = create_app('config.BaseConfig')

def run():
  application.run(port=5000)

def keep_alive():
    server = Thread(target=run)
    server.start()