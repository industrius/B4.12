import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from find_athlete import find

DB_PATH = "sqlite:///sochi_athletes.sqlite3"


base = declarative_base()

class User(base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)

    def __str__(self):
        return "id:{:<8} Рост:{:<8} Дата рождения:{}".format(self.id, self.height, self.birthdate)

def connect_db():
    """
    Устанавливает соединение к базе данных и возвращает объект сессии 
    """
    engine = sa.create_engine(DB_PATH)
    base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def request_data():
    """
    Запрашивает у пользователя данные
    """


    print("Запрос данных")
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    gender = ""
    while gender not in ("м","ж","М","Ж"):
        gender = input("Пол:(м/ж): ")
    if gender.lower() == "м": gender = "Male"
    if gender.lower() == "ж": gender = "Female"
    email = ""
    while not valid_email(email):
        email = input("e-mail: ")
    birthdate = input("Дата рождения: ")
    height = input("Рост: ")

    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user

def valid_email(email):
    """
    Проверяет валидность email. Возвращает True, если email допустимый, и False — в противном случае.
    """
    if email.count("@") == 1:
        if email.find(".", email.find("@"), len(email) - 2) != -1:
            return True
    return False

# Отладка
def user_auto(session, quantity):
    """
    Добавляет quantity-количество "случайных" записей в таблицу User
    """
    import datetime
    import random
    first_name = "dfsddsfg"
    last_name = "sdfwer"
    email = "dsf@sfdg.ru"
    
    for _ in range(quantity):
        gender = random.choice(["Male", "Female"])
        year = str(random.randint(1980, 2000))
        month = str(random.randint(1, 12))
        if len(month) < 2: month = "0" + month
        day = str(random.randint(1, 29))
        if len(day) < 2: day = "0" + day
        birthdate = "{}-{}-{}".format(year, month, day)
        height = random.randint(150, 199) / 100

        user = User(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            email=email,
            birthdate=birthdate,
            height=height
        )
        session.add(user)
    session.commit()

def show(session):
    """
    Вывод списков
    """
    for item in session.query(User).all():
        print(item)

def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()

    # просим пользователя выбрать режим
    mode = input(
        "Выбери режим.\n1 - найти пользователя по ID\n2 - ввести данные нового пользователя\n")
    # проверяем режим
    if mode == "1":
        # выбран режим поиска
        user_id = input("Введи ID пользователя для поиска: ")
        if user_id.isdigit():
            find(session, int(user_id))
        else:
            print("Некорректный ID")
    elif mode == "2":
        user_data = request_data()
        # добавляем нового пользователя в список user
        session.add(user_data)
        session.commit()
        print("Данные сохранены")
    else:
        print("Некорректный режим")

    #Отладка
    #user_auto(session, 15) #Функция генерирует и записывает 15 случайных записей в таблицу User(все от лени)
    #show(session) #Функция показывает все записи из таблицы User
    #find(session, 19) #поиск user с ID

if __name__ == "__main__":
    main()