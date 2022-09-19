import os
import pandas as pd
import datetime
import shutil


pnlist=[]
pnkeyword=['Понедельник','понедельник','ПН','Понедельнику','понедельнику','ПОНЕДЕЛЬНИК','Понедельника','понедельника','ПОНЕДЕЛЬНИКУ','ПОНЕДЕЛЬНИКА']

vtlist=[]
vtkeyword=['Вторник','вторник','ВТ','Вторнику','вторнику','ВТОРНИК','Вторника','вторника','ВТОРНИКУ','ВТОРНИКА']

srlist=[]
srkeyword=['Среда','среда','СР','Среду','среду','СРЕДА','Среды','среды','СРЕДУ','СРЕДЫ']

chtlist=[]
chtkeyword=['Четверг','четверг','ЧТ','Четвергу','четвергу','ЧЕТВЕРГ','Четверга','четверга','ЧЕТВЕРГУ','ЧЕТВЕРГА']

ptlist=[]
ptkeyword=['Пятница','пятница','ПТ','Пятницу','пятницу','ПЯТНИЦА','Пятницы','пятницы','ПЯТНИЦЫ','ПЯТНИЦУ','Пятничным','пятничным']

sblist=[]
sbkeyword=['Суббота','суббота','СБ','Субботу','субботу','СУББОТА','Субботы','cубботы','СУББОТЫ','СУББОТУ','Субботним','субботним']

vslist=[]
vskeyword=['Воскресенье','воскресенье','ВС','ВОСКРЕСЕНЬЕ','Воскресенья','воскресенья','ВОСКРЕСЕНЬЯ']

kruzhok = -175177391
vnvnc = -168260120
blank = -157199475
bar_union = -64877766
griboedov = -154594155
k_trinol = -197176470
hi_hat = -96237316
vide_room = -72390981
hotline_party = -161160335
block14 = -212322125
StackenShneider =-55837663

clublist = [kruzhok,vnvnc,blank,bar_union,griboedov,k_trinol,hi_hat,vide_room,hotline_party,block14,StackenShneider,
            ]

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


def df_to_txt(object):
    return str(object['txt'])

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

def weekday(object):
    try:
        date = datetime.date(2022, int(date_from_txt(finder(df_to_txt(object)))[0][1]),
                             int(date_from_txt(finder(df_to_txt(object)))[0][0])).weekday()
        if date == 0:
            pnlist.append(object)
        if date == 1:
            vtlist.append(object)
        if date == 2:
            srlist.append(object)
        if date == 3:
            chtlist.append(object)
        if date == 4:
            ptlist.append(object)
        if date == 5:
            sblist.append(object)
        if date == 6:
            vslist.append(object)
        try:
            date = datetime.date(2022, int(str(first_date(day_of_week2(date_to_day_of_week2(finder2(df_to_txt(object)))))[1])),int(str(first_date(day_of_week2(date_to_day_of_week2(finder2(df_to_txt(object)))))[0]))).weekday()
            print(date)
            if date == 0:
                pnlist.append(object)
            if date == 1:
                vtlist.append(object)
            if date == 2:
                srlist.append(object)
            if date == 3:
                chtlist.append(object)
            if date == 4:
                ptlist.append(object)
            if date == 5:
                sblist.append(object)
            if date == 6:
                vslist.append(object)
        except:
            pass
    except:
        pass

def weekday2(object):
    try:
        date = datetime.date(2022, int(date_from_txt(finder(df_to_txt(object)))[0][1]),
                             int(date_from_txt(finder(df_to_txt(object)))[0][0])).weekday()
        if date == 0:
            pnlist.append(object)
        if date == 1:
            vtlist.append(object)
        if date == 2:
            srlist.append(object)
        if date == 3:
            chtlist.append(object)
        if date == 4:
            ptlist.append(object)
        if date == 5:
            sblist.append(object)
        if date == 6:
            vslist.append(object)
    except:
            date = datetime.date(2022, int(str(first_date(day_of_week2(date_to_day_of_week2(finder2(df_to_txt(object)))))[1])),int(str(first_date(day_of_week2(date_to_day_of_week2(finder2(df_to_txt(object)))))[0]))).weekday()
            print(date)
            if date == 0:
                pnlist.append(object)
            if date == 1:
                vtlist.append(object)
            if date == 2:
                srlist.append(object)
            if date == 3:
                chtlist.append(object)
            if date == 4:
                ptlist.append(object)
            if date == 5:
                sblist.append(object)
            if date == 6:
                vslist.append(object)


