from sqlalchemy import create_engine, Table,Column, Integer,ForeignKey, String, MetaData
from sqlalchemy.sql import select
from sqlalchemy.orm import relationship,declarative_base,sessionmaker

engine = create_engine("sqlite:///my_base.sqlite",echo=True)
DBsession = sessionmaker(bind = engine)
session = DBsession()

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship(Person)

# Base.metadata.create_all(engine)
Base.metadata.bind = engine
session.add(Person(name = "Bill"))
session.commit()
add_street = Address(street_name = "Geroiv Kharkova",street_number = 308, post_code = 123456)
session.add(add_street)
session.commit()

for person in session.query(Person).all():
    print(f'Person: id : {person.id}, name:{person.name}')
    




