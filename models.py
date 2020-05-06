from datetime import datetime
from peewee import *

DATABASE = SqliteDatabase('journal_entry.db')

class Post(Model):
    post_id = IntegerField(primary_key=True)
    date = DateTimeField(default=datetime.now)
    title = CharField(max_length=100)
    time_spent = IntegerField()
    things_learned = TextField()
    resources = TextField()
    
    class Meta:
        database = DATABASE
        order_by = ('-date',)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Post], safe=True)
    