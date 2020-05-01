import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import datetime

 
Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)

    def __str__(self):
        return "id:{:<8} Рост:{:<8} Дата рождения:{}".format(self.id, self.height, self.birthdate)

class Athlete(Base):
    """
    Описывает структуру таблицы athelete
    """
    __tablename__="athelete"
    id = sa.Column(sa.Integer, primary_key=True)
    age = sa.Column(sa.Integer)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.Integer)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals = sa.Column(sa.Integer)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)

    def __str__(self):
       return "id:{:<8} Рост:{:<8} Дата рождения:{:<8} Имя:{}".format(self.id, self.height, self.birthdate, self.name)

def find(session, id):
    """
    Ищет среди списка пользователей users пользователя с заданным id
    Ближайших атлетов по росту и дате рождения
    """
    user_ = session.query(User).filter(User.id == id).first()
    if user_ is not None: 
        diff_min = 3.0 #начальное значение разницы в росте атлета и user 
        diff_date_min = 3650 #начальное значение в днях разницы между датами рождения
        date = user_.birthdate.split("-") #разбираем строку из БД с датой дождения вида 1992-09-28
        user_birthdate = datetime.datetime(int(date[0]), int(date[1]), int(date[2])) #и конвертируем в объект datetime

        for athlete_ in session.query(Athlete).all(): #перебираем всех атлетов
            
            #ищем id атлета с ближайшим ростом
            if athlete_.height is not None:
                diff_height = abs(user_.height - athlete_.height) #разница в росте без учета знака
                if diff_height < diff_min: #если разница в росте меньше предыдущего значения diff_min
                    diff_min = diff_height #то записываем ее
                    athlete_nearest_height_id = athlete_.id #отмечаем id записи БД
            
            #ищем id атлета с ближайшей датой рождения
            if athlete_.birthdate is not None:
                date = athlete_.birthdate.split("-")
                athlete_birthdate = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
                diff_date = user_birthdate - athlete_birthdate #находим разницу между датами рождения в datatime.timedelta
                if abs(diff_date.days) < diff_date_min: #если разница рождения атлета меньше чем diff_date_min
                    diff_date_min = abs(diff_date.days) #записываем разницу в днях без знака
                    athlete_nearest_birthdate_id = athlete_.id # и его ID

        print("ID найден                  ", user_)
        print("Ближайший по росту атлет   ", session.query(Athlete).filter(Athlete.id == athlete_nearest_height_id).first())
        print("Ближайший по дате рождения ", session.query(Athlete).filter(Athlete.id == athlete_nearest_birthdate_id).first())
    else:
        print("ID не найден.")