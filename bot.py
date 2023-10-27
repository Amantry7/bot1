from aiogram import Bot, Dispatcher,types, executor
import random

TOKEN_API = "6492785279:AAG6XcUcFe3wvtY1HSeDlOe3r4pyk-7V3oE"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
count = 0
async def on_startup(_):
    print("Бот подключон ")

helpcomm = """
<b>/start</b> - <em>запускает бота </em>
<b>/help</b> - <em>показывает список команд </em>
<b>/cat</b> - <em>показывает кота </em>
<b>/description</b> - <em>о боте </em>
<b>/count</b> - <em>счетчик</em>"""
@dp.message_handler(text=["как ты", "Как ты"])
async def send_welcome(message:types.Message): 
    await message.answer("Да не плохо ")
    
@dp.message_handler(content_types=['sticker'])
async def send_stic_id(message:types.Message):
    await message.answer(message.sticker.file_id)
    
# @dp.message_handler()
# async def echo(message:types.Message):
#     await message.answer(message.text)

@dp.message_handler(commands=['help'])
async def send_help(message:types.Message):
    await message.reply(text= helpcomm, parse_mode='HTML') 
@dp.message_handler(commands=['start']) 
async def send_welcome(message:types.Message): 
    await message.answer("Привет я бот для учебы" )
    await message.delete()
@dp.message_handler(commands=['description'])
async def send_descr(message:types.Message):
    await message.reply("""
я телеграм бот для учобы 
мой создатель это Аман 
он создал меня попреколу
(он мне даже имя не дал:( """)
@dp.message_handler(commands=['count'])
async def send_count(message:types.Message):
    global count 
    await message.answer(F"число: {count}")
    count += 1
# @dp.message_handler()
# async def echo(massage:types.Message):
#     if massage.text.count >= 1:
#        await massage.answer(text=massage.text)

@dp.message_handler(commands=['cat'])
async def sent_cat(message:types.Message):
    await message.answer("смотри какой котик ❤️") 
    await bot.send_sticker(message.from_user.id, sticker ='CAACAgIAAxkBAAEKnJFlOnbM4ozl8bbHmF1zVGer3KZDFQACfwcAAhhC7ghjZeQdLEIAAaAwBA')    
    
@dp.message_handler(text=["❤️"])
async def heart(message:types.Message):
    await message.reply("🤍")  
       
@dp.message_handler()
async def send_emoji(message:types.Message):
    await message.reply(message.text + " что за хуйня")



if __name__ == '__main__': 
    executor.start_polling(dp, on_startup=on_startup)
    