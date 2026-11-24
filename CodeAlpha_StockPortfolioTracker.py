import csv


def save_to_txt(portfolio, stock_prices, total_investment, filename="portfolio_summary.txt"):
    """Saves the stock portfolio summary to a plain text (.txt) file."""
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write("==================================================\n")
        file.write("             STOCK PORTFOLIO SUMMARY              \n")
        file.write("==================================================\n")
        file.write(f"{'Stock':<10}{'Shares':<10}{'Price ($)':<12}{'Total Value ($)':<15}\n")
        file.write("--------------------------------------------------\n")
        for ticker, quantity in portfolio.items():
            price = stock_prices[ticker]
            value = quantity * price
            file.write(f"{ticker:<10}{quantity:<10}${price:<11,.2f}${value:<14,.2f}\n")
        file.write("--------------------------------------------------\n")
        file.write(f"TOTAL INVESTMENT VALUE: ${total_investment:,.2f}\n")
        file.write("==================================================\n")
    print(f"Saved text summary to '{filename}'.")


def save_to_csv(portfolio, stock_prices, total_investment, filename="portfolio_summary.csv"):
    """Saves the stock portfolio summary to a comma-separated (.csv) file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Ticker", "Quantity", "Price per Share ($)", "Total Value ($)"])
        for ticker, quantity in portfolio.items():
            price = stock_prices[ticker]
            value = quantity * price
            writer.writerow([ticker, quantity, f"{price:.2f}", f"{value:.2f}"])
        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT", "", "", f"{total_investment:.2f}"])
    print(f"Saved CSV summary to '{filename}'.")


def run_portfolio_tracker():
    # Step 1: Hardcoded dictionary of stock prices (in USD)
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 140.00,
        "MSFT": 415.00,
        "AMZN": 185.00,
        "NVDA": 135.00,
    }

    # Dictionary to store the user's selected stocks and quantities
    portfolio = {}

    print("==================================================")
    print("       Welcome to the Stock Portfolio Tracker     ")
    print("==================================================")
    print("Available Stocks & Current Prices:")
    for ticker, price in stock_prices.items():
        print(f"  - {ticker:<6}: ${price:,.2f} per share")
    print("--------------------------------------------------")

    # Step 2: Loop to collect stock names and share quantities from the user
    while True:
        ticker = input("\nEnter a stock symbol to add (or type 'done' to finish): ").strip().upper()

        if ticker == "DONE":
            break

        if ticker not in stock_prices:
            print(f"'{ticker}' is not in the price list. Choose from: {', '.join(stock_prices.keys())}")
            continue

        quantity_input = input(f"Enter number of shares for {ticker}: ").strip()
        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("Invalid quantity! Please enter a positive whole number.")
            continue

        quantity = int(quantity_input)
        portfolio[ticker] = portfolio.get(ticker, 0) + quantity
        print(f"Added {quantity} share(s) of {ticker} at ${stock_prices[ticker]:,.2f} each.")

    # Step 3: Check if portfolio has any stocks and calculate total investment
    if not portfolio:
        print("\nNo stocks were added to your portfolio. Exiting tracker.")
        return

    total_investment = 0.0
    print("\n==================================================")
    print("             YOUR PORTFOLIO BREAKDOWN             ")
    print("==================================================")
    print(f"{'Stock':<10}{'Shares':<10}{'Price ($)':<12}{'Total Value ($)':<15}")
    print("--------------------------------------------------")

    for ticker, quantity in portfolio.items():
        price = stock_prices[ticker]
        value = quantity * price
        total_investment += value
        print(f"{ticker:<10}{quantity:<10}${price:<11,.2f}${value:<14,.2f}")

    print("--------------------------------------------------")
    print(f"TOTAL INVESTMENT VALUE: ${total_investment:,.2f}")
    print("==================================================")

    # Step 4: Optionally save the result to a .txt or .csv file
    save_choice = input(
        "\nWould you like to save your portfolio? Enter 'txt', 'csv', 'both', or 'no': "
    ).strip().lower()

    if save_choice == "txt":
        save_to_txt(portfolio, stock_prices, total_investment)
    elif save_choice == "csv":
        save_to_csv(portfolio, stock_prices, total_investment)
    elif save_choice == "both":
        save_to_txt(portfolio, stock_prices, total_investment)
        save_to_csv(portfolio, stock_prices, total_investment)
    else:
        print("Portfolio was not saved to a file. Goodbye!")


if __name__ == "__main__":
    run_portfolio_tracker()
