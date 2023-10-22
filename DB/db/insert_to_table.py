from psycopg2 import Error
from db_connect import connection
import faker
from random import randint


fake = faker.Faker("Ua")

insert_to_table_users = '''
INSERT INTO users(name,email,password,age) VALUES(%s,%s,%s,%s);'''



if __name__=='__main__':
    with connection() as conn:
        c = conn.cursor()
        for _ in range (50):
            c.execute(insert_to_table_users,(fake.name(),fake.email(), fake.password(),randint(18,80)))
            c.close()