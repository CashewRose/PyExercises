class Company():

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = list()

    def get_company_name(self):
        return self.company_name

    def set_company_name(self, new_name):
        self.company_name = new_name

    def get_company_founded_date(self):
        return self.date_founded

    def new_employee(self, employee_instance):
        self.employees.append(employee_instance)

    def __str__(self):
        name = f'The employees at {self.company_name}: '
        for employee in self.employees:
            name += f'{employee.name} '
        return name
class Employee():

    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

    def get_employee_name(self):
        return self.name

    def get_employee_job_title(self):
        return self.job_title

    def get_employee_start_date(self):
        return self.start_date

    def set_new_job_title(self, new_job):
        self.job_title = new_job

    def set_new_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return self.name

Eventbrite = Company("EventBrite", "2009")

Susan = Employee("Susan", "Junior Dev", "01/10/2012")
Josh = Employee("Josh", "Food Rabi", "10/11/2018")
Rashad = Employee("Rashad", "Senior Engineer", "03/20/2009")

Eventbrite.new_employee(Susan)
Eventbrite.new_employee(Josh)
Eventbrite.new_employee(Rashad)