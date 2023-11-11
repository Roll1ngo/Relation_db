from sqlalchemy import create_engine, Table,Column, Integer,ForeignKey, String, MetaData
from sqlalchemy.sql import select
from sqlalchemy.orm import relationship,declarative_base,sessionmaker
from rich import print

engine = create_engine("sqlite:///my_base.sqlite",echo = False)
DBsession = sessionmaker(bind = engine)
session = DBsession()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    articles = relationship('Article')


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer(), primary_key=True)
    title = Column(String(255))
    content = Column(String(255))
    user_id = Column(Integer(), ForeignKey('users.id'))
    author = relationship('User')

Base.metadata.create_all(engine)

if __name__ == '__main__':
    a = session.execute(select(User).join(User.articles)).scalars().all()
    for u in a:
        print(u.articles.title)








