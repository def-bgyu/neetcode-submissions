class TimeMap:

    def __init__(self):
        self.dict_ds = {}
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict_ds:
            self.dict_ds[key] = []
        self.dict_ds[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict_ds:
            return ""

        left = 0
        right = len(self.dict_ds[key]) -1
        pairs = self.dict_ds[key]
        result = ""

        while left <= right:
            mid = (left+right) //2

            if pairs[mid][0] <=timestamp:
                result = pairs[mid][1]
                left = mid + 1
            else:
                right = mid -1
        return result
