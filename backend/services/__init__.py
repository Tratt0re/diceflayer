from services.telegrambot_service import TelegramBot
from init.confing import Config

config = Config()

# Initialize a TelegramBotService instance.
TelegramBotService = TelegramBot(token=config.get_param("telegram.bot.token"))