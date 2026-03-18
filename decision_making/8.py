"""8. Electricity Bill
Calculate bill based on units:
First 100 units → ₹5/unit
Next 100 → ₹7/unit
Above 200 → ₹10/unit"""

units = int(input())
if units <= 100:
    bill = units*5
elif units <= 200:
    bill = (100*5) + (100-units)*7
else:
    bill = (100*5) + (100*7) + (units-200)*10

print("Total bill = ₹", bill)
