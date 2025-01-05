const TelegramBot = require('node-telegram-bot-api');

// Replace YOUR_BOT_TOKEN with your actual bot token
const token = '7676894188:AAGLz6HzdGEHyXzn1G9Ip7-4C2ik4sGAh_k';
const bot = new TelegramBot(token, { polling: true });

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, 'Hi!');
});
