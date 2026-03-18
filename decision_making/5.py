"""5. Grade Calculator
Input marks and assign grades:
90+ → A
75–89 → B
50–74 → C
Below 50 → Fail"""
marks = int(input())

if marks >= 90:
    print("A")
elif 90 > marks >= 75:
    print("B")
elif 75 > marks >= 50 :
    print("C")
else:
    print("Failed")