for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'1_'+str(club))
        df.name = '1_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'2_'+str(club))
        df.name = '2_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'3_'+str(club))
        df.name = '3_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'4_'+str(club))
        df.name = '4_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'5_'+str(club))
        df.name = '5_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'6_'+str(club))
        df.name = '6_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'7_'+str(club))
        df.name = '7_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'8_'+str(club))
        df.name = '8_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'9_'+str(club))
        df.name = '9_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'10_'+str(club))
        df.name = '10_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'11_'+str(club))
        df.name = '11_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'12_'+str(club))
        df.name = '12_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'13_'+str(club))
        df.name = '13_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

for club in clublist:
    try:
        df = pd.read_csv(filepath_or_buffer='/home/102spb/.tusabot/.undo_posts/'+'14_'+str(club))
        df.name = '14_'+str(club)
        txt=str(df['txt'])
        for keyword in pnkeyword:
            if keyword in txt:
                pnlist.append(df)
        for keyword in vtkeyword:
            if keyword in txt:
                vtlist.append(df)
        for keyword in srkeyword:
            if keyword in txt:
                srlist.append(df)
        for keyword in chtkeyword:
            if keyword in txt:
                chtlist.append(df)
        for keyword in ptkeyword:
            if keyword in txt:
                ptlist.append(df)
        for keyword in sbkeyword:
            if keyword in txt:
                sblist.append(df)
        for keyword in vskeyword:
            if keyword in txt:
                vslist.append(df)
        weekday(df)
        weekday2(df)
    except:
        pass

lists = [pnlist, vtlist, srlist, chtlist, ptlist, sblist, vslist]


print(
    len(pnlist),
    len(vtlist),
    len(srlist),
    len(chtlist),
    len(ptlist),
    len(sblist),
    len(vslist)
)

folders = ['/home/102spb/.tusabot/.posts/.pn', '/home/102spb/.tusabot/.posts/.vt',
          '/home/102spb/.tusabot/.posts/.sr', '/home/102spb/.tusabot/.posts/.cht',
          '/home/102spb/.tusabot/.posts/.pt', '/home/102spb/.tusabot/.posts/.sb',
          '/home/102spb/.tusabot/.posts/.vs']
for folder in folders:
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))



for df in pnlist:
    df.to_csv(os.path.join('/home/102spb/.tusabot/.posts/.pn',str(int(df.values[-1][2]))+'_'+str(int(df.values[-1][1]))))

for df in vtlist:
    df.to_csv(os.path.join('/home/102spb/.tusabot/.posts/.vt',str(int(df.values[-1][2]))+'_'+str(int(df.values[-1][1]))))

for df in srlist:
    df.to_csv(os.path.join('/home/102spb/.tusabot/.posts/.sr',str(int(df.values[-1][2]))+'_'+str(int(df.values[-1][1]))))

for df in chtlist:
    df.to_csv(os.path.join('/home/102spb/.tusabot/.posts/.cht',str(int(df.values[-1][2]))+'_'+str(int(df.values[-1][1]))))

for df in ptlist:
    df.to_csv(os.path.join('/home/102spb/.tusabot/.posts/.pt',str(int(df.values[-1][2]))+'_'+str(int(df.values[-1][1]))))

for df in sblist:
    df.to_csv(os.path.join('/home/102spb/.tusabot/.posts/.sb',str(int(df.values[-1][2]))+'_'+str(int(df.values[-1][1]))))

for df in vslist:
    df.to_csv(os.path.join('/home/102spb/.tusabot/.posts/.vs',str(int(df.values[-1][2]))+'_'+str(int(df.values[-1][1]))))

#выдает 16 из 37 т е 50%
#теперь 29 из 37
#по итогу 18 из 37 (без повторов)