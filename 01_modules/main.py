

from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime as dt
from permutation import Permutation


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print('Текущая дата:', dt.date(dt.now()))
    for p in Permutation.group(3):
        print(p)