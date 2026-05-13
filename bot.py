from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 8942399232:AAEyz0UK9ZEi77w9YTAlHKXSXlG2u313lio

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ø§Ù„Ø¨ÙˆØª ÙŠØ¹Ù…Ù„ Ø¨Ù†Ø¬Ø§Ø­ ðŸš€")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()