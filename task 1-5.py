# Расчеет прибыли компании
revenue = int(input("Enter revenue your company: "))
costs = int(input("Enter the company's costs: "))
if revenue < costs:
    print(f"your losses ", costs - revenue)
else:
    debet = revenue - costs
    print(f"your profit was ", debet, "this is", debet * costs // revenue / 100, "%")
    working = int(input("enter the number of employees "))
    print("profit per 1 employee ", debet//working)
