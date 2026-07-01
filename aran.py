import telebot

TOKEN = "8988223662:AAGXpaW0vcnjHpRPPfD0PaNx_S67Fg1g43I"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "✨ بەخێربێیت بۆ بۆتی A R A N\n\n"
        "📩 هەر پەیامێک بنێرە، من وەڵامت دەدەم."
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(
        message,
        "📖 فەرمانەکان:\n"
        "/start - دەستپێکردنی بۆت\n"
        "/help - یارمەتی"
    )

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(
        message,
        f"📨 پەیامەکەت:\n\n{message.text}"
    )

print("A R A N Bot is running...")
bot.infinity_polling()
