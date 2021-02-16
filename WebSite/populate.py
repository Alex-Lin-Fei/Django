import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'WebSite.settings')


import django
django.setup()

from saltfish.models import Category


def populate():
    categories = ['sports', 'luggage', 'booties', ' cosmetics', 'digital',
                  'furniture', 'home appliances', 'medicine']
    for cat in categories:
        add_category(cat)


def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()


if __name__ == '__main__':
    print('Starting saltfish population script...')
    populate()
