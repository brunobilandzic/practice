import math, random


def fact(n):
    if n==1 or n==0 or n<0:
        return 1
    else: return n*fact(n-1)   
    

def get_random(max):
    if(max<=3): return 1
    return math.floor(random.random() * max)


if __name__ == "__main__":
    print(fact(10))