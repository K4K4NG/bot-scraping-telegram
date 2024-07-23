import os
import random
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
import re
import json
import uuid

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6727871339:AAHQ1KPhE5CaUfwSmYWoqB0Lz5xoeSXvNFo'

ugen = []
for x in range(1000):
    rr = random.randint
    uacrack1 = f"Mozilla/5.0 (Linux; Android {str(rr(7, 12))}; RMX2101 Build/RKQ1.{str(rr(111111, 211111))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73, 150))}.0.{str(rr(5500, 5900))}.{str(rr(75, 99))} Mobile Safari/537.36"
    uacrack2 = f"Mozilla/5.0 (Linux; Android 11; Infinix X6512 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75, 150))}.0.{str(rr(5000, 5500))}.{str(rr(75, 99))} Mobile Safari/537.36"
    uacrack3 = f"Mozilla/5.0 (Linux; Android {str(rr(9, 13))}; LG-H918 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.{str(rr(3200, 3500))}.84 Mobile Safari/537.36"
    uacrack4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(9, 16))}_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1"
    uacrack5 = f"Mozilla/5.0 (Linux; Android {str(rr(7, 12))}; Redmi Note 9 Pro Max) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73, 99))}.0.{str(rr(4500, 5900))}.{str(rr(75, 150))} Mobile Safari/537.36"
    uacrack6 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7, 12))}; en-US; LEGEND MAX Build/RP1A.{str(rr(111111, 210000))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73, 99))}.0.{str(rr(3500, 4000))}.{str(rr(75, 150))} UCBrowser/{str(rr(10, 20))}.4.0.{str(rr(1300, 1500))} Mobile Safari/537.36"
    uacrack7 = f"Mozilla/5.0 (Linux; Android 12; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75, 99))}.0.{str(rr(4500, 4900))}.{str(rr(75, 99))} Mobile Safari/537.36"
    uanyancek = random.choice([uacrack1, uacrack2, uacrack3, uacrack4, uacrack5, uacrack6, uacrack7])
    ugen.append(uanyancek)

