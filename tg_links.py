# Исходный список ссылок
urls = [
  "https://t.me/druzyabd",
  "https://t.me/chat_devushkim",
  "https://t.me/virtiklove",
  "https://t.me/vpiska_chatik",
  "https://t.me/chat_ngrskp",
  "https://t.me/robuygg_chat",
  "https://t.me/obshchenie_virt",
  "https://t.me/chat_vinchkkk",
  "https://t.me/znakomstva_kiev_chatc",
  "https://t.me/chat_moskva_znakomstva",
  "https://t.me/ekbchat_66",
  "https://t.me/moscowchatwalk",
  "https://t.me/sexintim",
  "https://t.me/nayti1l",
  "https://t.me/spbchat_78",
  "https://t.me/turkey_public",
  "https://t.me/ekaterinburg_chat_ekb",
  "https://t.me/chat_tvoitai",
  "https://t.me/chatik_ufa",
  "https://t.me/chat_baby99",
  "https://t.me/obshchenia_chat9",
  "https://t.me/krasnodar_vpisky_chat",
  "https://t.me/starpetsgg_chat",
  "https://t.me/obshenie_ch_at",
  "https://t.me/abhazia_chat",
  "https://t.me/intimobs",
  "https://t.me/biznes_obsu",
  "https://t.me/lovee_chatik",
  "https://t.me/weinmiami",
  "https://t.me/druzyao05",
  "https://t.me/flexlive",
  "https://t.me/room_RO",
  "https://t.me/Life_chat_spb",
  "https://t.me/+XBeq0b_HER9iNTdi",
  "https://t.me/adssamui",
  "https://t.me/samara_v63",
  "https://t.me/indi_krasnoyarsk",
  "https://t.me/virtoznakomstva",
  "https://t.me/pleyadi_chat",
  "https://t.me/chechentsy_obshcheniye_95",
  "https://t.me/china_help_ru",
  "https://t.me/msk_znak_24",
  "https://t.me/bubsobshenie",
  "https://t.me/zartschool_public",
  "https://t.me/antalya_love",
  "https://t.me/deathlilkesin",
  "https://t.me/darkptz",
  "https://t.me/vapeperm59flood",
  "https://t.me/vzaimnaya_podpiska_vv"
]

# Функция для извлечения названия чата из URL
def extract_chat_name(url):
    # Убираем префиксы и лишние части
    if "t.me/" in url:
        chat_name = url.split("t.me/")[1]
    elif "tg-cat.com/" in url:
        chat_name = url.split("/")[-1]
    else:
        chat_name = url.split("/")[-1]  # На всякий случай для других случаев
    return chat_name

# Создание списка 'chats' с названиями чатов
chats = [extract_chat_name(url) for url in urls]

# Печать результата в нужном формате
'''print("chats = [")
for chat in chats:
    print(f"  '{chat}',")
print("]")'''


print(chats)