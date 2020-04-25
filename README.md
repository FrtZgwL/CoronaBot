
# What is CoronaBot?

CoronaBot is a Telegram Bot that allows users to get a quick overview over
some relevant numbers about the corona-crisis. It does so by showing graphs
and charts that compare numbers for different countries.

# How do I set up CoronaBot?

You'll need [Python 3](https://www.python.org/downloads/) and these packages:

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)

Next get a Bot Token from the [Telegram BotFather](https://core.telegram.org/bots#3-how-do-i-create-a-bot).

Then clone this repository into some folder on your PC or on a server:

```shell
$ git clone https://github.com/FrtZgwL/CoronaBot
```

Now run `setup.py`:

```shell
$ cd CoronaBot
$ python3 setup.py
```
Paste your token in here when the script asks you for it.

We're almost done. Start `data_manager.py`:

```shell
$ python3 data_manager.py
```

This script will keep running in the background and get new data from the John Hopkins repository every day. Then start the bot:

```shell
$ python3 corona_bot.py
```

Congratiulations! Your CoronaBot is ready to go. Just text the bot you created with BotFather the command `/start` and the bot should work.

# Where does the data come from?

We are retreiving our corona-data from a git-hub repositoy of the [John Hopkins universety](https://github.com/CSSEGISandData/COVID-19/) We get country populations from [worldometers](www.Worldometers.info). The deathrate data is from the [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/rankorder/2066rank.html).


