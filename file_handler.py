from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes
from utils.file_utils import convert_file


async def file_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[InlineKeyboardButton("📂 Upload from local", callback_data="upload_local")]]
    await update.message.reply_text("📁 Choose upload method:", reply_markup=InlineKeyboardMarkup(buttons))


async def file_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    if not doc:
        return await update.message.reply_text("⚠️ Please upload a document.")
    file = await doc.get_file()
    file_path = await file.download_to_drive()
    converted_path = convert_file(file_path)
    if converted_path:
        await update.message.reply_document(document=open(converted_path, "rb"))
    else:
        await update.message.reply_text("❌ Conversion failed.")


def register_file_handlers(app):
    app.add_handler(CommandHandler("file", file_command))
    app.add_handler(MessageHandler(filters.Document.ALL, file_received))
