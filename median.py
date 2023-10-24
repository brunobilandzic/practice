import math
import random

def sort(arr1, arr2):
    sorted = arr1 + arr2
    sorted.sort()
    print(f"\n Sorded: \n\n {sorted}\n\n")
    return sorted


def median(arr1, arr2):
    sorted = sort(arr1, arr2)
    length = len(sorted)
    
    if(length % 2 == 0):
        print("\neven\n")
        return (sorted[math.floor(length / 2) - 1] + sorted[math.floor(length/2) ]) / 2
    else:
        print("\nodd\n")
        return sorted[math.floor(length/2)]
    
def generate(maxSize):
    randomArray = []
    size = math.floor(1 + random.random() * maxSize)
    
    
    for i in range(0, size):
        isNegative = -1 if random.random() > 0.5  else 1
        randomArray.append(isNegative * random.random() * 1000)
        
    return randomArray

def testmedian():
    arr1 = generate(5)
    arr2 = generate(5)
    
    print(f"arr1:\n\n {arr1}\n\n")
    print(f"arr2:\n\n {arr2}\n\n")
    
    print(f"Median: \n\n {median(arr1, arr2)}\n\n")
    

if __name__ == "__main__":
    testmedian()