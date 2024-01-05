import os


TELEGRAM_BOT_TOKEN: str = os.environ.get('TELEGRAM_BOT_TOKEN')  # type: ignore
REDIS_URL: str = os.environ.get('REDIS_URL')  # type: ignore

GOOGLE_SERVICE_ACCOUNT_FILENAME = '/app/.config/service_account.json'
DOWNLOAD_DIR = '/app/downloads'
SPREADSHEET_ID = '1h0racUvfHibYF8rgpzWZqbZ6N6FVOWbESoXeI4RmAFM'
