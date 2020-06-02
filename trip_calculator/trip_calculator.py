distance = int(input("How many kilometers did you drive? "))
liters_per_km = int(input("How many liters-per-kilometer did the car use? "))
price = float(input("How much is it per liter of fuel? "))

total = (distance / liters_per_km) * price
print("The total cost of the trip will be $" + str(round(total, 2)))
