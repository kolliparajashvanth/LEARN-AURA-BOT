from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes
from utils.books import get_textbook_links


async def textbooks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[InlineKeyboardButton(f"Class {i}", callback_data=f"class_{i}")] for i in range(6, 13)]
    await update.message.reply_text("📘 Choose your class:", reply_markup=InlineKeyboardMarkup(buttons))


async def class_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    class_num = query.data.split("_")[1]
    books = get_textbook_links(int(class_num))
    if not books:
        await query.edit_message_text("🚫 No books found.")
        return
    buttons = [
        [InlineKeyboardButton(book['subject'], callback_data=f"book_{class_num}_{i}")]
        for i, book in enumerate(books)
 ]
    context.user_data[f"class_{class_num}_books"] = books
    await query.edit_message_text(
        f"📚 Subjects for Class {class_num}:", reply_markup=InlineKeyboardMarkup(buttons)
    )


async def book_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    _, class_num, idx = query.data.split("_")
    books = context.user_data.get(f"class_{class_num}_books", [])
    book = books[int(idx)]
    await query.edit_message_text(
        f"📖 {book['subject']}\n\n"
        f"[📥 Download]({book['download']}) | [🌐 Read Online]({book['online']})",
        parse_mode='Markdown'
    )


def register_textbook_handlers(app):
    app.add_handler(CommandHandler("textbooks", textbooks))
    app.add_handler(CallbackQueryHandler(class_handler, pattern=r"class_\d+"))
    app.add_handler(CallbackQueryHandler(book_handler, pattern=r"book_\d+_\d+"))


