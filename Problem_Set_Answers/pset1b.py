yearly_salary = float(input("Enter much you make per year: "))
portion_saved = float(input("What percentage of your salary do you want to save? Enter in decimal form: "))
cost_of_dream_house = float(input("Enter cost of dream house: "))
sa_raise = float(input("Enter your semi annual raise rate: "))
portion_down_payment = 0.25 * cost_of_dream_house

amount_saved = 0.0
monthly_wage = yearly_salary/12
r = 0.05
months_saved = 0

while amount_saved < portion_down_payment:
    if months_saved > 0 and months_saved%6 == 0:
        yearly_salary += yearly_salary * sa_raise
        monthly_wage = yearly_salary/12
    amount_saved += (r/12) * amount_saved
    amount_saved += monthly_wage * portion_saved 
    months_saved += 1

if amount_saved >= portion_down_payment:
    print(f"To save £{portion_down_payment}, you would need to save for {months_saved} months.")