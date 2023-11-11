from sqlalchemy import create_engine, Table,Column, Integer,ForeignKey, String, MetaData
from sqlalchemy.sql import select
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker
from sqlalchemy.orm import relationship,declarative_base
from rich import print
import asyncio
import aiosqlite


engine = create_async_engine("sqlite:///my_base.sqlite",echo = False)
AsyncDBsession = async_sessionmaker(bind = engine,expire_on_commit=False, class_=AsyncSession)


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

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def main():
        await init_models
        async with AsyncDBsession() as session:
            new_user = User(name = "VlaD azaza")
            session.add(new_user)
            new_address = Article(title = "Hello")
            session.add(new_address)
            await session.commit()
        
            u = await session.execute(select(User))
            r_u = u.scalars().all()
            for u in r_u:
                 print(u.id, u.name)

        


if __name__ == '__main__':
          
    asyncio.run(main())
    










