import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os

API_TOKEN = "8109739440:AAHHiE8HQmRiS0vhMo5xlCYgTB66IDrzUZA"  # Замените на ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Клавиатура приветствия
greeting_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Мое портфолио"),
            KeyboardButton(text="Гайды и пакеты")
        ],
        [
            KeyboardButton(text="Как со мной поработать"),
            KeyboardButton(text="Канал для SMM специалистов")
        ],
        [
            KeyboardButton(text="Бесплатный продукт"),
            KeyboardButton(text="Мой VPN")
        ]
    ],
    resize_keyboard=True
)

# Клавиатура для портфолио
portfolio_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Назад"), KeyboardButton(text="Telegram портфолио")],
        [KeyboardButton(text="Лазерная эпиляция"), KeyboardButton(text="Студия дизайна интерьера")],
        [KeyboardButton(text="Свадебное агенство"), KeyboardButton(text="Цветочный лофт")],
        [KeyboardButton(text="Производство игровых домов"), KeyboardButton(text="Студия красоты")],
        [KeyboardButton(text="Образование")]
    ],
    resize_keyboard=True
)

# Inline-клавиатура для студий лазерной эпиляции
lazer_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Студия Porvatova", callback_data="lazer_porvatova")],
        [InlineKeyboardButton(text="Клиника Lazeria", callback_data="lazer_lazeria")],
        [InlineKeyboardButton(text="Сеть студий Tanya Lazerr", callback_data="lazer_tanya")],
        [InlineKeyboardButton(text="Студия Nina_Lazerr", callback_data="lazer_nina")]
    ]
)

# Клавиатура для возврата и работы
work_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Как со мной поработать"), KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    video_path = os.path.join("media", "greeting.mp4")
    if os.path.exists(video_path):
        await message.answer_video(
            open(video_path, "rb"),
            caption="ПРИВЕТСТВИЕ НАЧАЛО",
            reply_markup=greeting_kb
        )
    else:
        await message.answer(
            "ПРИВЕТСТВИЕ НАЧАЛО\n(Видео будет добавлено позже)",
            reply_markup=greeting_kb
        )

