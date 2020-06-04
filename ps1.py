# total_cost = float(input('What is the cost of your dream house: '))
# annual_salary = float(input("What is your annual salary: "))
# portion_saved = float(input('What portion of your annual salary will you be saving? As a percent(number only): '))/100
# semi_annual_raise = float(input('What is your semi annual raise as a decimal percentage: '))
# portion_down_payment = 0.25 * total_cost
# current_savings = 0
# monthly_salary = annual_salary/12
# r = 0.04
# months_to_pay_down_payment = 0
#
# while(current_savings<portion_down_payment):
#     months_to_pay_down_payment += 1
#     current_savings += current_savings * r/12
#     current_savings += portion_saved * monthly_salary
#     if(months_to_pay_down_payment%6 == 0):
#         monthly_salary+= monthly_salary * semi_annual_raise
# print(months_to_pay_down_payment)
# ^ part a and b
import math
# Part C
def myFunc(portion,annual_salary):
    total_cost = 1000000
    semi_annual_raise = 0.07
    portion_saved = portion/100000
    portion_down_payment = 0.25 * total_cost
    current_savings = 0
    monthly_salary = annual_salary/12
    r = 0.04
    months_to_pay_down_payment = 0

    while(current_savings<(portion_down_payment-100)):
        months_to_pay_down_payment += 1
        current_savings += current_savings * r/12
        current_savings += portion_saved * monthly_salary
        if(current_savings>=portion_down_payment and current_savings < portion_down_payment+100):
            return months_to_pay_down_payment
        if(months_to_pay_down_payment%6 == 0):
            monthly_salary+= monthly_salary * semi_annual_raise
    return months_to_pay_down_payment

annual_salary = float(input("What is your annual salary: "))
goal = 36
current = 0
min = 1
max = 10000
iterations = 0
while(max-min > 2):
    print(iterations)
    iterations+=1
    options = max-min +1
    lower = min + math.floor(options/2) - 1
    upper = lower + 1
    upp = myFunc(upper,annual_salary)
    low = myFunc(lower,annual_salary)
    print(upp,low) # currently getting months value from myfunc but why not instead make it so get total after three years
    if(upp==goal):
        current = 1
        print("iterations: ", iterations)
        print("percent to save: ", upper/100)
        break
    if(low==goal):
        current = 1
        print("iterations: ", iterations)
        print("percent to save: ", lower/100)
        break
    if(abs(goal-upp)<abs(goal-low)):
         min = upper
    else:
        max = lower
if(max-min<3 and current == 0):
    for i in range(min,max+1):
        ret = myFunc(i,annual_salary)
        if(ret==goal):
            print("iterations: ", iterations+1)
            print("percent to save: ", i/100)
            break
if(current == 0):
    print('no savings rate can get you there')
