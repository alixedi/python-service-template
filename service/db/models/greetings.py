from sqlalchemy import Column, Integer, String
from yourapplication.database import Base

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    hello = Column(String(100))
    name = Column(String(100))

    def __init__(self, hello=None, name=None):
        self.hello = hello or 'Hello'
        self.name = name or 'World'

    @property
    def greeting(self):
        return f'{self.hello} {self.name}!'

    def __unicode__(self):
        return f'{self.hello} {self.name}!'
