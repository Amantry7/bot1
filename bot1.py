from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN_API = "6492785279:AAG6XcUcFe3wvtY1HSeDlOe3r4pyk-7V3oE"
 
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
async def on_start(_):
    print("бот подключон")

ikb = InlineKeyboardMarkup(row_width=1)
ib = InlineKeyboardButton(text='GitHub',
                          url='https://github.com/Amantry7')
ib2 = InlineKeyboardButton(text='notio',
                           url='https://geeksbackend.notion.site/geeksbackend/Geeks-Backend-2b37c7cbcfe240198c1d522b045a69c3')
ikb.add(ib,ib2)


help_command = """
<b>/start</b> - <em>начала нашей работы </em>
<b>/help</b> - <em>список команд</em>
<b>/котик</b> - <em>котик </em>
<b>/location</b> - <em>локация</em>

"""    

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='hello world',
                           reply_markup=ikb)

executor.start_polling(dp,on_startup=on_start )
