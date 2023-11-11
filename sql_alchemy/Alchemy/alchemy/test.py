from database.db import session
from database.models import User
def get_del_user(login):
    user = session.query(User).filter(User.login == login).delete(synchronize_session=False)
    session.commit()
    session.close()
    print(user)
    return user


get_del_user("Tsiri")