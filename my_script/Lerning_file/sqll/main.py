import csv
from peewee import *

db = PostgresqlDatabase(database='parsa', user='postgres', password='admin', host='localhost')

class Coin(Model):
    name = CharField()
    link = TextField()
    price = CharField()
    status = CharField()
    sku = CharField()

    class Meta:
        database = db

def main():
    db.connect()
    db.create_tables([Coin])

    with open('tetyana.csv') as f:
        order = ['name', 'sku', 'price', 'link', 'status']
        reader = csv.DictReader(f, fieldnames=order)

        coins = list(reader)

        # for row in coins:
        #     coin = Coin(name=row['name'],
        #                 link=row['link'],
        #                 price=row['price'],
        #                 status=row['status'],
        #                 sku=row['sku'])
        #     coin.save()

        with db.atomic():
            # for row in coins:
            #     Coin.create(**row)
            for i in range(0, len(coins), 100):
                Coin.insert_many(coins[i:i+100]).execute()

main()