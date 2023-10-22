from db_connect import connection
import faker



fake = faker.Faker("uk-UA")

update_to_table_users = '''
UPDATE users SET phone_number= %s 
WHERE id = %s
;'''



if __name__=='__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(update_to_table_users,(fake.phone_number(),(60,)))
        c.close()