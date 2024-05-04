from abc import ABC, abstractmethod
from src.users.resumen_response import resumen_response

class Visitor(ABC):
    @abstractmethod
    def visit_employee(self, employee):
        pass


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def accept(self, visitor):
        visitor.visit_employee(self)


class SalaryMetricsVisitor(Visitor):
    def __init__(self):
        self.total_salary = 0
        self.average_salary = 0
        self.num_employees = 0

    def visit_employee(self, employee):
        self.total_salary += employee.salary
        self.num_employees += 1

    def calculate_metrics(self)->resumen_response:
        resumen=resumen_response(0, 0, 0)
        if self.num_employees > 0:
            self.average_salary = self.total_salary / self.num_employees
            print(f"Número total de empleados: {self.num_employees}")
            print(f"Salario total de todos los empleados: {self.total_salary}")
            print(f"Salario promedio: {self.average_salary}")
            resumen=resumen_response(self.num_employees, self.total_salary, self.average_salary)
        else:
            print("No hay empleados para calcular métricas de salario.")
        return resumen


employees = [
    Employee("Juan", 3000),
    Employee("María", 4000),
    Employee("Pedro", 3500),
]

salary_metrics_visitor = SalaryMetricsVisitor()


for employee in employees:
    employee.accept(salary_metrics_visitor)

salary_metrics_visitor.calculate_metrics()

