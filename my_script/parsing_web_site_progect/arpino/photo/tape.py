import os

my_dict = {
    'Дуб альпийский': 'barselona_dub_alpiyskiy_50266',
    'Дуб коньяк': 'barselona_dub_cognac_5821',
    'Дуб горный': 'barselona_dub_gornyy_12093',
    'Дуб натуральный': 'barselona_dub_naturalnyy_5860',
    'Дуб шатто': 'barselona_dub_shatto_50226',
    'Дуб старинный': 'barselona_dub_starinnyy_52241',
    'Капучино': 'barselona_kapuchino_13708',
    'Латте': 'barselona_latte_12229',
    'Табако': 'barselona_tabako_8910',
    'col. blanc МДФ': 'barselona_belaya_emal_matovaya_mdf_13744',
    'col. blanc ЯС': 'barselona_blanc_5736',
    'Сапеле': 'barselona_sapele_8868'
}


li = os.listdir()[:-1]
new_li = []

for i in li:
    new_li.append(i[:-4])
print(new_li)

block = new_li
