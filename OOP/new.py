class Employee:
    company = 'Infosys'
    department = 'IT'
    base_salary = 40000
    location = 'Pune'

    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary_paid = 0
        self.bonuses = {}
        # self.total_bonuses=tb

    def employee_detail(self):
        return f'''
        Employee ID: {self.emp_id}
        Name: {self.name}
        Age: {self.age}
        Department: {Employee.department}
        Company: {Employee.company}
        Location: {Employee.location}
        Bonuses: {self.bonuses}
        Salary Paid: ₹{self.salary_paid}
        '''
e1=Employee(101,'vaibhav arjun',12)
print(e1.employee_detail())