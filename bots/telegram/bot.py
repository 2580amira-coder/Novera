from telegram.ext import Application

from config import BOT_TOKEN
from bots.telegram.handlers import setup_handlers


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    setup_handlers(app)

    print("🌍 Novera Bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()