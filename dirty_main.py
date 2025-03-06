from application.salary import *
from application.db.people import *
from datetime import datetime
import pyjokes

if __name__ == '__main__':
    calculate_salary()
    get_employees()

    today = datetime.now()
    print("Сегодняшняя дата:", today.strftime("%d-%m-%Y"))

    print(pyjokes.get_joke(language='ru'))
