total_cost = float(input('What is the cost of your dream house: '))
annual_salary = float(input("What is your annual salary: "))
portion_saved = float(input('What portion of your annual salary will you be saving? As a percent(number only): '))/100
semi_annual_raise = float(input('What is your semi annual raise as a decimal percentage: '))
portion_down_payment = 0.25 * total_cost
current_savings = 0
monthly_salary = annual_salary/12
r = 0.04
months_to_pay_down_payment = 0

while(current_savings<portion_down_payment):
    months_to_pay_down_payment += 1
    current_savings += current_savings * r/12
    current_savings += portion_saved * monthly_salary
    if(months_to_pay_down_payment%6 == 0):
        monthly_salary+= monthly_salary * semi_annual_raise
print(months_to_pay_down_payment)
