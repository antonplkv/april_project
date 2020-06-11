import mongoengine as me
import datetime

me.connect('webshop_adv_april')


"""
            ТЕХНИКА#root
               |
          БЫТОВАЯ ТЕХНИКА#child (подкатегория)
          /     |       \
    Холодил.  Микроволн.  Чайник #childs
"""


class Category(me.Document):
    title = me.StringField(min_length=1, max_length=512)
    description = me.StringField(min_length=2, max_length=4096)
    subcategories = me.ListField(me.ReferenceField('self'))
    parent = me.ReferenceField('self', default=None)


class Product(me.Document):
    #attrs
    title = me.StringField(min_length=1, max_length=512)
    description = me.StringField(min_length=2, max_length=4096)
    created = me.DateTimeField(default=datetime.datetime.now())
    price = me.DecimalField(required=True)
    discount = me.IntField(min_value=0, max_value=100)
    in_stock = me.BooleanField(default=True)
    image = me.FileField(required=True)
    category = me.ReferenceField(Category)


class Text(me.Document):

    TITLES = {
        'greetings': 'Текст приветствия',
        'cart': 'Текст корзины'
    }
    title = me.StringField(min_length=1, max_length=256, choices=TITLES.values(), unique=True)
    body = me.StringField(min_length=1, max_length=4096)