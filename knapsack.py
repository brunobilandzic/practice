import random
import math
from tools import fact, get_random

items_max_length = 20
max_value = 100
max_weight = 100

items_length =  get_random(items_max_length)



def generate_item():
    return {
        "value" : get_random(max_value),
        "weight": get_random(max_weight)
    }


def generate_items():
    items = []
    
    for i in range(items_length):
        new_item = generate_item()
        items.append(new_item)
        
    return items
    


def task():
    comb_length = items_length - get_random(items_length)
    num_combinations = fact(items_length) / (fact(items_length-comb_length)*fact(comb_length))
    item_used_times = fact(items_length-1)/ (fact(comb_length - 1)*fact((items_length -1) - (comb_length - 1)))
    
    print(f"items length: {items_length}\ncombination length: {comb_length}\nnumber of combinations: {num_combinations}\neach item used {item_used_times} times")
    
    
    
     



if __name__ == "__main__":  
    task()