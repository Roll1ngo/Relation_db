from psycopg2 import connect, DatabaseError,Error
from contextlib import contextmanager

@contextmanager
def connection():
    conn = None
    try:
        conn= connect(host = 'localhost', user = 'postgres',database = 'postgres', password = 'for_db')
        yield conn
        conn.commit()

    except Error as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()











    