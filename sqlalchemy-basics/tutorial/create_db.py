from model import Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///./db.sqlite', echo=True)
Base.metadata.create_all(engine)
