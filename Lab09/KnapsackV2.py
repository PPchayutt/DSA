import json
def knapsackV2(amount, itemlist):
    n = len(itemlist)
    dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        name, price, weight = itemlist[i-1]
        for w in range(amount + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + price)
            else:
                dp[i][w] = dp[i-1][w]
    w = amount
    selected = []
    for i in range(n, 0, -1):
        name, price, weight = itemlist[i-1]
        if weight <= w and dp[i][w] == dp[i-1][w-weight] + price:
            selected.append([name, price, weight])
            w -= weight
    selected.sort(key=lambda x: x[0])
    total_price = sum(item[1] for item in selected)
    return total_price, selected

def main():
    itemlist_str = input().strip()
    itemlist = json.loads(itemlist_str)
    amount = int(input().strip())
    total_price, selected_items = knapsackV2(amount, itemlist)
    print(f"Total: {total_price}")
    for name, price, weight in selected_items:
        print(f"{name} -> {weight} kg -> {price} THB")
main()
