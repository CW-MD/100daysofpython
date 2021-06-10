#tip Calculator
Welcome_Message = "Welcome to the Tip Calculator"

print(Welcome_Message)

totalBill = float(input('What was the total bill? '))
percent = float(input('What percentage would you like to tip? '))
groupSize = int(input('How many people are in your party? '))
ConvertedCost = (totalBill * (1.0 +(percent / 100)  )) /groupSize
print(f"Each person should pay {ConvertedCost}")
