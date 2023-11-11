import argparse
from database.crud import create_todo,get_all_todos,get_user,update_todo,remove_todo


parser = argparse.ArgumentParser(description = 'Todo APP')
parser.add_argument('--action', '-help = "Command: create, update,list,remove')
parser.add_argument('--id')
parser.add_argument('--title')
parser.add_argument('--desc')
parser.add_argument('--login')

arguments = parser.parse_args()
print(f'arguments:{arguments}')
my_arg = vars(arguments)
print(f'my_arg:{my_arg}')
action = my_arg.get('action')
print(f'action: {action}')
title = my_arg.get('title')
print(f"title: {title}")
description = my_arg.get('desc')
print(f"desc: {description}")
_id = my_arg.get("id")
print(f"_id: {id}")
login = my_arg.get('login')
print(f"login:{login}")


def main(user):
    match action:
        case 'create':
            create_todo(title=title, description=description,user = user)
        case 'list':
            todos = get_all_todos(user)
            for t in todos:
                print(t.id,t.title,t.description,t.user.login)
        case 'update':
            t = update_todo(_id==_id, title=title, description=description, user=user)
            if t:
                print(t.id, t.title, t.description, t.user.login)
            else:
                print("Not Found")
        
        case 'remove':
            r = remove_todo(_id==_id,user==user)
            print(f"remove_todo:{r}")

        case _:
            print('Nothing')


if __name__== '__main__':
    user = get_user(login)
    password = input('Password:')
    # print('woo I am autorised')if password == user.password else print('Wrong password')
    if password == user.password:
        main(user)
    else:
        print('Wrong password')