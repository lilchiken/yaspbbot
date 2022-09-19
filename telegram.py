import logging
from aiogram import Bot, Dispatcher, executor, types, md
from aiogram.dispatcher.filters import Text
import re
import pandas as pd
import os
import time

# Объект бота
proxy_url = 'http://proxy.server:3128'
bot = Bot(token="...", parse_mode="HTML", proxy=proxy_url) # Ваш токен
# Диспетчер для бота
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# файловая часть
kruzhok = (-175177391 , 'kruzhok')
vnvnc = (-168260120 , 'vnvnc')
blank = (-157199475 , 'blank')
bar_union = (-64877766 , 'bar_union')
griboedov = (-154594155 , 'griboedov')
k_trinol = (-197176470 , 'k_30')
hi_hat = (-96237316 , 'hi_hat')
vide_room = (-72390981 , 'vide_room')
hotline_party = (-161160335 , 'hotline_party')
block14 = (-212322125 , 'block14')
StackenShneider = (-55837663 , 'StackenShneider')

clublist = [kruzhok,vnvnc,blank,bar_union,griboedov,k_trinol,hi_hat,vide_room,hotline_party,block14,StackenShneider,
            ]

def open_file(path):
    return pd.read_csv(filepath_or_buffer=path)
def name_file(path):
    return os.path.basename(path)
def url_post(path):
    return 'https://vk.com/wall'+str(name_file(path))
def name_club(path):
    d = name_file(path).split('_')[0]
    for club in clublist:
        if int(d) == club[0]:
            return club[1]
def small_txt(path):
    df = open_file(path)
    txt = df.values[0][-1]
    try:
        txt = txt.replace('\n',' ')
        txt = re.sub("[\\[].*?[\\]]", "", txt)
        return str(txt[0:50] + '...')
    except:
        return str(txt)

#часть телеграма
new_users=[]
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Кто ты?")
    keyboard.add(button_1)
    new_users.append('')
    await message.answer("Привет", reply_markup=keyboard)

@dp.message_handler(Text(equals='Кто ты?'))
async def whoami(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Готов")
    keyboard.add(button_1)
    await message.answer('<b>Я это я.</b>'+'\n'+
                         'Я агрегатор твоей ночной жизни в Санкт-Петербурге.'+'\n'+
                         'Я это проект, построенный на энтузиазме двух людей.'+'\n'+
                         'И я постоянно развиваюсь.'+'\n'+ '<i>Обратная связь в подробнее.</i>'+'\n'
                         '<b>А ты готов к новым приключениям?</b>', reply_markup=keyboard)

@dp.message_handler(Text(equals='Готов'))
async def b0(message: types.Message):
    keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True).row('ПН','ВТ','СР','ЧТ','ПТ','СБ','ВС')
    await message.answer("Выбирай день недели", reply_markup=keyboard)

listforpn=[]
@dp.message_handler(Text(equals='ПН'))
async def b1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Вернуться назад")
    keyboard.add(button_1)
    listforpn.append('')
    for file in os.listdir('/home/102spb/.tusabot/.posts/' + str('.pn') + '/'):
        nm_cl = str(name_club('/home/102spb/.tusabot/.posts/' + str('.pn') + '/' + str(file))),
        url = str(url_post('/home/102spb/.tusabot/.posts/' + str('.pn') + '/' + str(file))),
        text = small_txt('/home/102spb/.tusabot/.posts/' + str('.pn') + '/' + str(file))
        nm_cl = str(nm_cl[0])
        url = str(url[0])
        await message.answer(md.hlink(str(nm_cl),str(url))+' '+str(text),reply_markup=keyboard)
    if len(os.listdir('/home/102spb/.tusabot/.posts/' + str('.pn') + '/')) == 0:
        await message.answer('Я понимаю, что надо опохмелиться, но не в этот раз', reply_markup=keyboard)

