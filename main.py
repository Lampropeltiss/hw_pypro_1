import application.salary as salary
import application.db.people as people
from datetime import datetime
import pyjokes

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()

    today = datetime.now()
    print("Сегодняшняя дата:", today.strftime("%d-%m-%Y"))

    print(pyjokes.get_joke(language='ru'))