@dp.message()
async def handle_buttons(message: types.Message):
    if message.text == "Мое портфолио":
        await message.answer(
            "МОЕПОРТФОЛИОТЕКСТ",
            reply_markup=portfolio_kb
        )
    elif message.text == "Лазерная эпиляция":
        photo_path = os.path.join("photo", "lazernepilaciya.jpg")
        if os.path.exists(photo_path):
            with open(photo_path, "rb") as photo:
                await message.answer_photo(
                    photo,
                    caption="ОПИСАНИЕ СТУДИЙ лазе эп",
                    reply_markup=lazer_inline_kb
                )
        else:
            await message.answer(
                "ОПИСАНИЕ СТУДИЙ лазе эп\n(Фото будет добавлено позже)",
                reply_markup=lazer_inline_kb
            )
    elif message.text == "Назад":
        # Возврат к списку ниш портфолио
        await message.answer(
            "МОЕПОРТФОЛИОТЕКСТ",
            reply_markup=portfolio_kb
        )
    elif message.text == "Telegram портфолио":
        await message.answer(
            "Ссылка на Telegram портфолио: https://t.me/your_portfolio_channel"
        )
    elif message.text == "Как со мной поработать":
        work_menu_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Контент-съемка + монтаж")],
                [KeyboardButton(text="Полное SMM-ведение")],
                [KeyboardButton(text="Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer(
            "Выберите формат сотрудничества:",
            reply_markup=work_menu_kb
        )
    elif message.text == "Контент-съемка + монтаж":
        content_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Связаться со мной")],
                [KeyboardButton(text="Отзывы и примеры")],
                [KeyboardButton(text="Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer(
            "КОНТЕНТСЪЕМКА текст",
            reply_markup=content_kb
        )
    elif message.text == "Связаться со мной":
        await message.answer("Мой Telegram: @your_telegram_id")
    elif message.text == "Отзывы и примеры":
        await message.answer("Раздел в разработке")
    elif message.text == "Полное SMM-ведение":
        smm_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Посмотреть примеры ведения")],
                [KeyboardButton(text="Связаться и обсудить")],
                [KeyboardButton(text="Вернуться в меню")]
            ],
            resize_keyboard=True
        )
        await message.answer(
            "СММВЕДЕНИЕ текст",
            reply_markup=smm_kb
        )
    elif message.text == "Посмотреть примеры ведения":
        await message.answer("Раздел в разработке")
    elif message.text == "Связаться и обсудить":
        await message.answer("Мой Telegram: @your_telegram_id")
    elif message.text == "Вернуться в меню":
        await message.answer(
            "Вы вернулись в главное меню.",
            reply_markup=greeting_kb
        )
    elif message.text in [
        "Свадебное агенство",
        "Студия дизайна интерьера",
        "Цветочный лофт",
        "Производство игровых домов",
        "Студия красоты"
    ]:
        video_files = {
            "Свадебное агенство": ("media/svadebnagenstvo.mp4", "СВАД АГЕНСТВО текст"),
            "Студия дизайна интерьера": ("media/dizaininteriera.mp4", "ДИЗАЙН ИНТЕРЬЕРА текст"),
            "Цветочный лофт": ("media/cvetloft.mp4", "ЦВЕТОЧНЫЙ ЛОФТ текст"),
            "Производство игровых домов": ("media/igrdom.mp4", "ПРОИЗВОДСТВО ИГРОВЫХ ДОМОВ текст"),
            "Студия красоты": ("media/beautystudio.mp4", "СТУДИЯ КРАСОТЫ текст")
        }
        video_path, desc = video_files[message.text]
        portfolio_niche_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Как со мной поработать")],
                [KeyboardButton(text="Назад")]
            ],
            resize_keyboard=True
        )
        if os.path.exists(video_path):
            with open(video_path, "rb") as video:
                await message.answer_video(
                    video,
                    caption=desc,
                    reply_markup=portfolio_niche_kb
                )
        else:
            await message.answer(
                f"{desc}\n(Видео будет добавлено позже)",
                reply_markup=portfolio_niche_kb
            )
    elif message.text == "Образование":
        edu_inline_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Образовательное агенство Dreamway to Korea", callback_data="edu_dreamway")],
                [InlineKeyboardButton(text="Образовательная площадка As Education", callback_data="edu_asedu")]
            ]
        )
        await message.answer(
            "ОПИСАНИЕ ОБРАЗОВАНИЯ",
            reply_markup=edu_inline_kb
        )
    elif message.text == "Гайды и пакеты":
        guides_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Консультация для СММ специалиста")],
                [KeyboardButton(text="Big ПАК по анимационному монтажу")],
                [KeyboardButton(text="Блогеры твоего города")],
                [KeyboardButton(text="Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer(
            "ОПИСАНИЕ ГАЙДОВ",
            reply_markup=guides_kb
        )
    elif message.text == "Блогеры твоего города":
        cities_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Москва"), KeyboardButton(text="Тверь")],
                [KeyboardButton(text="Казань"), KeyboardButton(text="Анапа")],
                [KeyboardButton(text="Ульяновск"), KeyboardButton(text="Свой город")],
                [KeyboardButton(text="Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer(
            "Выберите город:",
            reply_markup=cities_kb
        )
    elif message.text in ["Москва", "Тверь", "Казань", "Анапа", "Ульяновск"]:
        buy_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Купить"), KeyboardButton(text="Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer(
            f"Вы выбрали город: {message.text}",
            reply_markup=buy_kb
        )
    elif message.text == "Свой город":
        await message.answer(
            "Пожалуйста, введите название вашего города текстом:",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text="Назад")]],
                resize_keyboard=True
            )
        )
        dp['waiting_for_city'] = message.from_user.id
    elif dp.get('waiting_for_city') == message.from_user.id:
        city = message.text
        await message.answer("Спасибо! Ваш запрос отправлен.", reply_markup=greeting_kb)
        username = message.from_user.username
        user_info = f"@{username}" if username else f"id: {message.from_user.id}"
        await bot.send_message(
            815005535,
            f"НАСТЯ!!! Нужны блогеры человеку ({user_info}) по городу {city}"
        )
        dp['waiting_for_city'] = None
    elif message.text == "Бесплатный продукт":
        free_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Контент на 30 дней")],
                [KeyboardButton(text="Пак с таблицами для SMM")],
                [KeyboardButton(text="Чек лист instagram профиля")],
                [KeyboardButton(text="7 ошибок в сторис")],
                [KeyboardButton(text="Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer(
            "БЕСПЛАТНПРОДУКТ текст",
            reply_markup=free_kb
        )
    elif message.text == "Назад":
        await message.answer(
            "Вы вернулись в главное меню.",
            reply_markup=greeting_kb
        )
    elif message.text == "Мой VPN":
        vpn_inline_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Попробовать бесплатно", callback_data="vpn_try_free")]
            ]
        )
        vpn_kb = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Назад")]],
            resize_keyboard=True
        )
        await message.answer(
            "ОПИСАНИЕВПН текст",
            reply_markup=vpn_inline_kb
        )
    elif message.text == "Вернуться в меню":
        await message.answer(
            "Вы вернулись в главное меню.",
            reply_markup=greeting_kb
        )
    else:
        await message.answer(f"Неизвестная команда: {message.text}")

