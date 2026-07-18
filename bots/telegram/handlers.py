from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🌍 به Novera خوش آمدی!\n\n"
        "آماده ساخت امپراتوری خودت هستی؟ 👑"
    )


def setup_handlers(app):

    app.add_handler(
        CommandHandler("start", start)
    )