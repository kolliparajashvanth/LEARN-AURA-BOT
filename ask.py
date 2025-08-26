from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.ai import gemini_reply


async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("❓ Please ask something after /ask.")
        return
    await update.message.reply_text("🤖 Thinking...")
    answer = gemini_reply(question)
    await update.message.reply_text(answer)


ask_handler = CommandHandler("ask", ask)
