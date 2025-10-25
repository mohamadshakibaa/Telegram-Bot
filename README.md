# Telegram LLM Bot
A small Telegram bot that stores incoming messages in a local TinyDB database and lets designated admins trigger an LLM (OpenAI) completion for a stored message by reacting with 👍. Built with pyTelegramBotAPI (telebot), tinydb, and the OpenAI Python client.
## Features
- Stores every incoming Telegram message into `TinyDB` (`messages_db.json`).

- Admins can react to a message with 👍 in specified chats to have the bot call an LLM with the message text and replace a “working” reply with the LLM response.

- `/start` and `/help` commands return a welcome message.

- Simple, file-based DB handler with CRUD helpers.

## Repo structure (important files)
```python
.
├─ src/
│  ├─ bot.py             # Main bot logic and message/reaction handlers
│  ├─ config.py          # BOT_TOKEN, ADMINS_USERNAME, VALID_CHATS
│  ├─ constants.py       # WELCOME_MESSAGE
│  ├─ db.py              # TinyDB database wrapper (DBHandler)
│  ├─ llm.py             # OpenAI integration (call_llm function)
│  └─ messages_db.json   # Created automatically at runtime
│
├─ requirements.txt      # Python dependencies
└─ README.md

```

## Configuration
**Environment variables**
- `OPENAI_API_KEY` — **required** for `call_llm()`.

Fill in the following in `config.py`
```python
BOT_TOKEN = "123456:ABC-DEF..."         # Telegram bot token from BotFather
ADMINS_USERNAME = ["admin1", "admin2"] # list of admin Telegram usernames (without @)
VALID_CHATS = ["my_channel", "my_group"]  # allowed chat usernames (without @) where admin reactions work

```