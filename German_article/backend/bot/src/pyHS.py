from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5405689276:AAHS6MvfByrHAxHs6wR3CKWyQYaHoiUWo-E')
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)



executor.start_polling(dp, skip_updates=True)