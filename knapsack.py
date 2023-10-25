import random

def ggg(items, max_weight):
    value_sum = 0
    weight_sum = 0
    
    for item in items:
        value_sum += item.value
        weight_sum += item.weight
        
def make_combination(items, combination_length):
    combination = []
    for i in range(combination_length):
        random_item = random.choice(items)
        items.remove(random_item)
        combination.append(random_item)
    return combination
        

if __name__ == "__main__":  
    array = [
        {"v": 3, "w": 8},
    
        {"v": 5, "w": 3},
        
        {"v": 2, "w": 1},
        
        {"v": 6," w": 9},
    ]
    
    print(make_combination(array, 2))