## Dependencies
* python-telegram-bot 13.7
* nltk
* scikit-learn

## Setting up

##### Clone the repo

```
$ git clone https://github.com/Lenainweb/TelegramBot.git

```

##### Initialize a virtualenv

```
$ python3.9 -m venv env_t_bot
$ . env_t_bot/bin/activate 
or
env_t_bot\Scripts\activate
```

##### Install the dependencies

```
$ pip install -r requirements.txt
```
##### Connecting a telegram token

```
$ cd TelegramBot
$ echo "TOKEN = 'your_telegram_token'" >> setting.py
```
## Bot launch

```
$ python bot.py
```