listforvt=[]
@dp.message_handler(Text(equals='ВТ'))
async def b2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Вернуться назад")
    keyboard.add(button_1)
    listforvt.append('')
    for file in os.listdir('/home/102spb/.tusabot/.posts/' + str('.vt') + '/'):
        nm_cl = str(name_club('/home/102spb/.tusabot/.posts/' + str('.vt') + '/' + str(file))),
        url = str(url_post('/home/102spb/.tusabot/.posts/' + str('.vt') + '/' + str(file))),
        text = small_txt('/home/102spb/.tusabot/.posts/' + str('.vt') + '/' + str(file))
        nm_cl = str(nm_cl[0])
        url = str(url[0])
        await message.answer(md.hlink(str(nm_cl),str(url))+' '+str(text),reply_markup=keyboard)
    if len(os.listdir('/home/102spb/.tusabot/.posts/' + str('.vt') + '/')) == 0:
        await message.answer('Слушай, тебе с такими запросами только на думскую...', reply_markup=keyboard)

listforsr=[]
@dp.message_handler(Text(equals='СР'))
async def b3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Вернуться назад")
    keyboard.add(button_1)
    listforsr.append('')
    for file in os.listdir('/home/102spb/.tusabot/.posts/' + str('.sr') + '/'):
        nm_cl = str(name_club('/home/102spb/.tusabot/.posts/' + str('.sr') + '/' + str(file))),
        url = str(url_post('/home/102spb/.tusabot/.posts/' + str('.sr') + '/' + str(file))),
        text = small_txt('/home/102spb/.tusabot/.posts/' + str('.sr') + '/' + str(file))
        nm_cl = str(nm_cl[0])
        url = str(url[0])
        await message.answer(md.hlink(str(nm_cl),str(url))+' '+str(text),reply_markup=keyboard)
    if len(os.listdir('/home/102spb/.tusabot/.posts/' + str('.sr') + '/')) == 0:
        await message.answer('Кто бухает посреди рабочей недели?', reply_markup=keyboard)

listforcht=[]
@dp.message_handler(Text(equals='ЧТ'))
async def b4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Вернуться назад")
    keyboard.add(button_1)
    listforcht.append('')
    for file in os.listdir('/home/102spb/.tusabot/.posts/' + str('.cht') + '/'):
        nm_cl = str(name_club('/home/102spb/.tusabot/.posts/' + str('.cht') + '/' + str(file))),
        url = str(url_post('/home/102spb/.tusabot/.posts/' + str('.cht') + '/' + str(file))),
        text = small_txt('/home/102spb/.tusabot/.posts/' + str('.cht') + '/' + str(file))
        nm_cl = str(nm_cl[0])
        url = str(url[0])
        await message.answer(md.hlink(str(nm_cl),str(url))+' '+str(text),reply_markup=keyboard)
    if len(os.listdir('/home/102spb/.tusabot/.posts/' + str('.cht') + '/')) == 0:
        await message.answer('Четверг, конечно, день хороший, но не в этот раз', reply_markup=keyboard)

