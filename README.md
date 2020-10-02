B4.12 Домашнее задание

Вступление

В рамках домашнего задания к модулю нам предстоит проанализировать базу данных атлетов Олимпийских Игр в Сочи. Скачайте файл базы данных и, используя консольную утилиту sqlite3, проанализируйте содержимое этой базы данных:

Какие там есть таблицы?
Какова структура таблиц?
Какие типы данных используются для колонок?
Ответьте на следующие вопросы, используя консольную утилиту sqlite3 и язык структурированных запросов SQL:

Задание 1

Напишите модуль users.py, который регистрирует новых пользователей. Скрипт должен запрашивать следующие данные:

имя
фамилию
пол
адрес электронной почты
дату рождения
рост
Все данные о пользователях сохраните в таблице user нашей базы данных sochi_athletes.sqlite3.

Задание 2

Напишите модуль find_athlete.py поиска ближайшего к пользователю атлета. Логика работы модуля такова:

запросить идентификатор пользователя;
если пользователь с таким идентификатором существует в таблице user, то вывести на экран двух атлетов: ближайшего по дате рождения к данному пользователю и ближайшего по росту к данному пользователю;
если пользователя с таким идентификатором нет, вывести соответствующее сообщение.
