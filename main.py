import os
from telegram.ext import ApplicationBuilder
from handlers.start import start_handler
from handlers.ask import ask_handler
from handlers.search import search_handler
from handlers.textbooks import register_textbook_handlers
from handlers.file_handler import register_file_handlers
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(start_handler)
    app.add_handler(ask_handler)
    app.add_handler(search_handler)
    register_textbook_handlers(app)
    register_file_handlers(app)
    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
