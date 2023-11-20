import sqlite3
import random

db = sqlite3.connect('server1.db')                       #Подключение к баез данных
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS casino(
    login TEXT,
    password TEXT,
    cash INT
    )''')
db.commit()
def reg():
    user_login = input('Log in: ')
    user_password = input('Password: ')

    sql.execute(f'SELECT login FROM casino WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        sql.execute('INSERT INTO casino VALUES(?,?,?)',(user_login,user_password,0))
        db.commit()
        print('Зарегистрировано')
    else:
        print('Такая запись уже есть')
def delete_db():
    sql.execute(f'DELETE FROM casino WHERE login = "{user_login}"')
    db.commit()
    print('Запись удалена')
def casin():
    global user_login
    user_login = input('Login: ')
    number = random.randint(1,2)
    for i in sql.execute(f'SELECT cash FROM casino users WHERE login = "{user_login}"'):
        balance = i[0]
        print(balance)

    #кейс проверки на регистрацию
    sql.execute(f'SELECT login FROM casino WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print('Такого пользователя не существует')
        reg()
    else:
        if number == 1:
            sql.execute(f'UPDATE casino SET cash = {1000+balance} WHERE login = "{user_login}"')            #добавление средств
            print('Поздарвляем, вы выиграли!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            db.commit()
        else:
            print('Вы проиграли')
            delete_db()
def enter():
    for i in sql.execute('SELECT login, cash FROM casino'):
        print(i)
def main():
    casin()
    enter()
main()
