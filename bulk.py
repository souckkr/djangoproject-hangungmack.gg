import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-project-data.settings")
django.setup()

from game.models import Game


f = open('steamstore_game.csv', 'r', encoding='utf-8')
info = []
rdr = csv.reader(f)
print(rdr)

for row in rdr:
    name, developers, genres = row
    tuple = (name, developers, genres)
    info.append(tuple)
f.close()

instances = []
for (name, developers, genres) in info:
    instances.append(Game(title=name, developers=developers, genres=genres))
Game.objects.bulk_create(instances)