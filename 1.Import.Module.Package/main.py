from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date






if __name__ == '__main__':
    today = date.today()
    print(f"Текущая дата: {today}")
    employees = get_employees()
    salary = calculate_salary()
    
