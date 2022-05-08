from pyrogram import Client
from my_script.telegram_project.sergei.forward_message.my_accaunt.yakvenalexx import *
from get_logins import *
import random
import csv
import time

my_app = {1: 'yakvenalexx',
           2: 'sergei_anatolievich_yakovenko',
           3: 'ups_smirnova'}


accaunt = 'my_accaunt/' + my_app[1] + '_account'

def write_csv(data):
    with open('result_add_members.csv', 'a', newline='', encoding="utf-8") as f:
        order = ['good_resul', 'bad_resul']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

app = Client(accaunt, api_id, api_hash)
with app:
    bad = 'none'
    good = 'none'
    me = app.get_me()
    print(me.username)
    for i in logins[64:1000]:
        try:
            app.add_chat_members('ups_official_group', i)
            print(f'Пользователь с логином "{i}" добавлен в группу "ups_official_group"')
            good = i
            time.sleep(random.randint(101, 300))
        except Exception as ex:
            print(ex)
            print(f'Я не смог добавить пользователя с логином "{i}":(')
            bad = i
            time.sleep(random.randint(60, 120))
            pass
        finally:
            data = {'good_resul': good, 'bad_resul': bad}
            write_csv(data)