#this is my first approach to solve leetcode 701, created array with 1000001 slot which use more space, but easier way to solve the problem.

class MyHashMap:
    def __init__(self):
        self.arr = [None] * 1000001

    def put(self, key: int, val: int) -> None:
        self.arr[key] = val

    def get(self, key: int) -> int:
        val = self.arr[key]
        return val if val is not None else -1

    def remove(self, key: int) -> None:
        self.arr[key] = None

    def print_my_hash_vals(self):
        n = 0
        for i in self.arr:
            if i != None:
                print (n , i)
                n = n+1



myHash = MyHashMap()
myHash.put(5,2)
myHash.put(3,1)
myHash.put(8,3)
myHash.put(10,4)
myHash.remove(10)
print(myHash.get(8))
myHash.print_my_hash_vals()