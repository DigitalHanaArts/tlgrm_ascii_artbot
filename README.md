# TLGRM ASCII Art Bot

```text
╔══════════════════════════════════════╗
║          T L G R M   A S C I I       ║
║              A R T   B O T           ║
║                                      ║
║          D I G I T A L  H A N A      ║
║                 A R T S              ║
╚══════════════════════════════════════╝
````

A small Python Telegram bot that generates and sends random **ASCII word art** using [`pyfiglet`](https://github.com/pwaller/pyfiglet).

The bot randomly selects a word from a predefined list and renders it with a randomly chosen FIGlet font.

## Features

* Random ASCII-art words
* Random `pyfiglet` font selection
* Automatic scheduled messages
* Per-chat start/stop control
* Monospace formatting in Telegram
* Simple Python implementation
* Docker support

## Commands

| Command        | Description                        |
| -------------- | ---------------------------------- |
| `/start_ascii` | Start automatic ASCII-art messages |
| `/stop_ascii`  | Stop automatic messages            |

The current implementation sends a new ASCII-art message every **10 seconds**.

## Example

```text
  _    ____   ___ ___ ___
 / \  / ___| / __|_ _/ _ \
/ _ \ \___ \| (__ | | (_) |
/_/ \_\____/ \___|___\___/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/DigitalHanaArts/tlgrm_ascii_artbot.git
cd tlgrm_ascii_artbot
```

Install the dependencies:

```bash
pip install "python-telegram-bot[job-queue]" pyfiglet
```

Run the bot:

```bash
python TelegramAsciiBot.py
```

## Configuration

Create your Telegram bot with [@BotFather](https://t.me/BotFather) and provide its bot token to the application.

For a safer setup, store the token in an environment variable rather than committing it to the source code.

```bash
export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
```

Then use that variable in `TelegramAsciiBot.py`.

## Project

**Digital Hana Arts — Telegram ASCII Art Bot**

GitHub:
https://github.com/DigitalHanaArts/tlgrm_ascii_artbot

```

One important security issue: the code you pasted contains a **live Telegram bot token**. Since the GitHub repository is public, that token should be revoked/rotated through BotFather and replaced with an environment-variable-based configuration before committing the code. The repository currently contains `TelegramAsciiBot.py`, a `Dockerfile`, and a GitHub Actions workflow.
```
