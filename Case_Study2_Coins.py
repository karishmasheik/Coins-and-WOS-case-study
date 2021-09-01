# defining coinQty function
def coinQty(X, coins):
    value = [1, 0.50, 0.20, 0.10, 0.05]
    change = [0, 0, 0, 0, 0]
    i = 4
    while(X != 0):
        if coins[i] != 0:
            if coins[i]*value[i] > X:
                coins[i] = coins[i]-1
            else:
                X = X - coins[i]*value[i]
                change[i] = coins[i]
                i-=1
        else:
            i-=1
    return change

# Total value of coins paid to the customer
X = float(input("Enter the total change required.\n"))


# Each coins denomination
# Enter only 5 numbers with one space between the numbers like 3 7 0 0 0
coins = list(map(int, input("Enter the denomination of the coins with spaces between them.\n").split(" ")))

# Maximum Quantity of each coin denomination to pay the customer
print(coinQty(X,coins))
