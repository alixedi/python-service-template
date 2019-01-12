from sqlalchemy import Column, Integer, String

from service.db.models import Base


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    hello = Column(String(100))
    name = Column(String(100))

    def __init__(self, hello=None, name=None):
        """ By all means override the constructor if
        only to set defaults. This is a contrived
        example.
        """
        self.hello = hello or 'Hello'
        self.name = name or 'World'

    @property
    def greeting(self):
        """ This is an example of defining a property
        instead of a column when the result can be 
        easily and cheaply computed and doesn't need
        to be stored.
        """
        return f'{self.hello} {self.name}!'

    @staticmethod
    def get_users_with_name(session, name):
        """ This is an example of how to define a query
        using staticmethod to use the model class as a
        "namespace" only.
        """
        return session.query(User).filter(User.name==name)

    @staticmethod
    def get_user(session, user_id):
        """ Get the user with the given user_id.
        """
        return session.query(User).get(user_id)

    def __str__(self):        
        return self.greeting