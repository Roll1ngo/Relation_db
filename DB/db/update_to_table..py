from db_connect import connection
import faker
from random import randint


fake = faker.Faker("uk-UA")

update_to_table_users = '''
UPDATE users SET phone_number= %s 
WHERE id = %s
;'''



if __name__=='__main__':
    with connection() as conn:
        c = conn.cursor()
        for _id in range (1,60):
            c.execute(update_to_table_users,(fake.phone_number(),_id))
        c.close()