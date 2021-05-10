


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'rahul.settings')

import django
django.setup()

from faker import Faker
from firstname.models import *
fakegen = Faker()

def populate(n=5):
    for i in range(n):
        nam = fakegen.name().split()
        fstname = nam[0]
        lstname = nam[1]
        mail = fakegen.email()
        webpg= jose.objects.get_or_create(firstname=fstname,lastname=lstname,email=mail)[0]

if __name__ == '__main__':
    populate(20)
