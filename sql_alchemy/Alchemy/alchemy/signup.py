from sqlalchemy.exc import SQLAlchemyError
from database.db import session
from database.models import User


if __name__=='__main__':
    loggin = input('login:>>>')
    password = input('password:>>>')
    try:
        user = User(login = loggin, password = password)
        session.add(user)
        session.commit()
    except SQLAlchemyError as err:
        session.rollback()
        print(err)
    finally:
        session.close()