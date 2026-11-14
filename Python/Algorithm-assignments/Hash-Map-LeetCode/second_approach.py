# instade of creating a 1000001 iteams in one aray, we can do a 1000 aray in one array, but we have to deal with collision , and it will be less size than my first approach.
class MyHashMap:
    def __init__(self):
        self.arr = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        bucket = self.arr[key % 1000]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket = self.arr[key % 1000]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = self.arr[key % 1000]
        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                return



