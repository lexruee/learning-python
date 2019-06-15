from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import User


engine = create_engine('sqlite:///./db.sqlite')
Session = sessionmaker(bind=engine)
session = Session()


print("Show all user nicknames:")
users = session.query(User).all()
nicknames = [user.nickname for user in users]
print("\t" + "\n\t".join(nicknames))
print()


print('Filter users by their lastname:')
users = session.query(User).filter_by(lastname='Zimmermann')
nicknames = [user.nickname for user in users]
print("\t" + "\n\t".join(nicknames))
print()
