import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "8591024080:AAE-dYuDFylilhYcQ5qSc0tY7S78rlnXdzM"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("link"))
async def send_link(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀 Перейти по ссылке",
                    url="https://t.me/wgkskinsbot?start=ref_6591245969"
                )
            ]
        ]
    )

    await message.answer(
        "👇 Вот ваша ссылка\n\n"
        "1. Нажмите кнопку ниже\n"
        "2. Перейдите по ссылке\n"
        "3. Готово ✅",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())