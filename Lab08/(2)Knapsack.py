class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_weight(self):
        return self.weight
    
    def get_cost(self):
        return self.price / self.weight

def knapsack(itemList, amount):
    print(f"Knapsack Size: {amount} kg")
    print("===============================")
    
    selected_items = []
    total_weight = 0
    total_price = 0
    
    sorted_items = sorted(itemList, key=lambda item: item.get_cost(), reverse=True)
    
    for item in sorted_items:
        if total_weight + item.get_weight() <= amount:
            selected_items.append(item)
            total_weight += item.get_weight()
            total_price += item.get_price()
    
    for item in selected_items:
        print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
    
    print(f"Total: {total_price} THB")

def main():
    import json
    items = []
    num_items = int(input())
    
    for _ in range(num_items):
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
    
    knapsack_capacity = float(input())
    
    knapsack(items, knapsack_capacity)

main()
