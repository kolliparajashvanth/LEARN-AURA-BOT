from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.searcher import search_serpapi


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("🔎 Please enter a search term after /search.")
        return
    await update.message.reply_text("🔍 Searching the web...")
    results = search_serpapi(query)
    await update.message.reply_text(results)


search_handler = CommandHandler("search", search)