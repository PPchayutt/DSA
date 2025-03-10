"""Labs 09.02 - KnapsackV2 using Dynamic Programming"""
import json

class Item:
    """Item Class for Knapsack Problem"""
    def __init__(self, name, price, weight):
        """Initialize item with name, price, and weight"""
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        """Return item name"""
        return self.name

    def get_price(self):
        """Return item price"""
        return self.price

    def get_weight(self):
        """Return item weight"""
        return self.weight

def knapsackV2(amount, itemlist):
    """Solve knapsack problem using dynamic programming
       Returns the maximum value and selected items"""
    # Convert itemlist to list of Item objects if it's not already
    items = []
    for item in itemlist:
        if isinstance(item, list):  # If input is in the format [name, price, weight]
            items.append(Item(item[0], item[1], item[2]))
        else:  # Already an Item object
            items.append(item)
    
    n = len(items)
    
    # Create DP table: dp[i][w] represents the maximum value that can be obtained
    # using the first i items and with maximum weight w
    dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(amount + 1):
            # If current item weight exceeds current capacity, skip it
            if items[i-1].get_weight() > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Choose the better: (1) not taking the item, or (2) taking the item
                dp[i][w] = max(
                    dp[i-1][w],  # Not taking the item
                    dp[i-1][w - items[i-1].get_weight()] + items[i-1].get_price()  # Taking the item
                )
    
    # Backtrack to find which items to select
    selected_items = []
    w = amount
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            # This item was included
            selected_items.append(items[i-1])
            w -= items[i-1].get_weight()
    
    # Sort selected items alphabetically
    selected_items.sort(key=lambda item: item.get_name())
    
    # Calculate total value
    total_value = sum(item.get_price() for item in selected_items)
    
    # Return total and selected items
    return total_value, selected_items

def main():
    """Main function to handle input and output"""
    # Read input
    try:
        # Read itemlist as JSON
        itemlist_str = input()
        itemlist = json.loads(itemlist_str)
        
        # Read maximum weight
        amount = int(input())
        
        # Solve knapsack problem
        total_value, selected_items = knapsackV2(amount, itemlist)
        
        # Format output
        print(f"Total: {total_value}")
        for item in selected_items:
            print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()