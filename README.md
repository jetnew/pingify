# Pingify

Ping notifications to a Telegram bot.

## Set-up

1. Go to BotFather (@BotFather) on Telegram and create a new bot (/newbot) to get your bot token.
2. Go to your bot and click Start (/start).
3. Get your chat id (also user id), e.g. from @userinfobot, @username_to_id_bot, or @get_id_bot.
4. Create a .env file with both bot token (TELEGRAM_BOT_API_KEY) and chat id (TELEGRAM_CHAT_ID):

    ```.env
    TELEGRAM_BOT_API_KEY=X:Y
    TELEGRAM_CHAT_ID=123
    ```

5. Install dependencies with `pip3 install -r requirements.txt`.
6. Load the ping function (at pingify.py):

    ```python3
    def ping(message):
        import os; import requests; import dotenv
        dotenv.load_dotenv(); requests.post(f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_API_KEY')}/sendMessage?chat_id={os.getenv('TELEGRAM_CHAT_ID')}&text={message}")
    ```

7. Run `ping("Hello world!")` in your Python file.