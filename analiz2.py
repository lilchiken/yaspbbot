import datetime
import pandas as pd
import os

day_today = str(datetime.datetime.now())[8:11]
month_today = str(datetime.datetime.now())[5:7]
today_like_xx_dot_xx = day_today+month_today

folders = ['/home/102spb/.tusabot/.posts/.pn', '/home/102spb/.tusabot/.posts/.vt',
          '/home/102spb/.tusabot/.posts/.sr', '/home/102spb/.tusabot/.posts/.cht',
          '/home/102spb/.tusabot/.posts/.pt', '/home/102spb/.tusabot/.posts/.sb',
          '/home/102spb/.tusabot/.posts/.vs']

zerodate = ['0','1','2','3','4','5','6','7','8','9']
firstdate = ['0','1','2','3','4','5','6','7','8','9']
minusonedate = ['0','1','2','3','4','5','6','7','8','9']
minustwodate = ['0','1']

months =[]
jan = ['Январь', 'январь', 'Января', 'января','ЯНВАРЯ','ЯНВАРЬ']
feb = ['Феварль', 'Февраля','феварль', 'февраля','ФЕВРАЛЬ','ФЕВРАЛЯ']
mar = ['Март', 'Марта', 'март', 'марта','МАРТ','МАРТА']
apr = ['Апрель', 'апрель', 'Апреля', 'апреля','АПРЕЛЬ','АПРЕЛЯ']
may = ['Май','май','Мая','мая','МАЙ','МАЯ']
jun = ['Июнь','июнь','Июня','июня','ИЮНЬ','ИЮНЯ']
jul = ['Июль', 'июль', 'Июля', 'июля','ИЮЛЬ','ИЮЛЯ']
aug = ['Август', 'августа', 'Августа', 'август','АВГУСТ','АВГУСТА']
sep = ['Сентябрь', 'сентябрь', 'Сентября', 'сентября','СЕНТЯБРЬ','СЕНТЯБРЯ']
october = ['Октябрь','октябрь','Октября','октября','ОКТЯБРЬ','ОКТЯБРЯ']
nov = ['Ноябрь', 'ноябрь', 'Ноября', 'ноября','НОЯБРЬ','НОЯБРЯ']
dec = ['Декабрь', 'Декабря', 'декабрь', 'декабря','ДЕКАБРЬ','ДЕКАБРЯ']
months.append(jan)
months.append(feb)
months.append(mar)
months.append(apr)
months.append(may)
months.append(jun)
months.append(jul)
months.append(aug)
months.append(sep)
months.append(october)
months.append(nov)
months.append(dec)

def finder2(object): #отдает лист число + месяц(буквами) - 1
    date = []
    wordlist =[]
    name_months=[]
    k=0
    for word in object.split():
        wordlist.append(word)
    for k in range(12):
        for name in months[k]:
            name_months.append(name)
        k+=1
    for word in wordlist:
        try:
            if word[0] in zerodate or word[1] in firstdate:
                date.append(word)
        except:
            pass
        if word in name_months:
            date.append(word)
    return date

def date_to_day_of_week2(object): #заменяет месяц буквами на цифру и отдает стр по типу 1.01 -2
    name_months=[]
    for k in range(12):
        for name in months[k]:
            name_months.append(name)
        k+=1
    try:
        for o in object:
            for name in name_months:
                if o == name:
                    if name in jan:
                        return object[1] + '.01'
                    if name in feb:
                        return object[1] + '.02'
                    if name in mar:
                        return object[1] + '.03'
                    if name in apr:
                        return object[1] + '.04'
                    if name in may:
                        return object[1] + '.05'
                    if name in jun:
                        return object[1] + '.06'
                    if name in jul:
                        return object[1] + '.07'
                    if name in aug:
                        return object[1] + '.08'
                    if name in sep:
                        return object[1] + '.09'
                    if name in october:
                        return object[1] + '.10'
                    if name in nov:
                        return object[1] + '.11'
                    if name in dec:
                        return object[1] + '.12'
    except:
        pass

def day_of_week2(object): #разделяет 1.01 на лист 1 и 01 -3
    return object.split('.')

def finder(object): #находит что-то похожее на даты из текста по типу 1.01 -1.1
    wordlist = []
    date = []
    for word in object.split():
        wordlist.append(word)
    for word in wordlist:
        try:
            if word[0] in zerodate or word[1] in firstdate or word[-1] in minusonedate or word[-2] in minustwodate:
                date.append(word)
        except:
            pass
    return date

def date_from_txt(object): #находит дату из функции выше -1.2
    ddate =[]
    dddate=[]
    for date in object:
        try:
            d = date.split('.')
            ddate.append(d)
        except:
            pass
    for date in ddate:
        if len(date) == 2 and date[1]!='':
            dddate.append(date)
        else:
            pass
    return(dddate)

def first_date(object): #добавляет ноль ко дню, чтобы было не 1.01, а 01.01 -4
    date=[]
    ddate=[]
    if len(object[0]) == 1:
        object[0]='0'+object[0]
        date.append(object[0])
        date.append(object[1])
        ddate.append(date)
        return ddate
    else:
        return object


for folder in os.listdir('/home/102spb/.tusabot/.posts/'):
    for file in os.listdir('/home/102spb/.tusabot/.posts/' + str(folder) + '/'):
        path='/home/102spb/.tusabot/.posts/' + str(folder) + '/'+str(file)
        df = pd.read_csv(filepath_or_buffer=path)
        txt = df.values[0][-1]
        try:
            str(date_from_txt(finder(txt))[0][0])+'.'+str(date_from_txt(finder(txt))[0][1])
            if int(str(date_from_txt(finder(txt))[0][0])) < int(day_today) or int(str(date_from_txt(finder(txt))[0][1])) < int(month_today):
                os.remove(path)
            try:
                print(str(first_date(day_of_week2(date_to_day_of_week2(finder2(txt))))[0])+'.'+str(first_date(day_of_week2(date_to_day_of_week2(finder2(txt))))[1]))
                if int(str(first_date(day_of_week2(date_to_day_of_week2(finder2(txt))))[0])) < int(day_today) or int(str(first_date(day_of_week2(date_to_day_of_week2(finder2(txt))))[1])) < int(month_today):
                    os.remove(path)
            except:
                pass
        except:
            pass
print('true')