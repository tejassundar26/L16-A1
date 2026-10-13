
def calculate_change(paid, price):
    change = paid - price
    return change

snack_price = 40
print("===== SNACK VENDING MACHINE =====")
print(f"This snack costs {snack_price} units.")
print("Accepted coins: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin (8 , 16, 24 or 40): "))

    if coin != 8 and coin != 16 and coin != 24 and coin != 40:
        print("Invalid coin, try again!\n")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")

    if total_inserted >= snack_price:
        print("Enough money inserted!\n")
        break

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing your snack...")

if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")

print("\n===== PURCHASE SUMMARY =====")
print("Snack Price:", snack_price)
print("Coins Inserted:", coins_inserted)
print("Total Paid:", total_inserted)
print("Change Given:", change_due)
print("=============================")
print("Thanks for your purchase!")
# End of program










