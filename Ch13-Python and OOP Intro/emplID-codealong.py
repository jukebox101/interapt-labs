class EmployeeMethods:
    def __init__(self, empID, empName, empDept, empSalary):
        # _ shows this shouldn't be accessed directly
        self._emp_ID = empID
        # _ shows this shouldn't be accessed directly
        self._emp_name = empName
        self._emp_dept = empDept
        self._emp_salary = empSalary

        @property
        def emp_salary(self):
            return self._emp_salary
        
        @emp_salary.setter
        def emp_salary(self, new_sal):
            if 30_000 <= new_sal <= 200_000:
                self._emp_salary = new_sal
            else:
                print(f"new salary not in range. Salary set to 'None'")
                self._emp_salary = None

        def print_me(self):
            print(f'{self._emp_ID}\t{self._emp_name}\t{self._emp_dept}\t{self._emp_salary}')

        def give_emp_pct_raise(self, pct_raise):
            if pct_raise < 10 or pct_raise > 20:
                print(f'Raise percentage {pct_raise} out of range - no change made')
            elif self._emp_salary is None:
                print(f'Employee with Id: {self._emp_ID} has no valid salary - no change made')
            else:
                self._emp_salary = self._emp_salary * (1 + pct_raise/100)
                if self._emp_salary > 200_000:
                    self._emp_salary = 200_000