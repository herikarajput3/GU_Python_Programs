# Create a program name “employee.py” and implement the functions DA, HRA, PF, and ITAX. Create another program that uses the function of employee module and calculates gross and net salaries of an employee.

# Import the employee module
import employee

# Function to calculate gross salary
def gross_salary(basic_salary):
    da = employee.DA(basic_salary)
    hra = employee.HRA(basic_salary)
    return basic_salary + da + hra

# Function to calculate net salary
def net_salary(basic_salary):
    gross = gross_salary(basic_salary)
    pf = employee.PF(basic_salary)
    itax = employee.ITAX(basic_salary)
    return gross - (pf + itax)

# Main program to take input and calculate salaries
basic_salary = float(input("Enter basic salary of the employee: "))

gross = gross_salary(basic_salary)
net = net_salary(basic_salary)

print(f"Gross Salary: {gross}")
print(f"Net Salary: {net}")