def CreatePage(name: str, category: list, token: str):
    r = requests.Session()
    vir = {
        "params": {
            "client_input_params": {
                "cp_upsell_declined": 0,
                "category_ids": category,
                "profile_plus_id": "0",
                "page_id": "0"
            },
            "server_params": {
                "name": name,
                "INTERNAL__latency_qpl_instance_id": random.randrange(36700000, 36800000),
                "creation_source": "android",
                "screen": "category",
                "referrer": "pages_tab_launch_point",
                "INTERNAL__latency_qpl_marker_id": float(f'{random.random() + 3:.13f}E13'),
                "variant": 5
            }
        }
    }
    var = {
        "params": {
            "params": json.dumps(vir),
            "bloks_versioning_id": 'c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec',
            "app_id": "com.bloks.www.additional.profile.plus.creation.action.category.submit"
        },
        "scale": "1",
        "nt_context": {
            "styles_id": 'e6c6f61b7a86cdf3fa2eaaffa982fbd1',
            "using_white_navbar": True,
            "pixel_ratio": 1,
            "is_push_on": True,
            "bloks_version": 'c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec'
        }
    }
    data = {
        'access_token': token,
        'method': 'post',
        'pretty': False,
        'format': 'json',
        'server_timestamps': True,
        'locale': 'id_ID',
        'purpose': 'fetch',
        'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.additional.profile.plus.creation.action.category.submit',
        'fb_api_caller_class': 'graphservice',
        'client_doc_id': '11994080423068421059028841356',
        'variables': json.dumps(var),
        'fb_api_analytics_tags': ["GraphServices"],
        'client_trace_id': str(uuid.uuid4())
    }
    pos = r.post('https://graph.facebook.com/graphql', data=data).text.replace('\\', '')
    if ('profile_plus_id' in str(pos)) and ('page_id' in str(pos)):
        name, page_id, profile_id = re.findall(r'"android", "pages_tab_launch_point", "(.*?)", "(.*?)", "(.*?)", "intent_selection"', str(pos))[0]
        return f"Success Create Page!\nPage Name  : {name}\nPage ID    : {page_id}\nProfile ID : {profile_id}"
    else:
        return 'Failed Create Page!'

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("1. Scrape Instagram Photo", callback_data='1'),
            InlineKeyboardButton("2. Scrape Instagram Username", callback_data='2'),
        ],
        [
            InlineKeyboardButton("3. Download YouTube Video", callback_data='3'),
            InlineKeyboardButton("4. Download Instagram Post", callback_data='4'),
        ],
        [
            InlineKeyboardButton("5. Download Instagram Highlights", callback_data='5'),
            InlineKeyboardButton("6. Update Tools", callback_data='6'),
        ],
        [
            InlineKeyboardButton("7. Create Facebook Page", callback_data='7'),
            InlineKeyboardButton("8. Send Message Grup", callback_data='8'),
        ],
        [
            InlineKeyboardButton("9. Send Message User", callback_data='9'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    selection = query.data

    if selection == '1':
        context.user_data['current_option'] = '1'
        query.edit_message_text(text="Masukan link foto:")
    elif selection == '2':
        context.user_data['current_option'] = '2'
        query.edit_message_text(text="Masukkan nama pengguna (username) Instagram:")
    elif selection == '3':
        context.user_data['current_option'] = '3'
        query.edit_message_text(text="Masukkan URL YouTube:")
    elif selection == '4':
        context.user_data['current_option'] = '4'
        query.edit_message_text(text="Masukkan link post Instagram:")
    elif selection == '5':
        context.user_data['current_option'] = '5'
        query.edit_message_text(text="Masukkan id highlights Instagram:")
    elif selection == '6':
        query.edit_message_text(text="Maaf Update Belum Tersedia Oleh owner nya")
    elif selection == '7':
        context.user_data['current_option'] = '7'
        query.edit_message_text(text="Masukkan nama halaman Facebook yang ingin dibuat:")
    elif selection == '8':
        context.user_data['current_option'] = '8'
        query.edit_message_text(text="Masukkan link grup Telegram dan pesan yang ingin dikirim (dipisahkan dengan koma):")
    elif selection == '9':
        context.user_data['current_option'] = '9'
        query.edit_message_text(text="Masukkan link pengguna Telegram dan pesan yang ingin dikirim (dipisahkan dengan koma):")
        

def handle_input(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    current_option = context.user_data.get('current_option')

    if current_option == '1':
        url = user_input
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        image_url = soup.find('meta', property='og:image')['content']
        caption = soup.find('meta', property='og:description')['content']
        update.message.reply_photo(photo=image_url, caption=f"Caption: {caption}")
    elif current_option == '2':
        username = user_input
        url = f"https://www.instagram.com/{username}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        followers_tag = soup.find('meta', attrs={'property': 'og:description', 'content': True})
        if followers_tag:
            followers_content = followers_tag['content']
            followers_count = followers_content.split(',')[0].split()[0]
            following_count = followers_content.split(',')[1].split()[0]
            post_count = followers_content.split(',')[2].split()[0]
            profile_photo_tag = soup.find('meta', property='og:image')
            bio_tag = soup.find('meta', attrs={'content': True, 'name': 'description'})
            if profile_photo_tag:
                profile_photo_url = profile_photo_tag['content']
                bio = bio_tag['content']
                update.message.reply_photo(photo=profile_photo_url)
                update.message.reply_text(f"Link image profile : {profile_photo_url} ")
                update.message.reply_text(f"Nama Pengguna: {username}\nJumlah Pengikut: {followers_count}\nJumlah yang Diikuti: {following_count}\nJumlah Postingan: {post_count}\nBio Lengkap : {bio}")
            else:
                update.message.reply_text("Foto profil tidak ditemukan.")
        else:
            update.message.reply_text("Data tidak ditemukan.")            
    elif current_option == '3':
        video_url = user_input
        yt = YouTube(video_url)
        update.message.reply_text("Mendownload...")
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        update.message.reply_audio(audio=open(new_file, 'rb'))
    elif current_option == '4':
        url = user_input
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        media_url = soup.find('meta', property='og:video') or soup.find('meta', property='og:image')
        if media_url:
            media_url = media_url['content']
            if "video" in media_url:
                update.message.reply_video(video=media_url)
            else:
                update.message.reply_photo(photo=media_url)
        else:
            update.message.reply_text("Media tidak ditemukan.")
    elif current_option == '8':
        send_message_to_group(update, context)
    elif current_option == '9':
        send_message_to_user(update, context)
    elif current_option == '7':
        page_name = user_input
        token = 'EAATKgyZCPz44BAGRzsxXSzXIdRYkaegdyRvsbIe3fROx3Sz6BDbHDfwXhS4pe4rX2WdKu0GPadoonWAuvoADYXNZBIbiZBo3QH5JVHU4YzMMxMT1IooPIjjZAO2Q8YMt8Ff2x4zhkBwHP7sXdF03QY75axpJXmS3v02lZC9o0BmSOSZB2k2rSb9HnM7WJwRlkZD'  # Replace with actual Facebook access token
        category = ['2214']  # Replace with actual category IDs
        result = CreatePage(page_name, category, token)
        update.message.reply_text(result)

def extract_chat_id_from_link(link: str) -> str:
    """
    Ekstrak chat ID atau username dari link grup atau pengguna Telegram.
    """
    match = re.search(r't.me/(\w+)', link)
    if match:
        username = match.group(1)
        return f"@{username}"
    match = re.search(r't.me/joinchat/(\w+)', link)
    if match:
        chat_id = match.group(1)
        return f"-{chat_id}"
    return None

def send_message_to_group(update: Update, context: CallbackContext) -> None:
    """
    Kirim pesan ke grup Telegram menggunakan link grup.
    """
    try:
        message_parts = update.message.text.split(',', 1)
        if len(message_parts) != 2:
            update.message.reply_text('Format pesan tidak benar. Gunakan format: link_grup, pesan.')
            return
        
        group_link = message_parts[0].strip()
        message = message_parts[1].strip()

        group_id = extract_chat_id_from_link(group_link)
        if not group_id:
            update.message.reply_text('Link grup tidak valid.')
            return

        context.bot.send_message(chat_id=group_id, text=message)
        update.message.reply_text('Pesan berhasil dikirim ke grup.')
    except Exception as e:
        if 'Forbidden' in str(e):
            update.message.reply_text('Bot tidak memiliki izin untuk mengirim pesan ke grup ini.')
        else:
            update.message.reply_text(f'Terjadi kesalahan: {e}')

def send_message_to_user(update: Update, context: CallbackContext) -> None:
    """
    Kirim pesan ke pengguna Telegram menggunakan link pengguna.
    """
    try:
        message_parts = update.message.text.split(',', 1)
        if len(message_parts) != 2:
            update.message.reply_text('Format pesan tidak benar. Gunakan format: link_pengguna, pesan.')
            return
        
        user_link = message_parts[0].strip()
        message = message_parts[1].strip()

        user_id = extract_chat_id_from_link(user_link)
        if not user_id:
            update.message.reply_text('Link pengguna tidak valid.')
            return

        context.bot.send_message(chat_id=user_id, text=message)
        update.message.reply_text('Pesan berhasil dikirim ke pengguna.')
    except Exception as e:
        if 'Forbidden' in str(e):
            update.message.reply_text('Bot tidak memiliki izin untuk mengirim pesan ke pengguna ini.')
        else:
            update.message.reply_text(f'Terjadi kesalahan: {e}')

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_input))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
