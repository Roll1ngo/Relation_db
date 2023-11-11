from sqlalchemy import create_engine, Table,Column, Integer,ForeignKey, String, MetaData
from sqlalchemy.sql import select

engine = create_engine('sqlite:///:memory:', echo=True)
metadata = MetaData()

users = Table("users",metadata,
              Column("id", Integer, primary_key= True),
              Column("fullname",String)
              )

test_users= Table("test_users",metadata,
              Column("id", Integer, primary_key= True),
              Column("fullname",String)
              )

addresses = Table("addresses",metadata,
              Column("id", Integer, primary_key= True),
              Column("email",String, nullable=False),
              Column("user_id", Integer, ForeignKey("test_users.id"))
              )

metadata.create_all(engine)

if __name__== "__main__":
    names = ["Nik Orelsky","Oleksiy Zagorulko","Mykola Gryshyn"]
    with engine.connect() as conn:
        for name in names:
            r_user = test_users.insert().values(fullname = name )
            add_row = conn.execute(r_user)
        sell = conn.execute(select(test_users))
        print(sell.fetchall())
#         result = conn.execute(r_user)

        
        
       

    #    r_address = addresses.insert().values(email = 'mfdhfjdf@.ua',user_id = result_user.lastrowid)

    #    a_u = select(users.c.fullname, addresses.c.email).select_from(users)
    #    call = conn.execute(a_u)
    #    print(call.fetchall())
