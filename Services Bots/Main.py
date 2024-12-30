import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your bot token
API_TOKEN = '7895494742:AAGTqnrrCV76eNaR7K_YmBhg4-dMXUSRYFc'

# Replace with your group and channel IDs
GROUP_ID = -1002273874326  # Replace with your group ID
CHANNEL_ID = -1002428641212  # Replace with your channel ID

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create inline keyboard
    keyboard = InlineKeyboardMarkup(row_width=2)
    group_button = InlineKeyboardButton(
        text="Join Group", url="https://t.me/AzzuraStudioChat")
    channel_button = InlineKeyboardButton(
        text="Join Channel", url="https://t.me/azzurastudio")
    verify_button = InlineKeyboardButton(
        text="✅ Check Verification ✅", callback_data="check_verification")

    keyboard.add(group_button, channel_button)
    keyboard.add(verify_button)

    bot.send_message(
        message.chat.id,
        "Please join the group and channel to use this bot:",
        reply_markup=keyboard
    )

# Callback query handler for button clicks
@bot.callback_query_handler(func=lambda call: call.data == "check_verification")
def check_membership(call):
    user_id = call.from_user.id

    # Check membership in the group
    try:
        group_member = bot.get_chat_member(GROUP_ID, user_id)
        is_in_group = group_member.status in ["member", "administrator", "creator"]
    except:
        is_in_group = False

    # Check membership in the channel
    try:
        channel_member = bot.get_chat_member(CHANNEL_ID, user_id)
        is_in_channel = channel_member.status in ["member", "administrator", "creator"]
    except:
        is_in_channel = False

    if is_in_group and is_in_channel:
        bot.answer_callback_query(
            call.id, "You are verified! Thank you for joining.")
    else:
        bot.answer_callback_query(
            call.id, "You must join both the group and channel to use this bot.", show_alert=True)

# Polling for new messages
bot.polling()