listforpt=[]
@dp.message_handler(Text(equals='ПТ'))
async def b5(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Вернуться назад")
    keyboard.add(button_1)
    listforpt.append('')
    for file in os.listdir('/home/102spb/.tusabot/.posts/' + str('.pt') + '/'):
        nm_cl = str(name_club('/home/102spb/.tusabot/.posts/' + str('.pt') + '/' + str(file))),
        url = str(url_post('/home/102spb/.tusabot/.posts/' + str('.pt') + '/' + str(file))),
        text = small_txt('/home/102spb/.tusabot/.posts/' + str('.pt') + '/' + str(file))
        nm_cl = str(nm_cl[0])
        url = str(url[0])
        await message.answer(md.hlink(str(nm_cl),str(url))+' '+str(text),reply_markup=keyboard)
    if len(os.listdir('/home/102spb/.tusabot/.posts/' + str('.pt') + '/')) == 0:
        await message.answer('А ты хоть раз бывал в Ионотеке?', reply_markup=keyboard)

listforsb=[]
@dp.message_handler(Text(equals='СБ'))
async def b6(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Вернуться назад")
    keyboard.add(button_1)
    listforsb.append('')
    for file in os.listdir('/home/102spb/.tusabot/.posts/' + str('.sb') + '/'):
        nm_cl = str(name_club('/home/102spb/.tusabot/.posts/' + str('.sb') + '/' + str(file))),
        url = str(url_post('/home/102spb/.tusabot/.posts/' + str('.sb') + '/' + str(file))),
        text = small_txt('/home/102spb/.tusabot/.posts/' + str('.sb') + '/' + str(file))
        nm_cl = str(nm_cl[0])
        url = str(url[0])
        await message.answer(md.hlink(str(nm_cl),str(url))+' '+str(text),reply_markup=keyboard)
    if len(os.listdir('/home/102spb/.tusabot/.posts/' + str('.sb') + '/')) == 0:
        await message.answer('Что? Всегда можно пойти на думскую :)', reply_markup=keyboard)

listforvs=[]
@dp.message_handler(Text(equals='ВС'))
async def b7(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Вернуться назад")
    keyboard.add(button_1)
    listforvs.append('')
    for file in os.listdir('/home/102spb/.tusabot/.posts/' + str('.vs') + '/'):
        nm_cl = str(name_club('/home/102spb/.tusabot/.posts/' + str('.vs') + '/' + str(file))),
        url = str(url_post('/home/102spb/.tusabot/.posts/' + str('.vs') + '/' + str(file))),
        text = small_txt('/home/102spb/.tusabot/.posts/' + str('.vs') + '/' + str(file))
        nm_cl = str(nm_cl[0])
        url = str(url[0])
        await message.answer(md.hlink(str(nm_cl),str(url))+' '+str(text),reply_markup=keyboard)
    if len(os.listdir('/home/102spb/.tusabot/.posts/' + str('.vs') + '/')) == 0:
        await message.answer('Извини, я был бы сам удивлен, если бы в воскресенье тусовок не было', reply_markup=keyboard)

listforback=[]
@dp.message_handler(Text(equals='Вернуться назад'))
async def b0(message: types.Message):
    keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True).row('ПН','ВТ','СР','ЧТ','ПТ','СБ','ВС')
    listforback.append('')
    await message.answer("Выбирай день недели", reply_markup=keyboard)

@dp.message_handler(Text(equals='Арина'))
async def arina(message: types.Message):
    keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
    but_1 = types.KeyboardButton(text='Вернуться назад')
    keyboard.add(but_1)
    await message.answer('Арина самая милая девочка на земле', reply_markup=keyboard)

@dp.message_handler(Text(equals='арина'))
async def arina(message: types.Message):
    keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
    but_1 = types.KeyboardButton(text='Вернуться назад')
    keyboard.add(but_1)
    await message.answer('Арина самая милая девочка на земле', reply_markup=keyboard)

@dp.message_handler(Text(equals='stats'))
async def stats(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but_1 = types.KeyboardButton(text='Вернуться назад')
    keyboard.add(but_1)
    await message.answer('stats_today:'+'\n'+str(len(listforback))+' кол-во нажатий вернуться назад'
                         +'\n'+str(len(listforpn))+' по пн'
                         +'\n'+str(len(listforvt))+' по вт'
                         +'\n'+str(len(listforsr))+' по ср'
                         +'\n'+str(len(listforcht))+' по чт'
                         +'\n'+str(len(listforpt))+' по пт'
                         +'\n'+str(len(listforsb))+' по сб'
                         +'\n'+str(len(listforvs))+' по вс'
                         +'\n'+str(len(new_users))+' число новых пользователей', reply_markup=keyboard)

@dp.message_handler(Text(equals='qoqushki3'))
async def save_stats(message: types.Message):
    df = pd.DataFrame([[
        'stats_today:' + '\n' + str(len(listforback)) + ' кол-во нажатий вернуться назад'
        + '\n' + str(len(listforpn)) + ' по пн'
        + '\n' + str(len(listforvt)) + ' по вт'
        + '\n' + str(len(listforsr)) + ' по ср'
        + '\n' + str(len(listforcht)) + ' по чт'
        + '\n' + str(len(listforpt)) + ' по пт'
        + '\n' + str(len(listforsb)) + ' по сб'
        + '\n' + str(len(listforvs)) + ' по вс'
        + '\n' + str(len(new_users)) + ' число новых пользователей']],
        columns=['txt'])
    df.to_csv(os.path.join('/home/102spb/.tusabot/.stats', str(time.asctime())))
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but_1 = types.KeyboardButton(text='Вернуться назад')
    keyboard.add(but_1)
    await message.answer('Сейв был сделан', reply_markup=keyboard)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)