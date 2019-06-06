import os
import plays
from application import Application

if __name__ == "__main__":
    base_dir = os.path.abspath(os.pardir)

    application = Application(base_dir=base_dir)
    application.boot()
    application.run(plays.default)
