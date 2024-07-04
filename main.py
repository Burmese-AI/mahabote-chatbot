import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from configparser import ConfigParser
import re
import mahabote

config = ConfigParser()
config.read('config.ini')
request_token = config['MAHABOTE']['TOKEN']

welcome_message = "\
မင်္ဂလာပါ\n\
MahaBote မှကြိုဆိုပါတယ်။\n\n\
သင်ရဲ့ မဟာဘုတ်ဇာတာအား သိရှိနိုင်ရန် မွေးသက္ကရာဇ်(ခရစ်နှစ်) ပေးပို့ပေးပါ။\n\n\
ပေးပိုရာတွင် အင်္ဂလိပ်အက္ခရာဖြင့် ရက်-လ-ခုနှစ် အစဉ်လိုက် (ဥပမာ 29-1-2000) ရေးသားပေးပါရန် တောင်းဆိုအပ်ပါတယ်။"

error_message = "ကျေးဇူးပြု၍ ထပ်မံပေးပို့ပေးပါ။"

result_message = "{}သား/သမီး {}ဖွားဖြစ်ပါတယ်"

date_pattern = r'^\d{1,2}-\d{1,2}-\d{4}$'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)


async def takeAction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_dob = update.message.text
    if re.match(date_pattern, input_dob): # check whether input is in defined format or not
        day, house = mahabote.getHouse(input_dob)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=result_message.format(day, house))
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=error_message)


if __name__ == '__main__':
    application = ApplicationBuilder().token(request_token).build()
    
    start_handler = CommandHandler('start', start)
    action_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), takeAction)

    application.add_handler(start_handler)
    application.add_handler(action_handler)

    application.run_polling()