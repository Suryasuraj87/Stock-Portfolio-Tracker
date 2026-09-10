# Stock Portfolio Tracker

print("===== STOCK PORTFOLIO TRACKER =====")

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio = []

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment

    portfolio.append((stock_name, quantity, price, investment))

    print(f"{stock_name}: {quantity} shares × ${price} = ${investment}")


print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity, price, investment in portfolio:
    print(f"{stock} | Quantity: {quantity} | Price: ${price} | Investment: ${investment}")

print(f"\nTotal Investment: ${total_investment}")

# Save result to a text file
with open("portfolio_result.txt", "w") as file:
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=======================\n\n")

    for stock, quantity, price, investment in portfolio:
        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Investment: ${investment}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio result saved to portfolio_result.txt")
