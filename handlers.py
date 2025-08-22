from telegram import(
    Update, ParseMode, ReplyKeyboardMarkup, KeyboardButton
)
from pprint import pprint
from datetime import datetime
import requests
from telegram.ext import CallbackContext
from config import API_KEY
BASE_URL = 'http://api.weatherapi.com/v1'


def start(update: Update, context: CallbackContext):
    user = update.effective_user

    update.message.reply_text(
        f'Assalomu aleykum {user.first_name}',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton('⛅️ Ob-havoni kurish uchun lokatsiya yuboring', request_location = True)]
            ],
            resize_keyboard=True
        )
    )

def send_weather_by_location(update: Update, context: CallbackContext):
    
    if update.message.location:
        lat = update.message.location.latitude
        lon = update.message.location.longitude

        
        url = f"{BASE_URL}/current.json?key={API_KEY}&q={lat},{lon}&aqi=no"
        response = requests.get(url)
        data = response.json()

        
        if "current" in data:
            temp = data['current']['temp_c']
            condition = data['current']['condition']['text']
            feels_like = data['current']['feelslike_c']
            humidity = data['current']['humidity']

            text = (
                f"📍 Sizning joylashuvingiz bo‘yicha ob-havo:\n"
                f"🌡 Harorat: {temp}°C\n"
                f"🤔 His qilinadi: {feels_like}°C\n"
                f"☁ Holat: {condition}\n"
                f"💧 Namlik: {humidity}%"
            )
        else:
            text = "Ob-havo ma'lumotini olishda xatolik yuz berdi."
        
        update.message.reply_text(text)
    else:
        update.message.reply_text("Iltimos, avval location yuboring.")