@dp.callback_query()
async def handle_lazer_studio_callback(callback: types.CallbackQuery):
    studio_videos = {
        "lazer_porvatova": ("media/porvatova_reels.mp4", "ОПИСАНИЕ СТУДИИ Porvatova"),
        "lazer_lazeria": ("media/lazeria_reels.mp4", "ОПИСАНИЕ СТУДИИ Lazeria"),
        "lazer_tanya": ("media/tanya_reels.mp4", "ОПИСАНИЕ СТУДИИ Tanya Lazerr"),
        "lazer_nina": ("media/nina_reels.mp4", "ОПИСАНИЕ СТУДИИ Nina_Lazerr"),
        "edu_dreamway": ("media/dreamway_reels.mp4", "ОПИСАНИЕ Dreamway to Korea"),
        "edu_asedu": ("media/asedu_reels.mp4", "ОПИСАНИЕ As Education")
    }
    data = callback.data
    if data in studio_videos:
        video_path, desc = studio_videos[data]
        if os.path.exists(video_path):
            with open(video_path, "rb") as video:
                await callback.message.answer_video(
                    video,
                    caption=desc,
                    reply_markup=work_kb
                )
        else:
            await callback.message.answer(
                f"{desc}\n(Видео будет добавлено позже)",
                reply_markup=work_kb
            )
    if callback.data == "vpn_try_free":
        vpn_try_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Инструкция по установке", callback_data="vpn_instruction")],
                [InlineKeyboardButton(text="Задать вопрос", callback_data="vpn_question")]
            ]
        )
        menu_kb = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Вернуться в меню")]],
            resize_keyboard=True
        )
        await callback.message.answer(
            "Выберите действие:",
            reply_markup=vpn_try_kb
        )
        await callback.message.answer(
            "Для возврата используйте кнопку ниже.",
            reply_markup=menu_kb
        )
        await callback.answer()
        return
    if callback.data == "vpn_instruction":
        await callback.message.answer("Инструкция по установке: ...")
        await callback.answer()
        return
    if callback.data == "vpn_question":
        await callback.message.answer("Задайте свой вопрос в Telegram: @your_telegram_id")
        await callback.answer()
        return
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
