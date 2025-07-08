initial_deposit = float(input("Enter deposit amount: "))
house_cost = 800000
down_payment = house_cost * 0.25
months = 36

epsilon = 100
high = 1.0
low = 0.0
r = (high + low)/2.0
number_of_runs = 0

max_possible = initial_deposit * (1 + 1/12)**months
if down_payment - epsilon > max_possible :
    print("Best savings rate: None")
    print("Steps in bisection search: 0")
    exit()
amount_saved = initial_deposit * (1 + r/12)**months
while abs(amount_saved - down_payment) >= epsilon:
    print(r)
    print(f"{amount_saved - down_payment}")
    if amount_saved > down_payment:
        high = r
    else:
        low = r
    r = (high + low)/2.0
    number_of_runs += 1
    amount_saved = initial_deposit * (1 + r/12)**months

print(f"Best savings rate: {r}")
print(f"Number of Runs: {number_of_runs}")
