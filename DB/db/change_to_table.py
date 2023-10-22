from random import randint

import faker

from db_connect import connection

fake = faker.Faker("uk-UA")

change_table_users = '''
ALTER TABLE users
ADD COLUMN phone_number varchar(25) 
;'''



if __name__=='__main__':
    with connection() as conn:
        c = conn.cursor() 
        c.execute(change_table_users)
        c.close()