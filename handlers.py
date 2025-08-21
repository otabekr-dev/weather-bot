from telegram import(
    Update, ParseMode, ReplyKeyboardMarkup, KeyboardButton
)
from telegram.ext import CallbackContext



def start(update: Update, context: CallbackContext):
    user = update.effective_user

    update.message.reply_text(
        '''Assalomu alaykum
Ob-havo haqida ma'lumot beruvchi botga hush keldingiz

Sizga qanday murojaat qilishim mumkin.
Ismingiz...?''',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton('⛅️ Hozirgi ob-havo')],
                [KeyboardButton('🕓 Soatlik ob-havo'), KeyboardButton('🗓 Haftalik ob-havo')],
                [KeyboardButton("📍 Hududni o'zgartirish")],
                [KeyboardButton('📞 Aloqa')]
            ],
            resize_keyboard=True
        )
    )
