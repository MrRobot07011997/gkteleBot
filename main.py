
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8110407526:AAHJeSibbNa_bODyOzbRHDUgX_KELt2apbw"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        welcome_msg = f"✨ Welcome, {member.first_name}! ✨\n🎉 We're glad to have you here in GKMOVIES !\n🚀 Enjoy Movies and have fun! 😊"
        await update.message.reply_text(welcome_msg)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    
    print("Bot starting...")
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
