import telebot
from pytube import YouTube
import os
bot=telebot.TeleBot('5591356432:AAEMi2Wre6FNMi84PfFXJ07gKf4px1Q5QUs')
@bot.message_handler(commands=['start'])
def msc0(self):
    choice = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    choice.add('🎥 Видео', '🎼 Музыка')
    download = bot.send_message(self.chat.id, "Выберите что вы хотите загрузить:", reply_markup=choice)
    bot.register_next_step_handler(download, choicz)
def choicz(self):
    if self.text=='🎼 Музыка':
        link = bot.send_message(self.chat.id, "Введите ссылку на YouTube видео:")
        bot.register_next_step_handler(link, msc)
    if self.text=='🎥 Видео':
        link = bot.send_message(self.chat.id, "Введите ссылку на YouTube видео:")
        bot.register_next_step_handler(link, vid)
def vid(self):
    try:
        video(self, self.text)
    except:
        bot.send_message(self.chat.id, "Вы написали неправильную ссылку. Нажмите /start чтобы начать все сначало.")
def msc(self):
    try:
        music(self, self.text)
    except:
        bot.send_message(self.chat.id, "Вы написали неправильную ссылку. Нажмите /start чтобы начать все сначало.")
def music(self, link):
    bot.send_message(self.chat.id, "Файл в процессе загрузки...")
    yt=YouTube(f'{link}')
    audio=yt.streams.filter(only_audio=True).get_by_itag(251)
    destination = "."
    out_file = audio.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    bot.send_message(self.chat.id, f'''Файл {yt.title} был успешно загружен. Ожидайте ваш файл.
Желаете загрузить еще один файл? Напишите команду /start.''')
    vid = open(new_file, 'rb')
    try:
        bot.send_audio(self.chat.id, vid, timeout=999)
    except:
        bot.send_message(self.chat.id, "Произошла критическая ошибка при отправке вашего файла. Попробуйте еще раз.")
    vid.close()
    os.remove(new_file)
    print(audio)
def video(self, link):
    bot.send_message(self.chat.id, "Файл в процессе загрузки...")
    yt=YouTube(f'{link}')
    video = yt.streams.filter(file_extension='mp4').get_by_itag(22)
    destination = "."
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
    bot.send_message(self.chat.id, f"Файл {yt.title}" + " был успешно загружен. Ожидайте ваш файл."
    "Желаете загрузить еще один файл? Напишите команду /start.")
    vid=open(new_file, 'rb')
    try:
        bot.send_video(self.chat.id, vid, timeout=999)
    except:
        bot.send_message(self.chat.id, "Произошла критическая ошибка при отправке вашего файла. Попробуйте еще раз.")
    vid.close()
    os.remove(new_file)
@bot.message_handler(commands=['help'])
def help(self):
    bot.send_message(self.chat.id, '''Запустите команду /start, чтобы начать диалог.
Выберите что вы хотите загрузить - Видео или Аудио файл.
Если вы выбрали не то что вам надо, просто перезапустите диалог командой /start.
Пожалуйста, не используйте бота в группе - там он может нестабильно работать.''')
@bot.message_handler(commands=['about'])
def about(self):
    bot.send_message(self.chat.id, '''YouTube Downloader 
(bubbleBOT v2.0)
Created by @bubblechuk
Powered by pytelegrambotapi
12.08.22''')
bot.polling(none_stop=True)
