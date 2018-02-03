import time

from . import ModelMixin
from . import db


class Wl(db.Model, ModelMixin):
    __tablename__ = 'mt4_whitelabel_info'
    id = db.Column(db.Integer, primary_key=True)
    mt4_id = db.Column(db.Integer)
    url = db.Column(db.String())
    company = db.Column(db.String())
    company_address = db.Column(db.String())
    tag = db.Column(db.String())
    # 这是一个外键
    # user_id = db.Column(db.Integer, db.ForeignKey('stb_users.id'))
    # # relationship
    # reviews = db.relationship('Review', backref='chest')

    def __init__(self, form):
        print('chest init', form)
        self.task = form.get('task', '')
        self.created_time = int(time.time())

    def update(self, form):
        self.task = form.get('task', '')
        self.save()
