from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

TOKEN_API = "6492785279:AAG6XcUcFe3wvtY1HSeDlOe3r4pyk-7V3oE"
 
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
async def on_start(_):
    print("бот подключон")
    
help_command = """
<b>/start</b> - <em>начала нашей работы </em>
<b>/help</b> - <em>список команд</em>
<b>/котик</b> - <em>котик </em>
<b>/location</b> - <em>локация</em>

"""    

kb = ReplyKeyboardMarkup()
kb.add(KeyboardButton('help'))
@dp.message_handler(commands=['start'])
async def send_start(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,text="добро пожалывать в группу", reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['котик'])
async def send_image(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo='https://icdn.lenta.ru/images/2020/09/30/13/20200930130228617/detail_9ad62f72eb0b24b9b8f76677d3a1c605.jpg')     
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_point(message:types.Message): 
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=34,
                            longitude=76)

@dp.message_handler(commands=['help'])
async def help_comm(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                        text=help_command, parse_mode='HTML'   )
    await message.delete()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
