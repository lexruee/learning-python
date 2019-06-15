from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import User


engine = create_engine('sqlite:///./db.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

users = [
    User(firstname='Mike', lastname='Müller', nickname='mike'),
    User(firstname='Peter', lastname='Müller', nickname='pete'),
    User(firstname='Hans', lastname='Peter', nickname='hanspeter'),
    User(firstname='Hans', lastname='Zimmer', nickname='hanz'),
    User(firstname='Fritz', lastname='Zimmermann', nickname='fritz'),
    User(firstname='Mark', lastname='Zimmermann', nickname='mark'),
]

session.add_all(users)
session.commit()
