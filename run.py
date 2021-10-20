from app import create_app
from threading import Thread

application = create_app('config.BaseConfig')

def run():
  application.run(host='0.0.0.0', port=80)

def keep_alive():
    server = Thread(target=run)
    server.start()