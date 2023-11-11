from database.db import engine
from sqlalchemy import Column, Integer,ForeignKey, String,DateTime,func,event
from sqlalchemy.orm import relationship,declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(25),unique=True)
    password = Column(String(25))


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String(250),nullable=False)
    description = Column(String(250), nullable = False)
    created_at  = Column(DateTime,default=func.now())
    updated_at = Column(DateTime,default=func.now())
    user_id = Column(Integer,ForeignKey('users.id'))
    user = relationship(User)

@event.listens_for(Todo,'before_update')
def update_updated_at(mapper,conn,target):
    target.updated_at = func.now()

Base.metadata.create_all(engine)
    
