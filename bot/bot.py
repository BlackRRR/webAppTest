from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater
from dotenv import load_dotenv
import os


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def run_bot(token: str) -> None:
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("Starting the bot...")
    app.run_polling()


if __name__ == "__main__":
    load_dotenv()  # load variables from .env file (don't forget to fill it!)

    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("Invalid BOT_TOKEN in .env file")

    run_bot(
        token=bot_token
    )
