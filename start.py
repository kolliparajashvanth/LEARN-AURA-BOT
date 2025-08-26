from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, CallbackQueryHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to LearnAuraBot!\n\n"
        "📚 Features:\n"
        "/ask - Ask AI any question\n"
        "/search - Search the web\n"
        "/textbooks - NCERT & Diploma books\n"
        "/file - Upload & convert files\n"
    )


start_handler = CommandHandler("start", start)


# Function to handle button taps on the start menu
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()


    data = query.data
    if data == "textbooks":
        await query.message.reply_text("📘 Please select your class to view textbooks:")
        # Actual class options are handled in `handlers/textbooks.py`
    elif data == "ask_ai":
        await query.message.reply_text("💬 Use /ask followed by your question to talk to the AI.")
    elif data == "search":
        await query.message.reply_text("🔍 Use /search followed by your topic to look it up.")
    elif data == "file_transfer":
        await query.message.reply_text("📁 Upload a file to convert using /file.")
    elif data == "manual":
        await query.message.reply_text(
            "📖 *User Manual:*\n"
            "/start - Show main menu\n"
            "/ask - Ask anything to AI\n"
            "/search - Search any topic\n"
            "/file - Upload and convert files\n"
            "/textbooks - Browse textbooks\n"
            "/manual - Show this guide",
            parse_mode="Markdown"
        )
    else:
        await query.message.reply_text("⚠️ Unknown action.")


# Exported handlers
start_handler = CommandHandler("start", start)
button_handler = CallbackQueryHandler(button_handler)
