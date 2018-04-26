import random 

def binary_search(array, x, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left > right:
        return False
    
    mid = (left + right) // 2
    value = array[mid]

    if x == value:
        return mid
    elif x > value:
        return binarySearch(array, x, mid + 1, right)
    elif x < value:
        return binarySearch(array, x , left, mid - 1)

if __name__ == "__main__":
    array = list(range(100000))
    x = random.randint(0, 100000)
    print(x)
    print(binarySearch(array, x))

