import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'rahul.settings')

import django
django.setup()

from faker import Faker
from firstname.models import *
fakegen = Faker()

def populate(n=5):
    for i in range(n):
        name  = fakegen.firstname()
        lstname = fakegen.lastname()
        mail = fakegen.email()
        webpg= jose.objects.get_or_create(firstname=name,lastname=lstname,email=mail)

if __name__ = '__main__':
    populate(20)
