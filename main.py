import telebot
import urllib.request
import xlrd
import datetime


def get_cells():
    url = ''
    urllib.request.urlretrieve(url, 'file.xlsx')
    rb = xlrd.open_workbook('file.xlsx')
    sheet = rb.sheet_by_index(4)
    ans = '<b>{}</b>\n' \
          '{} {}\n' \
          '{} {}\n' \
          '{} {}\n' \
          '<b>{}</b>\n' \
          '{} {}\n' \
          '{} {}\n' \
          '{} {}\n' \
          '<b>{}</b>\n' \
          '{} {}\n'.format(sheet.cell(28, 0).value, sheet.cell(29, 0).value, sheet.cell(29, 1).value,
                           sheet.cell(30, 0).value, sheet.cell(30, 1).value, sheet.cell(31, 0).value,
                           sheet.cell(31, 1).value, sheet.cell(32, 0).value, sheet.cell(33, 0).value,
                           sheet.cell(33, 1).value, sheet.cell(34, 0).value, sheet.cell(34, 1).value,
                           sheet.cell(35, 0).value, sheet.cell(35, 1).value, sheet.cell(36, 0).value,
                           sheet.cell(37, 0).value, sheet.cell(37, 1).value)
    rb.release_resources()
    del rb
    return ans
print(get_cells())


bot = telebot.TeleBot('')
print(bot.get_me())


@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.from_user.id
    f = open('list.txt', 'r')
    puk = f.readlines()
    puk = [x.strip() for x in puk]
    f.close()
    if puk.count(str(message.from_user.id)) == 0:
        f = open('list.txt', 'a')
        f.write('\n' + str(message.from_user.id))
        f.close()

    if message.text == '/start':
        bot.send_message(user_id, 'Бот работает')

uid = 


sended = True
while True:
    now = datetime.datetime.now()
    if int(now.hour) == 22 and sended:
        ans = get_cells()
        bot.send_message(uid, ans, parse_mode='HTML')
        sended = False
    if int(now.hour) == 0:
        sended = True
    try:
        bot.polling(none_stop=True)
    except Exception as err:
        print(err)
