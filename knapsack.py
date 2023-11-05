import random
import math
from tools import fact, get_random, print_enumerable

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
    num_combs = fact(items_length) / (fact(items_length-comb_length)*fact(comb_length))
    item_used = fact(items_length-1)/ (fact(comb_length - 1)*fact((items_length -1) - (comb_length - 1)))
    
    
    items_list = generate_items()
    
    items = dict()
    
    items["comb_length"] = comb_length
    items["num_combs"] = num_combs
    items["item_used"] = item_used
    items["data"] = items_list
            
    return items
    

if __name__ == "__main__":  
    items = task()
    print(print_enumerable(items["data"]))
    