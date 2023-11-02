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
 
 
@dp.message_handler(content_types=['sticker'])
async def send_stic_id(message:types.Message):
    await message.answer(message.sticker.file_id)
 
# @dp.message_handler(['oregen'])
# async def send_ori(message:types.Message): 
#     await bot.send_sticker(message.from_user.id, sticker=)
# executor.start_polling(dp, skip_updates=True, on_startup=on_start)

executor.start_polling(dp,on_startup=on_start )
