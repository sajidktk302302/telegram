import telebot
from telebot import types

BOT_TOKEN = "7343281956:AAHdB96OIavowtvtAxIQYgl1jTRpc7a_zWA"
ADMIN_ID = 7083983430
CHANNEL_LINK = "https://t.me/+gMFUmLD4XV4zOWU0"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    buy_button = types.InlineKeyboardButton("🔘 Buy Course", callback_data="buy_course")
    help_button = types.InlineKeyboardButton("🔘 Help Line", callback_data="help_line")
    markup.add(buy_button, help_button)
    bot.send_message(message.chat.id, "Welcome to the Trading Course Bot!
Choose an option below:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "buy_course":
        bot.send_message(call.message.chat.id, "📌 Send payment to this Binance ID:
`738206848`

📸 After payment, please send a screenshot here.")
    elif call.data == "help_line":
        bot.send_message(call.message.chat.id, "📞 Contact us on Telegram:
@YourSupportUsername")

@bot.message_handler(content_types=["photo"])
def handle_screenshot(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "📤 Your screenshot has been sent to the admin for approval.
Please wait...")

@bot.message_handler(commands=["approve"])
def approve_user(message):
    if message.from_user.id == ADMIN_ID and message.reply_to_message:
        user_id = message.reply_to_message.forward_from.id
        bot.send_message(user_id, f"✅ Payment Approved!

🎥 Access the course here:
{CHANNEL_LINK}")

bot.polling()
