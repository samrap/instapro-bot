import glob
import json

class Configuration:
    def __init__(self):
        self.all = {}

    def load(self, load_func, *load_args):
        if callable(load_func):
            self.all = load_func(*load_args)

    def get(self, key, default=None):
        if key in self.all:
            return self.all[key]
        return default

def json_loader(path):
    files = [f for f in glob.glob(path + "*.json")]
    config = {}
    for f in files:
        with open(f) as json_file:
            config.update(json.load(json_file))
    return config
