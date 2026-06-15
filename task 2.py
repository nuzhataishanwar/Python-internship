#TASK 2: Stock Portfolio Tracker
"""
● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock
prices.
● Simplified Scope:
○ User inputs stock names and quantity.
○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}).
○ Display total investment value and optionally save the result in a .txt or .csv file.
● Key Concepts Used: dictionary, input/output, basic arithmetic
"""
prices={
    "AAPL":312, "GGLE":376, "NTRC": 234
}
n=int(input("how many stocks you want?"))
total=0
for i in range(n):
    stock=input("enter the name of stock you want:")
    if stock in prices:
        quantity=int(input("how many stock you want of" + stock + ":"))
        total+=prices[stock] * quantity
        print("your total investment is", total)
    else:
        print("stock not found")
        print("enter one of these stock: AAPL, GGLE, NTRC")