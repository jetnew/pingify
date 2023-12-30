def ping(message):
    import os; import requests; import dotenv
    dotenv.load_dotenv(); requests.post(f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_API_KEY')}/sendMessage?chat_id={os.getenv('TELEGRAM_CHAT_ID')}&text={message}")

if __name__ == "__main__":
    ping("Hello World")
