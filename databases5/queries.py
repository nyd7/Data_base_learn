from models import Employee


if __name__ == '__main__':
    employee = Employee.query.first()
    print(employee.company.name)
