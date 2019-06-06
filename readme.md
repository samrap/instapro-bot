# instapro-bot

A framework for running the [InstaPy](https://github.com/timgrossmann/InstaPy) Instagram bot

InstaPy is a fantastic bot for automating Instagram interactions, but can be a little messy to work with. This is a WIP Python framework that allows you to set basic configurations using dotenv and JSON, while defining the actual interactions as _plays_. A play is simply a function you pass to `Application.run` which receives an InstaPy session already configured with everything you need.

! This is a WIP !
