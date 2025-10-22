from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Step 1: /start command — sends button to open your HTML Mini App
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "Open My App",
                web_app=WebAppInfo(url="https://yopc.github.io/Telegram-mini-app/")
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button below to open your app 👇", reply_markup=reply_markup)

# Step 2: Handle data coming back from your Mini App
async def handle_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.effective_message.web_app_data.data
    await update.message.reply_text(f"Received data from web app: {data}")

# Step 3: Run your bot
app = ApplicationBuilder().token("8403621556:AAHPBHCKqmZSvLv1IRdt2HTPiOsGPk5OQBA").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_data))

print("Bot is running...")
app.run_polling()
