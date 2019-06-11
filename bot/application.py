import os
import logging
from pythonjsonlogger import jsonlogger
from dotenv import load_dotenv
import bot
import config

class Application:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.configuration = None
        self.booted = False

    def boot(self):
        # Load our secrets from dotenv
        load_dotenv(
            dotenv_path=os.path.join(self.base_dir, '.env'),
            override=True)

        # Load all of the JSON configuration files into our configuration object.
        self.load_config(path=os.path.join(self.base_dir, 'config/'))

        self.booted = True

    def load_config(self, path):
        configuration = config.Configuration()
        configuration.load(config.json_loader, path)

        self.configuration = configuration

    def run(self, play):
        if not self.booted:
            raise Exception('application has not been booted')

        session = bot.build(
            os.getenv('INSTAGRAM_USERNAME'),
            os.getenv('INSTAGRAM_PASSWORD'),
            self.configuration)

        # We need to call this explicitly as we disable it in case we fail to
        # build the bot.
        session.set_selenium_local_session()

        # Run the play
        play(session)
