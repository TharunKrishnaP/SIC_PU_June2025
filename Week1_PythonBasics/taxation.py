#LEVEL 1
def emp_log():
    name = input("Name: ")
    emp_id = input("EMP ID: ")
    base_sal = int(input("Basic Monthly salary: "))
    spl_allowance = int(input("Special allowances(monthly): "))
    bonus_per = int(input("Bonus percentage: "))
    gross_monthly_sal = base_sal + spl_allowance
    bonus = (bonus_per * gross_monthly_sal)/100
    annual_gross_sal = (gross_monthly_sal * 12) + bonus
    
    emp_dict = {"Name": name, "EMP ID": emp_id, "Base Salary": base_sal, 
                "Special Allowance": spl_allowance, "Bonus_per": bonus_per,
                "Monthly Gross Salary": gross_monthly_sal, "Bonus": bonus,
                "Annual Gross Salary": annual_gross_sal }
    return emp_dict

def print_log(dict):
    print("------------Employee details and Salary details--------------")
    for key, value in dict.items():
        print(f"{key} : {value}")

#LEVEL 2
def calculate_taxable_income(emp_dict):
    std_deduction = 50000
    taxable_income = emp_dict["Annual Gross Salary"] - std_deduction
    return std_deduction, taxable_income

def print_taxable_income(emp_dict):
    print("-----------------Taxable Income----------------------------")
    print("Standard deduction: ",Sd)
    print("Taxable Income: ",TI)

#LEVEL 3

def taxpayable(A):
    tax_payable = 0
    if TI>1500000:
        tax_payable += 0.30*TI
    elif TI>1200000:
        tax_payable += 0.20*TI
    elif TI>900000:
        tax_payable += 0.15*TI
    elif TI>600000:
        tax_payable += 0.10*TI
    elif TI>300000:
        tax_payable += 0.05*TI
    else:
        tax_payable = 0
    if TI<=700000:
        tax_payable = 0

    tax_payable = 0.04*tax_payable
    return tax_payable

def net_sal_calc(emp_dict):
    net_sal = emp_dict["Annual Gross Salary"] - TI
    return net_sal

def print_net_sal(emp_dict):
    print("------------------Net Salary Calculation------------------------")
    print("Annual Gross Salary: ",emp_dict["Annual Gross Salary"])
    print("Total tax payable: ",TP)
    print("Annual Net Salary: ",NetSal)

def report_generation(A):
    print_log(A)
    print_taxable_income(A)
    print_net_sal(A)

A = emp_log()
Sd, TI = calculate_taxable_income(A)
TP = taxpayable(A)
NetSal = net_sal_calc(A)
print("-------------------------Report----------------------------")
report_generation(A)
