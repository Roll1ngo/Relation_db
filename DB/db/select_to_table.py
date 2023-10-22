from db_connect import connection
import faker
from random import randint
import pprint as print




fake = faker.Faker("uk-UA")

simple_select = '''
SELECT * FROM  users  WHERE id = %s;'''

select = '''
SELECT id,name,email,age
FROM users
WHERE age > 50
ORDER BY name
LIMIT 10
;'''

select_regex = """
SELECT id, name, email, age
FROM  users
WHERE name SIMILAR TO '%(Адам|нко)%'
ORDER BY name
LIMIT 3
;"""



if __name__=='__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(select_regex)
        print(c.fetchall())
        c.close()