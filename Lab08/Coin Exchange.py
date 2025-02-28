def coinExchange(amount, coins):
    print(f"Amount: {amount}")
    used_coins = {10: 0, 5: 0, 2: 0, 1: 0}
    remaining = amount
    
    for coin_value in sorted(coins.keys(), reverse=True):
        coins_needed = min(remaining // coin_value, coins[coin_value])
        used_coins[coin_value] = coins_needed
        remaining -= coins_needed * coin_value
    
    if remaining > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        total_coins = sum(used_coins.values())
        for coin_value in sorted(used_coins.keys(), reverse=True):
            print(f"  {coin_value} baht = {used_coins[coin_value]} coins")
        print(f"Number of coins: {total_coins}")

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def main():
    import json
    amount = int(input())
    coin_data = input()
    coins = convert_key(json.loads(coin_data))
    coinExchange(amount, coins)

main()
