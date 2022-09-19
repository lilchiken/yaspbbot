import vk_api
import time
import pandas as pd
import os

ntime = time.time()
weektime= ntime-604800
session = vk_api.VkApi(token='...')   # Ваш токен
vk= session.get_api()

def get_posts(group_id):
    posts = session.method('wall.get', {'owner_id':group_id,'count':1})
    i=posts['items']
    l=i[0]
    id_post = l['id']
    date=l['date']
    txt=l['text']
    if date>=weektime:
        print(date,txt)
        path='/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path,'1_'+str(group_id)))

    posts = session.method('wall.get', {'owner_id':group_id,'count':1,'offset':1})
    i=posts['items']
    l=i[0]
    id_post = l['id']
    date=l['date']
    txt=l['text']
    if date>=weektime:
        print(date,txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '2_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id':group_id,'count':1,'offset':2})
    i=posts['items']
    l=i[0]
    id_post = l['id']
    date=l['date']
    txt=l['text']
    if date>=weektime:
        print(date,txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '3_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': 3})
    i = posts['items']
    l = i[0]
    id_post = l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '4_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': 4})
    i = posts['items']
    l = i[0]
    id_post = l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '5_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': 5})
    i = posts['items']
    l = i[0]
    id_post = l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '6_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': 6})
    i = posts['items']
    l = i[0]
    id_post = l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '7_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': 7})
    i = posts['items']
    l = i[0]
    id_post = l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '8_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': 8})
    i = posts['items']
    l = i[0]
    id_post = l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '9_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': 9})
    i = posts['items']
    l = i[0]
    id_post = l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '10_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': 10})
    i = posts['items']
    l = i[0]
    id_post = l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '11_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset':11})
    i = posts['items']
    l = i[0]
    id_post = l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '12_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': 12})
    i = posts['items']
    l = i[0]
    id_post = l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '13_' + str(group_id)))

    posts = session.method('wall.get', {'owner_id': group_id, 'count': 1, 'offset': 13})
    i = posts['items']
    l = i[0]
    id_post=l['id']
    date = l['date']
    txt = l['text']
    if date >= weektime:
        print(date, txt)
        path = '/home/102spb/.tusabot/.undo_posts/'
        df = pd.DataFrame(
            [[id_post, group_id, date, txt]],
            columns=['id_post', 'group_id', 'date', 'txt']
        )
        df.to_csv(os.path.join(path, '14_' + str(group_id)))



print('kruzhok'
      ''
      '')
get_posts(-175177391)
print('')
print('')
print('vnvnc')
print('')
print('')
get_posts(-168260120)
print('')
print('')
print('blank')
print('')
print('')
get_posts(-157199475)
print('')
print('')
print('bar union')
print('')
print('')
get_posts(-64877766)
print('')
print('')
print('griboedov')
print('')
print('')
get_posts(-154594155)
print('')
print('')
print('k-30')
print('')
print('')
get_posts(-197176470)
print('')
print('')
print('hi-hat')
print('')
print('')
get_posts(-96237316)
print('')
print('')
print('Vibe Room')
print('')
print('')
get_posts(-72390981)
print('')
print('')
print('hotline party')
print('')
print('')
get_posts(-161160335)
print('')
print('')
print('block14')
print('')
print('')
get_posts(-212322125)
print('')
print('')
print('StackenShneider')
print('')
print('')
get_posts(-55837663)