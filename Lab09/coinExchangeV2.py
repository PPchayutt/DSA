def convert_key(data):
    return {int(k): v for k, v in data.items()}


def coinExchangeV2(amount, coins):
    coin_values = sorted(coins.keys(), reverse=True)
    
    dp = {0: {cv: 0 for cv in coin_values}}

    for i in range(1, amount + 1):
        dp[i] = None 
        for cv in coin_values:
            if i >= cv and dp[i - cv] is not None and dp[i - cv][cv] < coins[cv]:
                new_coins = dp[i - cv].copy()
                new_coins[cv] += 1
                
                if dp[i] is None or sum(new_coins.values()) < sum(dp[i].values()):
                    dp[i] = new_coins
    
    print(f"Amount: {amount}")
    if dp[amount] is None:
        print("Can not exchange.")
    else:
        print("Coin exchange result:")
        total_coins = 0
        for cv in coin_values:
            count = dp[amount][cv]
            print(f"  {cv} baht = {count} coins")
            total_coins += count
        print(f"Number of coins: {total_coins}")


def main():
    import json
    amount = int(input())
    coins = convert_key(json.loads(input()))
    coinExchangeV2(amount, coins)
main()
